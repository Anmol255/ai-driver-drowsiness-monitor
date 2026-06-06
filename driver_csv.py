import cv2
import csv
import os
import time
from datetime import datetime

# Load Haar Cascade Classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# Start Webcam
cap = cv2.VideoCapture(0)

closed_frames = 0
drowsiness_score = 0
blink_count = 0
eyes_previously_closed = False

alert_count = 0
alert_active = False

max_drowsiness_score = 0
start_time = time.time()

# CSV File
log_file = os.path.join(
    os.path.dirname(__file__),
    "drowsiness_log.csv"
)

print("Saving CSV to:")
print(os.path.abspath(log_file))

with open(log_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Timestamp",
        "Drowsiness Score",
        "Blink Count",
        "Alert Number"
    ])

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Face Detection
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Keep only the largest face
    if len(faces) > 0:

        faces = sorted(
            faces,
            key=lambda f: f[2] * f[3],
            reverse=True
        )

        faces = [faces[0]]

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray
        )

        # Eye Logic
        if len(eyes) == 0:

            closed_frames += 1
            drowsiness_score += 1

            if not eyes_previously_closed:
                blink_count += 1
                eyes_previously_closed = True

        else:

            closed_frames = 0
            eyes_previously_closed = False

            if drowsiness_score > 0:
                drowsiness_score -= 1

        # Track maximum score
        if drowsiness_score > max_drowsiness_score:
            max_drowsiness_score = drowsiness_score

        # Draw eye rectangles
        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

    # Display Stats
    cv2.putText(
        frame,
        f"Drowsiness Score: {drowsiness_score}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Blinks: {blink_count}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Alerts: {alert_count}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    # Alert Logic
    if drowsiness_score > 20:

        if not alert_active:

            alert_count += 1
            alert_active = True

            with open(log_file, "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    drowsiness_score,
                    blink_count,
                    alert_count
                ])

        cv2.putText(
            frame,
            "DROWSINESS ALERT!",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    else:
        alert_active = False

    cv2.imshow(
        "Driver Drowsiness Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

# Session Report
session_duration = int(
    time.time() - start_time
)

minutes = session_duration // 60
seconds = session_duration % 60

print("\n========= SESSION REPORT =========")
print("Total Blinks:", blink_count)
print("Total Alerts:", alert_count)
print("Maximum Drowsiness Score:", max_drowsiness_score)
print(f"Session Duration: {minutes}m {seconds}s")
print("==================================")