# FastAPI Backend

from fastapi import FastAPI
from pydantic import BaseModel
import utils

app = FastAPI()

class CompanyRequest(BaseModel):
    company_name: str

@app.post("/analyze")
async def analyze(request: CompanyRequest):
    company_name = request.company_name
    articles = utils.fetch_news(company_name)
    processed_articles = []
    for article in articles:
        text = utils.extract_text(article["url"])
        summary = utils.summarize_text(text)
        sentiment = utils.analyze_sentiment(text)
        topics = utils.extract_topics(text)
        processed_articles.append({
            "title": article["title"],
            "summary": summary,
            "sentiment": sentiment,
            "topics": topics
        })

# Generate comparative analysis (simplified example)

    sentiment_dist = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for art in processed_articles:
        sentiment_dist[art["sentiment"]] += 1
    final_report = f"{company_name} has {sentiment_dist['Positive']} positive, {sentiment_dist['Negative']} negative articles."
    audio_path = utils.generate_hindi_tts(final_report)
    return {
        "company": company_name,
        "articles": processed_articles,
        "comparative_analysis": sentiment_dist,
        "audio_url": audio_path
    }