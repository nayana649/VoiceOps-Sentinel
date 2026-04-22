import whisper
import os
from jiwer import wer

class VoiceProcessor:
    def __init__(self):
        print("Loading AI Model... Please wait.")
        self.model = whisper.load_model("small") 
    def transcribe_file(self, audio_path):
        if not os.path.exists(audio_path):
            return None
        print(f"Transcribing: {audio_path}")
        # Task 1.1: Handling different input formats is built into Whisper
        result = self.model.transcribe(audio_path)
        return result["text"]

# --- Week 1 Deliverable: WER Check ---
if __name__ == "__main__":
    processor = VoiceProcessor()
    
    # 1. Provide the "Ground Truth" (Exactly what you said in the audio)
    ground_truth = "Python is the Powerful language in Engineering."
    
    # 2. Run the transcription on your test file
    audio_file = "my_voice.m4a" # Ensure this file is in your folder!
    hypothesis = processor.transcribe_file(audio_file)
    
    if hypothesis:
        print(f"\nAI Output: {hypothesis}")
        
        # 3. Calculate Error Rate
        error_rate = wer(ground_truth.lower(), hypothesis.lower())
        accuracy = (1 - error_rate) * 100
        
        print(f"--- Week 1 Results ---")
        print(f"Word Error Rate: {error_rate:.2%}")
        print(f"System Accuracy: {accuracy:.2f}%")
    else:
        print("Error: Could not find test.wav. Please record a sample!")