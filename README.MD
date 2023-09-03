# YouTube Video Downloader

`download.py` - this Python script allows you to easily download YouTube videos as mp4 files with optional mp3 audio extraction. It utilizes the `yt_dlp` library, which is a more up-to-date and actively maintained fork of the popular `youtube-dl` library.

## Prerequisites

Before you can use this script, you need to have Python and the `yt_dlp` library installed on your system. You can install `yt_dlp` using pip:

```bash
pip install yt-dlp
```

## Usage

1. Copy the YouTube video URL that you want to download.
2. Modify the script by setting the `video_url` variable to the URL of the video you want to download.
3. Set the `output_directory` variable to the directory where you want to save the downloaded video.

```python
video_url = 'https://www.youtube.com/watch?v=xF_CJUadatY'
output_directory = 'audio'
download_video(video_url, output_directory)
```

4. Run the script using Python:

```bash
python your_script_name.py
```

## Options

The script uses `yt_dlp` options to specify the download format and audio extraction settings. You can customize these options in the `ydl_opts` dictionary:

- `'format'`: You can specify the desired video and audio format using yt-dlp format specifiers. The default format is `'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'`, which attempts to download the best available video and audio streams.

- `'outtmpl'`: This option determines the filename and location of the downloaded video. By default, it is set to `output_dir + '/%(title)s.%(ext)s'`, which saves the video in the specified output directory with the video's title as the filename and the appropriate extension.

- `'postprocessors'`: This option specifies post-processing steps, such as audio extraction. In the default configuration, it extracts audio as an mp3 file with a bitrate of 192 kbps.

You can find more information about `yt_dlp` options in the [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp/blob/master/README.md).


# Google Speech Recognition

`googlesr.py` - this Python script demonstrates how to use the Google Speech Recognition API to transcribe audio from a file. It uses the `speech_recognition` library to perform the transcription.

## Prerequisites

Before running the script, you need to ensure that you have the required Python library installed. You can install it using `pip`:

```bash
pip install SpeechRecognition
```

## Usage

1. Save the audio file you want to transcribe to the same directory as this script. In this example, the file is named `swartz.wav`, but you can replace it with your audio file.

2. Open the script in your preferred Python development environment or text editor.

3. Run the script. It will attempt to transcribe the audio and print the recognized text to the console.

## Script Explanation

- `import speech_recognition as sr`: This line imports the `speech_recognition` library, which provides the functionality for speech recognition.

- `r = sr.Recognizer()`: Creates a recognizer object from the `speech_recognition` library.

- `file_path = "swartz.wav"`: Specifies the path to the audio file you want to transcribe. Replace `"swartz.wav"` with the path to your audio file.

- `with sr.AudioFile(file_path) as source`: Opens the audio file using the `AudioFile` context manager from the recognizer.

- `audio = r.record(source)`: Records the audio from the source file.

- The `try` block attempts to recognize the audio using Google's speech recognition service and prints the result if successful.

  - `text = r.recognize_google(audio)`: Uses Google's speech recognition to transcribe the audio.

  - `print("You said:", text)`: Prints the recognized text to the console.

- The `except` blocks handle potential errors:

  - `sr.UnknownValueError`: If the recognizer couldn't understand the audio, it prints "Could not understand audio."

  - `sr.RequestError as e`: If there was an issue with the request to Google's speech recognition service, it prints an error message containing the specific issue.

## Note

Ensure that you have an internet connection while running the script because it relies on Google's speech recognition service to transcribe the audio.

Feel free to replace `"swartz.wav"` with the path to your own audio file, and the script should transcribe it using Google's speech recognition service.


# Speech Recognition using PocketSphinx

`pocketsphinx_sr.py` - this Python script converts a WAV audio file to raw 16-bit PCM format and performs speech recognition on it using the PocketSphinx speech recognition system. The recognized text is then printed to the console. Additionally, temporary files generated during the process are cleaned up.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed on your system:

1. **FFmpeg**: FFmpeg is used to convert the input WAV file to raw PCM format. You can download FFmpeg from [ffmpeg.org](https://www.ffmpeg.org/download.html) or install it via package manager (e.g., `apt` or `brew`).

2. **PocketSphinx**: PocketSphinx is a lightweight speech recognition engine. You can install it using the following command:

   ```
   pip install pocketsphinx
   ```

## Usage

1. **Input WAV File**: Place the WAV audio file that you want to transcribe in the same directory as this script. Update the `wav_file` variable in the script to specify the name of your WAV file.

   ```python
   wav_file = 'your_audio.wav'
   ```

2. **Language Model Files**: Ensure you have the necessary language model files for your desired language and acoustic model (HMM) in the same directory as the script. Update the following variables accordingly:

   - `hmm`: The name of the folder containing the Hidden Markov Model files.
   - `dict_file`: The path to the pronunciation dictionary file.
   - `lm`: The path to the language model binary file.
   - `config`: The path to the PocketSphinx configuration file.

3. **Run the Script**: Open your terminal or command prompt and navigate to the directory containing the script. Run the script using the following command:

   ```
   python speech_recognition.py
   ```

4. **View Recognized Text**: After running the script, the recognized text will be printed to the console.

## Cleanup

The script will automatically clean up temporary files generated during the process, including the raw PCM file and the output text file.

## Additional Information

- For more information on PocketSphinx and its configuration, refer to the [PocketSphinx documentation](https://cmusphinx.github.io/wiki/).

- This script assumes that the input WAV file is single-channel (mono) and has a sample rate of 16,000 Hz. Adjust the parameters in the FFmpeg command accordingly if your input file has different characteristics.

- Make sure you have proper permissions to run external commands and read/write files in the script's directory.

- Customize the script as needed for your specific use case, such as handling different audio file formats or configuring PocketSphinx for different languages.

# Speech Recognition Script

`whisper_sr.py` - this script utilizes the Whisper ASR (Automatic Speech Recognition) library to transcribe audio from a given file. It supports multiple models for speech recognition, including tiny, base, small, medium, and large.

## Requirements

Before running the script, make sure you have the following prerequisites installed:

- Python (3.6 or higher)
- Whisper library (`pip install whisper`)

## Usage

To use this script, follow these steps:

1. Clone or download this repository to your local machine.

2. Ensure you have Python and the Whisper library installed.

   ```bash
   pip install whisper
   ```

3. Place the audio file you want to transcribe in the same directory as the script or specify the path to the audio file in the `audio_file` variable.

4. Open a terminal and navigate to the directory containing the script.

5. Run the script with the desired model as an argument. If no model is specified, it will default to the "base" model.

6. The script will transcribe the audio and display the transcribed text on the terminal.

## Available Models

You can choose from the following pre-trained models for speech recognition:

- `tiny`: A small and fast model with lower accuracy.
- `base`: A balanced model offering a good trade-off between speed and accuracy (default).
- `small`: A slightly larger model with improved accuracy.
- `medium`: A larger model with higher accuracy but slower performance.
- `large`: The largest model with the highest accuracy but the slowest performance.

## License

All scripts is provided under the MIT License. Feel free to modify and distribute it as needed.