import logging
import yaml
import cv2
import os
from datetime import datetime
from trackers.tracker import PlayerTracker

def list_files(folder, exts=None):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if exts:
        files = [f for f in files if any(f.lower().endswith(ext) for ext in exts)]
    return files

def prompt_selection(folder, prompt_text, exts=None):
    files = list_files(folder, exts)
    if not files:
        raise ValueError(f"No files found in {folder}")
    print(f"Available {prompt_text}:")
    for idx, f in enumerate(files):
        print(f"  [{idx+1}] {f}")
    while True:
        try:
            choice = int(input(f"Select {prompt_text} [1-{len(files)}]: "))
            if 1 <= choice <= len(files):
                return os.path.join(folder, files[choice-1]), files[choice-1]
        except Exception:
            pass
        print("Invalid selection. Try again.")

def load_config(config_path: str = "config.yaml") -> dict:
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def process_match_video(input_path: str, output_path: str, model_path: str, favorite_team: str) -> None:
    try:
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {input_path}")
        fps = cap.get(cv2.CAP_PROP_FPS)
        video_frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            video_frames.append(frame)
        cap.release()
        total_frames = len(video_frames)
        if total_frames == 0:
            raise ValueError("No frames found in video.")
        height, width = video_frames[0].shape[:2]
        tracker = PlayerTracker(model_path=model_path)
        tracks = tracker.get_object_tracks(video_frames)
        output_video_frames = tracker.draw_annotations(video_frames, tracks)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        for idx, frame in enumerate(output_video_frames):
            out.write(frame)
            if (idx + 1) % 100 == 0:
                progress = ((idx + 1) / total_frames) * 100
                print(f"Processing: {progress:.1f}% complete")
        out.release()
        print(f"Processing complete. Output saved to: {output_path}")
    except Exception as e:
        print(f"Error processing video: {e}")
        raise

def main():
    config = load_config()
    if not config:
        raise ValueError("Failed to load configuration")
    input_path, input_filename = prompt_selection('input_videos', 'input video', exts=['.mp4', '.avi', '.mov'])
    model_path, model_filename = prompt_selection('models', 'model', exts=['.pt', '.pth'])
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"output_videos/output_{now}_{os.path.splitext(model_filename)[0]}_{os.path.splitext(input_filename)[0]}.avi"
    print(f"Kickoff! Processing {input_filename} with model {model_filename}!")
    process_match_video(
        input_path=input_path,
        output_path=output_filename,
        model_path=model_path,
        favorite_team=config["favorite_team"]
    )

if __name__ == "__main__":
    main()