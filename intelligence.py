import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Download the sentiment dictionary (only happens once)
nltk.download('vader_lexicon')

class VoiceIntelligence:
    def __init__(self):
        print("--- Initializing Intelligence Layer ---")
        # Initialize Sentiment Analyzer (VADER)
        self.sia = SentimentIntensityAnalyzer()
        
        # Initialize Summarizer (BART model)
        # Note: This will download about 1.5GB the first time you run it!
        print("Loading Summarization Model... please wait.")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def analyze_text(self, text):
        # 1. Sentiment Analysis
        scores = self.sia.polarity_scores(text)
        if scores['compound'] >= 0.05:
            mood = "Positive 😊"
        elif scores['compound'] <= -0.05:
            mood = "Negative 😡"
        else:
            mood = "Neutral 😐"

        # 2. Summarization
        # We only summarize if the text is long enough to make sense
        if len(text.split()) > 25:
            summary_output = self.summarizer(text, max_length=50, min_length=10, do_sample=False)
            summary = summary_output[0]['summary_text']
        else:
            summary = "Call too short for a meaningful summary."

        return mood, summary