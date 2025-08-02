from transformers import pipeline

# 要約パイプラインの初期化
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        input_length = len(text)
        # 入力が長い場合はmax_lengthを大きくする
        max_len = min(300, int(input_length * 0.6))
        min_len = min(100, max_len - 1) if max_len > 100 else max_len // 2
        result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        if not result or not isinstance(result, list) or len(result) == 0 or 'summary_text' not in result[0]:
            return "要約できませんでした。"
        return result[0]['summary_text']
    except Exception as e:
        return f"要約エラー: {str(e)}"