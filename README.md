# VoiceOps Sentinel 🛡️
**Real-Time Call Intelligence & Automated Transcription System**

VoiceOps Sentinel is an AI-driven pipeline designed to transform raw customer service audio into actionable business intelligence. It focuses on high-fidelity transcription, privacy compliance, and real-time sentiment analysis to improve support center efficiency.

🚀 **Project Status: Week 2 Complete** **Current Milestone:** Intelligence Layer (Sentiment & Summarization) implemented.

---

## 📊 Performance Metrics

| Metric | Result | Milestone |
| :--- | :--- | :--- |
| **ASR Accuracy** | 94.06% | Week 2 Validation |
| **Intelligence Latency** | 13.25s | Near Real-Time Goal |
| **Sentiment Logic** | VADER-based | Positive/Negative/Neutral |
| **Summarization** | BART-Large-CNN | Executive Summary Generation |

---

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **ASR Engine:** OpenAI Whisper
* **Intelligence Layer:** Hugging Face Transformers (BART), NLTK (VADER)
* **Signal Processing:** FFmpeg
* **Evaluation:** JiWER (Word Error Rate calculation)

---

## 📅 4-Week Implementation Roadmap

### Week 1: Transcription Pipeline (COMPLETED) ✅
* [x] Environment setup (Python, VS Code, FFmpeg).
* [x] Integration of Whisper "Small" model for robust ASR.
* [x] Implementation of WER/Accuracy validation script.
* [x] Hardware calibration for signal integrity.

### Week 2: Intelligence Layer (COMPLETED) ✅
* [x] Implementation of Sentiment Analysis (Happy/Angry/Neutral detection).
* [x] Development of automated Summarization using BART LLM workflows.
* [x] Latency optimization and testing for long-form technical discourse.
* [x] Achievement of >94% Accuracy on engineering-focused transcripts.

### Week 3: Diarization & Compliance 🔒 (UPCOMING)
* [ ] Integrate Pyannote for Speaker A/B labeling.
* [ ] Build PII Redaction system (scrubbing names, phones, and emails).
* [ ] Conduct privacy audit on mock call data.

### Week 4: Final Packaging 🎨
* [ ] Develop FastAPI backend for external requests.
* [ ] Build a minimal dashboard UI for side-by-side visualization.
* [ ] Final end-to-end system stress testing.