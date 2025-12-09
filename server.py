"""Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:8080.
"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
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
    
    # Extract label and score from response
    label = response['label']
    score = response['score']
    
    # Handle case when label or score is None (error case)
    if label is None:
        return "Error: Unable to analyze sentiment."
    
    # Format the output text
    # Remove 'SENT_' prefix from label for display
    sentiment_label = label.split('_')[1] if '_' in label else label
    return (f"The given text has been identified as {sentiment_label} "
            f"with a score of {score}.")


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
