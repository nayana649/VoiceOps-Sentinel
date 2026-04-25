import os
import sys

# --- STEP 1: THE MUFFLER ---
class Silence:
    def __enter__(self):
        self._original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self._original_stderr

# --- STEP 2: SILENCED IMPORTS ---
with Silence():
    import torch
    import warnings
    import librosa
    from pyannote.audio import Pipeline
    from pydub import AudioSegment

# --- STEP 3: ENVIRONMENT SETUP ---
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["PYTHONWARNINGS"] = "ignore"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
warnings.filterwarnings("ignore")

def run_diarization():
    # UPDATED: Changed token to True for GitHub Security Compliance
    # This works because you are already logged in locally via huggingface-cli
    HF_TOKEN = True 
    
    input_file = "python_test.m4a"
    wav_file = "python_test.wav"

    print("--- 1. Converting Audio ---")
    try:
        audio = AudioSegment.from_file(input_file, format="m4a")
        audio.export(wav_file, format="wav")
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {e}")
        return

    print("--- 2. Loading Diarization Model ---")
    try:
        # Pipeline now uses the local cache/login
        pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", token=HF_TOKEN)
        pipeline.to(torch.device("cpu"))
    except Exception as e:
        print(f"Model Load Error: {e}")
        return

    print("--- 3. Analyzing Audio ---")
    try:
        y, sr = librosa.load(wav_file, sr=16000)
        audio_tensor = torch.from_numpy(y).float().unsqueeze(0)
        
        output = pipeline({"waveform": audio_tensor, "sample_rate": sr})

        print("\n--- 4. Speaker Timeline (Success!) ---")
        
        if hasattr(output, 'speaker_diarization'):
            results = output.speaker_diarization
        else:
            results = getattr(output, 'annotation', output)

        found = False
        for segment, track, speaker in results.itertracks(yield_label=True):
            print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {speaker}")
            found = True

        if not found:
            print("No speech detected. Check your audio file!")

    except Exception as e:
        print(f"Final Analysis Error: {e}")

if __name__ == "__main__":
    run_diarization()