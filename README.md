# Football Analysis System

A minimal, robust football match video analysis system using YOLOv11l for detection and ByteTrack for tracking. It processes match footage to detect and track players, referees, and the ball, and outputs annotated video files.
heres a quick Youtube link for the kind of output u can expect https://youtu.be/IQ8Muetic8Q.

## Features
- ⚽ Player, referee, and ball detection via YOLOv11l
- 🎯 Object tracking using ByteTrack
- 🔧 Configurable favorite team overlay (see `config.yaml`)
- 🖥️ Simple CLI interface


### 🛠️ Challenges

While developing this system, I faced and addressed several key challenges:

- **Accurate Object Detection:**  
  Differentiating between players, referees, and the ball required fine-tuning YOLOv11l anchors and confidence thresholds to minimize false positives and missed detections.

- **Small Object (Ball) Tracking:**  
  The ball’s small size and rapid motion led to frequent lost tracks. Integrating ByteTrack with custom motion models and increasing frame-rate interpolation helped maintain continuity.

- **Team Classification:**  
  Assigning detected players to teams based on jersey colors was complicated by varying lighting and resolution. Implementing color-space normalization and dynamic clustering improved classification accuracy.

- **Annotation Overlay Synchronization:**  
  Ensuring labels, bounding boxes, and team overlays stayed correctly aligned during fast camera pans required optimized buffer handling and GPU-accelerated rendering in OpenCV.

- **Performance Optimization:**  
  Processing high-resolution videos in real time demanded balancing model precision with inference speed. Strategies included batching frames, model quantization, and multi-threaded I/O pipelines.

- **Modular CLI Design:**  
  Building a user-friendly CLI that could handle different modes (detection-only, detection + tracking) led to designing a clear command syntax and input validation routines.

- **Configurable Workflow:**  
  Abstracting configuration for favorite team overlay and model selection into `config.yaml` meant designing a flexible parser and error-handling when user parameters were missing or invalid.

These challenges shaped the system’s design and performance, laying a solid foundation for future extensions like speed analysis and tactical heatmaps.


## 🚀 Potential Extensions

- Frame-by-frame player speed estimation  
- Team classification by jersey color  
- Positional heatmaps and tactical overlays  
- Real-time live detection on streaming video  

## Installation
    git clone git@github.com:batraa11/Machine-Learning-Research-Projects.git
    cd Machine-Learning-Research-Projects
    pip install -r requirements.txt

## Configuration
    favorite_team: "YourTeamName"  # in config.yaml

## Usage
    python main.py
Follow prompts to select your input video (in `input_videos/`) and YOLO model (in `models/`). Outputs are saved to `output_videos/`. I added that I trained for you in there.

## Project Structure
    .
    ├── input_videos/      # Raw match videos
    ├── output_videos/     # Annotated output videos
    ├── models/            # Pre-trained YOLO weights (.pt)
    ├── config.yaml        # Favorite team setting
    ├── main.py            # Processing entrypoint
    ├── requirements.txt   # Dependencies
    ├── trackers/          # ByteTrack implementation
    ├── team_assigner/     # Jersey-color team assignment
    └── utils/             # I/O and logging helpers

## License
MIT License — see [LICENSE](LICENSE) for details.

## Author
**Aarohan Batra**
