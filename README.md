VoiceOps Sentinel 🛡️

Real-Time Call Intelligence & Automated Transcription System

VoiceOps Sentinel is an AI-driven pipeline designed to transform raw customer service audio into actionable business intelligence. It focuses on high-fidelity transcription, privacy compliance, and real-time sentiment analysis to improve support center efficiency.

🚀 Project Status: Week 3 Complete Current Milestone: Diarization & Compliance (Speaker ID & PII Redaction) implemented.

📊 Performance Metrics

Metric                                            Result                              Milestone

ASR Accuracy                                      94.06%                           Week 2 Validation
Speaker ID Accuracy                               ~98%                             Week 3 Diarization
PII Redaction                                     100%                             Name/Location Masking
Intelligence Latency                              13.25s                           Near Real-Time Goal

🛠️ Technical Stack
Language: Python 3.10+

ASR Engine: OpenAI Whisper

Diarization: Pyannote Audio 3.1

Intelligence Layer: Hugging Face Transformers (BART), NLTK (VADER)

Signal Processing: FFmpeg, Librosa

Evaluation: JiWER & Privacy Audit Logs

📅 4-Week Implementation Roadmap
Week 1: Transcription Pipeline ✅
[x] Environment setup (Python, VS Code, FFmpeg).

[x] Integration of Whisper "Small" model for robust ASR.

[x] Implementation of WER/Accuracy validation script.

Week 2: Intelligence Layer ✅
[x] Implementation of Sentiment Analysis (Happy/Angry/Neutral detection).

[x] Development of automated Summarization using BART LLM.

[x] Achievement of >94% Accuracy on engineering-focused transcripts.

Week 3: Diarization & Compliance 🔒 ✅
[x] Integrated Pyannote for Speaker A/B labeling and timestamps.

[x] Built PII Redaction system (scrubbing names and locations).

[x] Conducted privacy audit to ensure 100% compliance on mock data.

[x] Secured repository by removing hardcoded API tokens.

Week 4: Final Packaging 🎨 (UPCOMING)
[ ] Develop FastAPI backend for external requests.

[ ] Build a minimal dashboard UI for side-by-side visualization.

[ ] Final end-to-end system stress testing.
