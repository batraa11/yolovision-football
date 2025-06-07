# Football Analysis System

A minimal, robust football match video analysis system using YOLOv11l for detection and ByteTrack for tracking. It processes match footage to detect and track players, referees, and the ball, and outputs annotated video files.

## Features
- ⚽ Player, referee, and ball detection via YOLOv11l
- 🎯 Object tracking using ByteTrack
- 🔧 Configurable favorite team overlay (see `config.yaml`)
- 🖥️ Simple CLI interface

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
Follow prompts to select your input video (in `input_videos/`) and YOLO model (in `models/`). Outputs are saved to `output_videos/`.

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
