import os
from moviepy.editor import VideoFileClip

def extract_audio(video_folder, output_folder):
  """Extracts audio from all MP4 video files in a folder and saves them as MP3 files.

  Args:
    video_folder (str): Path to the folder containing the MP4 video files.
    output_folder (str): Path to the folder where the extracted MP3 files will be saved.
  """

  # Create the output folder if it doesn't exist
  os.makedirs(output_folder, exist_ok=True)

  for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
      video_path = os.path.join(video_folder, filename)
      audio_filename = os.path.splitext(filename)[0] + ".mp3"  # Extract filename without extension
      output_path = os.path.join(output_folder, audio_filename)

      try:
        # Extract audio using MoviePy
        clip = VideoFileClip(video_path)
        audio = clip.audio
        audio.write_audiofile(output_path)
        clip.close()  # Close clips to free resources
        print(f"Extracted audio from '{filename}' to '{output_path}'")
      except Exception as e:
        print(f"Error extracting audio from '{filename}': {e}")

# Example usage:
video_folder = "Vidio/"  # Replace with your video folder path
output_folder = "Audio"  # Replace with your desired output folder path for MP3s
extract_audio(video_folder, output_folder)
