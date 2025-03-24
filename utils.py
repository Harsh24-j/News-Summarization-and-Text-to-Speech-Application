# Fetch News URLs (GNews API)

from gnews import GNews

def fetch_news(company_name: str, max_articles=10):
    google_news = GNews(language='en', period='7d', max_results=max_articles)
    articles = google_news.get_news(f"{company_name} company news")
    return [{"title": a["title"], "url": a["url"]} for a in articles]

# Scrape Article Content

from newspaper import Article

def extract_text(url: str):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# Summarization & Sentiment Analysis

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def summarize_text(text: str):
    return summarizer(text, max_length=150, do_sample=False)[0]["summary_text"]

def analyze_sentiment(text: str):
    result = sentiment_analyzer(text)[0]
    if result["label"] == "POSITIVE" and result["score"] > 0.6:
        return "Positive"
    elif result["label"] == "NEGATIVE" and result["score"] > 0.6:
        return "Negative"
    else:
        return "Neutral"

# Topic Extraction (YAKE)

import yake

def extract_topics(text: str, top_n=5):
    kw_extractor = yake.KeywordExtractor(top=top_n)
    keywords = kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords]

# Translation & Hindi TTS

from transformers import pipeline
import soundfile as sf

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
tts = pipeline("text-to-speech", model="facebook/mms-tts-hin")

def generate_hindi_tts(text: str, output_file="output.mp3"):
    translated = translator(text)[0]["translation_text"]
    speech = tts(translated)
    sf.write(output_file, speech["audio"], speech["sampling_rate"])
    return output_file