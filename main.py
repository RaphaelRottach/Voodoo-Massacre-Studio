import sounddevice as sd
import numpy as np
import wave

# Audio Settings
SAMPLE_RATE = 44100  # Default sample rate
CHANNELS = 2  # Stereo input
DURATION = 10  # Recording duration in seconds

def list_devices():
    """List available audio devices"""
    print(sd.query_devices())

def record_audio(filename, sample_rate=SAMPLE_RATE, channels=CHANNELS, duration=DURATION):
    """Record audio from selected input device and save to a file"""
    print(f"Recording for {duration} seconds...")

    # Start recording
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    
    # Wait until recording is finished
    sd.wait()

    # Save audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    
    print(f"Recording saved to {filename}")

if __name__ == "__main__":
    # Step 1: List available devices
    print("Available audio devices:")
    list_devices()
    
    # Step 2: Record audio
    record_audio("test_recording.wav", sample_rate=44100, channels=2, duration=5)
