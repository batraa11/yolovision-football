# PlayerTracker Module

A utility module for detecting and tracking football players, referees, and the ball in video frames using YOLOv11l and ByteTrack.

## Installation

    pip install -r requirements.txt

## Usage

    from trackers import PlayerTracker

    # Initialize tracker
    tracker = PlayerTracker(model_path="models/best.pt", confidence_threshold=0.1)

    # Load video frames
    frames = load_your_video_frames()

    # Get object tracks
    tracks = tracker.get_object_tracks(frames)

    # Draw annotations
    annotated_frames = tracker.draw_annotations(frames, tracks)

## API Reference

### PlayerTracker(model_path, confidence_threshold=0.1, batch_size=20)
- **model_path** (str): Path to YOLOv11l `.pt` file  
- **confidence_threshold** (float): Minimum confidence for detections  
- **batch_size** (int): Number of frames per inference batch  

### detect_frames(frames: list[np.ndarray]) -> list
Runs batched inference and returns raw detection results.

### get_object_tracks(frames: list[np.ndarray]) -> dict
Returns a dict with keys `"players"`, `"referees"`, and `"ball"` mapping to lists of track dicts.

### draw_ellipse(frame, bbox, color, track_id=None) -> np.ndarray
Draws an ellipse under a tracked object with optional ID label.

### draw_triangle(frame, bbox, color) -> np.ndarray
Draws a triangle marking the ball.

### draw_annotations(video_frames, tracks) -> list[np.ndarray]
Applies ellipse/triangle annotations to each frame.

## Project Structure

    trackers/
    ├── __init__.py
    └── tracker.py

## License

MIT License — see LICENSE for details.

## Author

**Aarohan Batra**
