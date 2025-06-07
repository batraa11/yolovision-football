# Utils: Bounding Box & Video Helpers

A collection of utility functions for bounding box math, video processing, and general helpers.

## Installation

    pip install -r requirements.txt

## Modules

### bbox_utils.py

- `get_center_of_bbox(bbox: tuple[int, int, int, int]) -> tuple[int, int]`  
  Returns the (x, y) center of a bounding box `(x1, y1, x2, y2)`.

- `get_bbox_width(bbox: tuple[int, int, int, int]) -> int`  
  Returns the width of the bounding box.

### video_utils.py

- `read_video(path: str) -> Generator[np.ndarray]`  
  Reads video frames from a given file path.

- `write_video(frames: List[np.ndarray], output_path: str, fps: int)`  
  Writes a sequence of frames to a video file.

## Usage

    from utils.bbox_utils import get_center_of_bbox, get_bbox_width
    from utils.video_utils import read_video, write_video

    bbox = (10, 20, 110, 220)
    center = get_center_of_bbox(bbox)
    width = get_bbox_width(bbox)

## License

MIT License — see LICENSE for details.

## Author

**Aarohan Batra**
