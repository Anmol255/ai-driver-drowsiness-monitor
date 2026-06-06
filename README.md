# AI Driver Drowsiness Monitoring System

A real-time computer vision application that monitors driver alertness using facial and eye analysis. The system detects signs of drowsiness, triggers audio warnings, logs alert events, and generates session analytics.

---

## Features

### Real-Time Monitoring

* Face Detection using Haar Cascade Classifiers
* Eye Detection and Tracking
* Driver-focused Largest Face Selection
* Live Webcam Processing

### Drowsiness Analysis

* Eye Closure Detection
* Dynamic Drowsiness Score Calculation
* Blink Counting
* Real-Time Drowsiness Alerts

### Safety Features

* Visual Alert Display
* Audio Warning System (Hooter/Buzzer)
* Multiple Alert Tracking

### Data Logging & Analytics

* Automatic CSV Event Logging
* Timestamped Alert Records
* Session Statistics Generation
* Maximum Drowsiness Score Tracking

---

## Technology Stack

* Python
* OpenCV
* Haar Cascade Classifiers
* CSV Logging
* Winsound (Audio Alerts)

---

## Project Workflow

1. Capture live webcam feed.
2. Detect the driver's face.
3. Track only the largest face when multiple people appear.
4. Detect eyes within the face region.
5. Calculate drowsiness score based on eye closure duration.
6. Count blinks in real time.
7. Trigger visual and audio alerts when drowsiness exceeds a threshold.
8. Log alert events to a CSV file.
9. Generate a session report after program termination.

---

## Output Metrics

The system tracks:

* Total Blink Count
* Total Alert Count
* Maximum Drowsiness Score
* Session Duration
* Alert Event History

---

## Sample CSV Output

| Timestamp           | Drowsiness Score | Blink Count | Alert Number |
| ------------------- | ---------------- | ----------- | ------------ |
| 2026-06-03 13:49:57 | 22               | 16          | 1            |
| 2026-06-03 13:50:04 | 21               | 37          | 2            |

---

## Project Structure

```text
ai-driver-drowsiness-monitor/
│
├── driver_csv.py
├── drowsiness_log.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

```bash
pip install opencv-python
```

---

## Run

```bash
python driver_csv.py
```

Press **Q** to exit the application.

---

## Future Enhancements

* Eye Aspect Ratio (EAR) based detection
* Facial Landmark Tracking
* Fatigue Trend Analysis
* Dashboard Visualization
* Real-Time Performance Charts
* Driver Behavior Analytics

---

## Author

Anmol K

Computer Vision • Artificial Intelligence • Machine Learning

