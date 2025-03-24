# News Summarization and Text-to-Speech Application

[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deployed on Hugging Face](https://img.shields.io/badge/Deployed%20on-Hugging%20Face%20Spaces-blue)](https://huggingface.co/spaces)

A web application that extracts news articles for a given company, performs summarization, sentiment analysis, and generates a Hindi text-to-speech (TTS) report. Built with **FastAPI**, **Gradio**, and Hugging Face models.

---

## 🚀 Features
- **News Extraction**: Fetches 10+ news articles using the GNews API.
- **Summarization**: Generates concise summaries using `facebook/bart-large-cnn`.
- **Sentiment Analysis**: Classifies articles as Positive/Negative/Neutral with `distilbert-base-uncased`.
- **Comparative Analysis**: Compares sentiment distribution and topic overlap across articles.
- **Hindi TTS**: Converts the final report to Hindi speech using `facebook/mms-tts-hin`.
- **Deployment**: Ready for deployment on Hugging Face Spaces via Docker.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/news-summarizer-tts.git
   cd news-summarizer-tts# News-Summarization-and-Text-to-Speech-Application

## Install dependencies:
   pip install -r requirements.txt
   
   ## Run Locally
   1. Start the FastAPI backend:
      uvicorn api:app --reload
      The API will run at http://localhost:8000.
    2.Start the Gradio frontend:
      python app.py
      Access the UI at http://localhost:7860
    3. Input a company name (e.g., "Tesla") and click Submit to:
       -> Fetch news articles.
       -> View summaries, sentiment scores, and topics.
       -> Play the Hindi TTS report.

## Deployment on Hugging Face Spaces
   Create a new Space on Hugging Face with Docker SDK.

   Upload all project files (including Dockerfile and requirements.txt).

   Build and deploy:

   Hugging Face automatically builds the Docker image using the provided Dockerfile.

   The app will be accessible at https://huggingface.co/spaces/{your-username}/{space-name}.

## Project Structure
   ├── app.py               # Gradio frontend
   ├── api.py               # FastAPI backend routes
   ├── utils.py             # Helper functions (scraping, models)
   ├── requirements.txt     # Dependencies (FastAPI, Gradio, transformers)
   ├── Dockerfile           # Deployment configuration
   └── README.md

## API Documentation
   Endpoint: /analyze
   Method: POST

  Input:
  { "company_name": "BMW" }

  Output:
  {
    "company": "BMW",
    "articles": [{"title": "...", "summary": "...", "sentiment": "Positive", "topics": [...]}],
    "comparative_analysis": {"Positive": 6, "Negative": 2, "Neutral": 2},
    "audio_url": "output.mp3"
  }

## Assumptions & Limitations

   News Source: Relies on GNews API (English articles only; free tier has rate limits).

   Language: TTS output is in Hindi; translation quality depends on Helsinki-NLP/opus-mt-en-hi.

   Edge Cases: Limited error handling for invalid URLs or missing articles.

## License
   This project is licensed under the MIT License. See LICENSE for details.
