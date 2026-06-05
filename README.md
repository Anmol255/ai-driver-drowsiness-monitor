# ai-driver-drowsiness-monitor
# AI Driver Drowsiness Monitor

A real-time computer vision system that detects driver drowsiness using facial and eye analysis with OpenCV.

## Features

* Real-time face detection
* Eye detection and monitoring
* Blink counting
* Drowsiness score calculation
* Driver alert system
* Alert counting
* CSV event logging
* Session analytics report
* Largest-face tracking for improved robustness when multiple people appear in the frame

## Technologies Used

* Python
* OpenCV
* Haar Cascade Classifiers
* CSV Logging

## How It Works

The system continuously captures frames from a webcam and detects the driver's face and eyes.

* When eyes are detected, the drowsiness score decreases.
* When eyes remain closed, the drowsiness score increases.
* If the score exceeds a threshold, a drowsiness alert is triggered.
* Blink counts and alert events are tracked.
* Alert events are automatically saved to a CSV file with timestamps.
* At the end of the session, a report is generated containing:

  * Total blinks
  * Total alerts
  * Maximum drowsiness score
  * Session duration

## Project Highlights

* Real-time video processing
* Driver-focused tracking using largest-face selection
* Event logging and analytics
* Lightweight implementation suitable for learning computer vision concepts

## Future Improvements

* Eye Aspect Ratio (EAR) based detection
* Facial landmark tracking
* Audio alerts
* Dashboard visualization
* Fatigue trend analysis

## Run the Project

```bash
pip install -r requirements.txt
python driver_csv.py
```

Press `Q` to exit the application.

## Author

Anmol K
