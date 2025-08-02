from flask import Flask, render_template, request, jsonify
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'テキストがありません'}), 400
    summary = summarize_text(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)