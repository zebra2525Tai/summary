from transformers import pipeline

# 要約パイプラインの初期化
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text']