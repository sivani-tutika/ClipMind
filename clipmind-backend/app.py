from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.transcript import fetch_transcript
from summarize import generate_summary


app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    
    data = request.get_json()
    url = data.get('url')
    print("Data", data)
    if not url:
        return jsonify({"error", "Missing video URL"}), 400
    try:
        transcript = fetch_transcript(url)
        summary = generate_summary(transcript)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True)
    
