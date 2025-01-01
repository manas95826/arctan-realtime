# Real-Time Noise Cancellation System

This repository contains a Python implementation of a real-time noise cancellation system. The system filters out unwanted background noise from a live audio stream (microphone input) and outputs clean audio in real-time. The processed audio is also saved as a `.wav` file.

## Features
- **Real-Time Processing**: Processes live audio with a latency of less than 100 ms for each 200 ms chunk.
- **Noise Reduction**: Reduces background noise while preserving the clarity of the target speaker(s).
- **Output as File**: Saves the processed (cleaned) audio to a `.wav` file for later use.
- **Scalable for Single and Multiple Speakers**: Works well in both single-speaker and multi-speaker scenarios.

## Technologies Used
- **Python**: Core programming language.
- **Libraries**:
  - `pyaudio`: For capturing live audio from the microphone.
  - `numpy`: For efficient numerical operations.
  - `noisereduce`: For noise reduction using spectral gating.
  - `wave`: For saving processed audio to `.wav` files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manas95826/arctan-realtime.git
   cd arctan-realtime
   ```

2. Install the required dependencies:
   ```bash
   pip install pyaudio numpy noisereduce wave
   ```

   **Note**: On some systems, you may need to install `portaudio` for `pyaudio`:
   ```bash
   sudo apt-get install portaudio19-dev  # For Ubuntu/Debian
   ```

3. Ensure your microphone is connected and accessible.

## Usage

1. Run the script to start real-time noise cancellation:
   ```bash
   python realtime_noise_cancellation.py
   ```

2. The script will process the audio in real-time and save the cleaned audio to a file named `cleaned_audio.wav`.

3. To stop the program, press `Ctrl+C`. The processed audio will automatically be saved before the program exits.

## File Structure
- `realtime_noise_cancellation.py`: Main script for real-time noise cancellation.
- `README.md`: Documentation for the project.

## How It Works

1. **Audio Input**: Captures live audio in chunks from the microphone using `pyaudio`.
2. **Noise Reduction**: Applies noise reduction to each chunk using the `noisereduce` library.
3. **Real-Time Output**: Outputs the processed audio stream in real-time.
4. **File Saving**: Saves the processed audio into a `.wav` file when the program stops.

## Example Output

The output is a `.wav` file named `cleaned_audio.wav` that contains the processed audio with significantly reduced background noise.

## Future Enhancements
- Add support for advanced noise reduction algorithms like neural network-based models.
- Implement support for stereo audio processing.
- Integrate a GUI for easier user interaction.
