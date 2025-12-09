"""Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:8080.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Load environment variables from .env file
load_dotenv()

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """This code receives the text from the HTML interface and
    runs sentiment analysis over it using sentiment_analysis()
    function. The output returned shows the label and its confidence
    score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    return jsonify(response)


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
