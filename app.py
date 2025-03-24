# Gradio Frontend

import gradio as gr
import requests

def analyze_company(company_name):
    response = requests.post(
        "http://localhost:8000/analyze",
        json={"company_name": company_name}
    )
    if response.status_code == 200:
        result = response.json()
        articles_output = "\n\n".join([
            f"**Title**: {art['title']}\n**Summary**: {art['summary']}\n**Sentiment**: {art['sentiment']}\n**Topics**: {', '.join(art['topics'])}"
            for art in result["articles"]
        ])
        return f"{articles_output}\n\n**Final Report**: {result['comparative_analysis']}\n**Audio**: {result['audio_url']}"
    else:
        return "Error!"

iface = gr.Interface(
    fn=analyze_company,
    inputs=gr.Textbox(label="Company Name"),
    outputs=gr.Markdown(),
    title="News Analyzer"
)

if __name__ == "__main__":
    iface.launch()