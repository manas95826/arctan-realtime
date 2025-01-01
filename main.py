# Import required libraries for audio processing and noise reduction
import pyaudio
import numpy as np
import noisereduce as nr
import wave
import threading

class AudioProcessor:
    """
    A class to handle real-time audio processing with noise reduction capabilities.
    Captures audio input, processes it to reduce noise, and saves to a WAV file.
    """
    # Default audio parameters
    CHANNELS = 1          # Mono audio
    FORMAT = pyaudio.paInt16  # 16-bit audio format
    RATE = 16000         # Sample rate in Hz
    CHUNK_SIZE = 1024    # Number of frames per buffer
    
    def __init__(self, output_filename="cleaned_audio.wav"):
        """
        Initialize the AudioProcessor with output file configuration and audio setup.
        Args:
            output_filename (str): Name of the output WAV file
        """
        self.output_filename = output_filename
        self.frames = []  # Store processed audio frames
        self.pyaudio = pyaudio.PyAudio()
        self.stream = None
        self.initialize_stream()

    def initialize_stream(self):
        """
        Set up the audio input stream with specified parameters.
        """
        self.stream = self.pyaudio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK_SIZE
        )

    def process_audio(self, chunk_data):
        """
        Process a chunk of audio data to reduce noise.
        Args:
            chunk_data (bytes): Raw audio data
        Returns:
            bytes: Processed audio data with reduced noise
        """
        audio_data = np.frombuffer(chunk_data, dtype=np.int16)
        reduced_noise_data = nr.reduce_noise(y=audio_data, sr=self.RATE)
        return reduced_noise_data.astype(np.int16).tobytes()

    def save_audio_to_file(self):
        """
        Save the processed audio frames to a WAV file.
        """
        if self.frames:
            with wave.open(self.output_filename, 'wb') as wf:
                wf.setnchannels(self.CHANNELS)
                wf.setsampwidth(self.pyaudio.get_sample_size(self.FORMAT))
                wf.setframerate(self.RATE)
                wf.writeframes(b''.join(self.frames))
            print(f"Processed audio saved to {self.output_filename}")

    def capture_and_process_audio(self):
        """
        Main loop for capturing and processing audio in real-time.
        Runs until interrupted by Ctrl+C.
        """
        try:
            print("Real-time noise cancellation is running... Press Ctrl+C to stop.")
            while True:
                # Read audio chunk and handle buffer overflow
                chunk_data = self.stream.read(self.CHUNK_SIZE, exception_on_overflow=False)
                # Process the chunk and store it
                reduced_chunk = self.process_audio(chunk_data)
                self.frames.append(reduced_chunk)
        except KeyboardInterrupt:
            print("\nStopping real-time audio processing.")
            self.save_audio_to_file()
            self.cleanup()

    def cleanup(self):
        """
        Clean up audio resources and close streams.
        """
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()
        print("Audio resources released.")

def main():
    """
    Entry point of the program.
    Creates an AudioProcessor instance and starts audio processing.
    """
    processor = AudioProcessor()
    processor.capture_and_process_audio()

if __name__ == "__main__":
    main()

