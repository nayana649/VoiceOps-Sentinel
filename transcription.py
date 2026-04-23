import whisper
import os
import nltk
import time
import torch
from jiwer import wer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Download the required dictionary for sentiment
nltk.download('vader_lexicon', quiet=True)

class VoiceProcessor:
    def __init__(self):
        print("--- Initializing VoiceOps Sentinel (Manual Mode) ---")
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Running on: {self.device}")
        
        # 1. Whisper Setup
        print("Loading Whisper Model...")
        self.model = whisper.load_model("medium") 
        
        # 2. Sentiment Setup
        self.sia = SentimentIntensityAnalyzer()
        
        # 3. Manual BART Setup
        print("Loading BART Intelligence (Direct Load)...")
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.bart_model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def transcribe_file(self, audio_path):
        if not os.path.exists(audio_path):
            return None
        result = self.model.transcribe(audio_path)
        return result["text"]

    def run_intelligence(self, text):
        # 1. Sentiment
        scores = self.sia.polarity_scores(text)
        if scores['compound'] >= 0.05: sentiment = "Positive 😊"
        elif scores['compound'] <= -0.05: sentiment = "Negative 😡"
        else: sentiment = "Neutral 😐"

        # 2. Manual Summarization
        # Threshold set to 20 words to ensure short tests don't trigger heavy LLM load
        if len(text.split()) > 20:
            inputs = self.tokenizer([text], max_length=1024, return_tensors="pt", truncation=True).to(self.device)
            summary_ids = self.bart_model.generate(inputs["input_ids"], num_beams=4, max_length=50, min_length=10)
            summary = self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        else:
            summary = "Transcript too short for summary."

        return sentiment, summary

if __name__ == "__main__":
    processor = VoiceProcessor()
    
    # --- UPDATED GROUND TRUTH FOR WEEK 2 LONG-FORM TEST ---
    ground_truth = (
        "Hello, Good Afternoon to all."
        "Python has become the backbone of modern engineering and artificial intelligence. "
        "In my current work with VoiceOps Sentinel, I am utilizing Python’s extensive library "
        "ecosystem to bridge the gap between raw hardware signals and high-level data intelligence. "
        "By using libraries like Whisper for speech-to-text and Transformers for natural language "
        "understanding, we can automate the analysis of complex communication. Python's versatility "
        "allows us to handle everything from low-level signal processing in electronics to high-level "
        "automation in cloud environments. This specific test is designed to measure how effectively "
        "our intelligence layer can condense technical discussions into actionable executive summaries."
    )
    
    audio_file = "python_test.m4a" 
    
    hypothesis = processor.transcribe_file(audio_file)
    
    if hypothesis:
        print(f"\nAI Transcript: {hypothesis}")
        
        # WER Check (Week 1 requirement carried over)
        error_rate = wer(ground_truth.lower(), hypothesis.lower())
        print(f"Accuracy: {(1 - error_rate) * 100:.2f}%")
        
        # Intelligence Report (Week 2 primary task)
        print("\nRunning Intelligence Layer...")
        t1 = time.time()
        sentiment, summary = processor.run_intelligence(hypothesis)
        latency = time.time() - t1

        print(f"--- Week 2 Report ---")
        print(f"Sentiment: {sentiment}")
        print(f"Summary: {summary}")
        print(f"Latency: {latency:.2f}s")
    else:
        print(f"Error: Could not find {audio_file}. Please check the filename and path.")