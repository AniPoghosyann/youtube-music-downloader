from pytube import YouTube
import tempfile
import os
import sys



#define a function to download audio from YouTube
def download_audio(youtube_url, save_path=None):
    """
    Downloads audio from the given YouTube video URL.

    Args:
        youtube_url (str): the link to the YouTube video.
        save_path (str, optional): Directory to save the audio file. If None, uses a temporary directory.

    """

    try:

        #creating a YouTube object
        yt = YouTube(youtube_url)
        #getting audio-only stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        #check if the audio stream was found
        if not audio_stream:
            print("No audio stream found.")
            return None

        #determine where to save the path
        if save_path is None:
            # Create a temporary directory if none specified
            target_dir = tempfile.mkdtemp()
        else:
            os.makedirs(save_path, exist_ok=True)
            target_dir = save_path

        print(f"Downloading audio from: {yt.title}")

        #Download file to the chosen directory
        download_path = audio_stream.download(output_path=target_dir)
        print(f"Audio successfully downloaded to: {download_path}")
        return download_path

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter Youtube video URL: ")
    download_audio(url)
