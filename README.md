# News Summarization & Text-to-Speech Application

A Python web application that collects company-related news, summarizes articles, performs sentiment analysis, compares article signals, and generates a Hindi text-to-speech report.

## Overview

```text
Company name
     ↓
 GNews API
     ↓
News articles
  ↙     ↓      ↘
Summary Sentiment Topics
  \      |      /
   Comparative analysis
          ↓
     Hindi TTS report
```

## Features

- **News extraction:** Fetches company-related articles through the GNews API
- **Summarization:** Uses `facebook/bart-large-cnn` for concise summaries
- **Sentiment analysis:** Classifies articles as Positive, Negative, or Neutral
- **Comparative analysis:** Compares sentiment distribution and topic overlap
- **Hindi TTS:** Generates a Hindi spoken report using `facebook/mms-tts-hin`
- **Web interface:** Gradio frontend backed by a FastAPI service
- **Deployment:** Docker-based deployment support for Hugging Face Spaces

## Technology Stack

- **Language:** Python 3.9+
- **API:** FastAPI
- **UI:** Gradio
- **NLP:** Hugging Face Transformers
- **Models:** BART, DistilBERT, MMS TTS
- **Data/ML:** Python data-processing workflow
- **Deployment:** Docker / Hugging Face Spaces

## Project Structure

```text
├── app.py               # Gradio frontend
├── api.py               # FastAPI routes
├── utils.py             # Data fetching and model helpers
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
└── README.md
```

## Run Locally

```bash
git clone https://github.com/Harsh24-j/News-Summarization-and-Text-to-Speech-Application.git
cd News-Summarization-and-Text-to-Speech-Application
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn api:app --reload
```

Start the frontend in another terminal:

```bash
python app.py
```

- API: `http://localhost:8000`
- Gradio UI: `http://localhost:7860`

## API

### `POST /analyze`

Example request:

```json
{
  "company_name": "BMW"
}
```

The service returns article summaries, sentiment information, comparative analysis, and an audio output reference.

## Limitations

- News availability depends on the GNews API and its rate limits.
- Source articles are English-language inputs in the documented workflow.
- Hindi TTS quality depends on the underlying translation/TTS models.
- Real-world article availability and model output can vary by run.

## License

MIT License. See `LICENSE` for details.

## Author

**Harsh Shrivastava**  
[GitHub](https://github.com/Harsh24-j) · [LinkedIn](https://linkedin.com/in/harshshrivastava24)
