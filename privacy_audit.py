import spacy

# Load the NLP model for PII detection
nlp = spacy.load("en_core_web_sm")

def run_privacy_audit(segments):
    print("--- Week 3: Privacy Audit Verification ---")
    print("Testing Focus: 100% Redaction Accuracy\n")

    for seg in segments:
        text = seg["text"]
        doc = nlp(text)
        
        redacted_text = text
        # Logic to find Names (PERSON) and Locations (GPE)
        for ent in doc.ents:
            if ent.label_ in ["PERSON", "GPE", "ORG"]:
                redacted_text = redacted_text.replace(ent.text, f"[{ent.label_}_REDACTED]")
        
        print(f"TIME SLOT: {seg['time']}")
        print(f"ORIGINAL : {text}")
        print(f"REDACTED : {redacted_text}")
        print("-" * 40)

# MOCK DATA: Using your real timestamps from your previous success!
test_segments = [
    {
        "time": "21.48s - 25.26s", 
        "text": "Hello, my name is Nayana Yaranal and I am calling from Bengaluru."
    },
    {
        "time": "32.19s - 34.03s", 
        "text": "My office is at Infotact Solutions and my phone number is 9876543210."
    }
]

if __name__ == "__main__":
    run_privacy_audit(test_segments)