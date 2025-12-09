"""Sentiment analysis using Watson NLP BERT Sentiment Analysis."""
import json
import os
import requests
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import (
    Features, SentimentOptions
)
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Load environment variables
load_dotenv()


def sentiment_analyzer(text_to_analyse):
    """Analyze sentiment using Watson NLP BERT model.
    
    This function sends a POST request to the Watson Embedded AI Libraries
    deployed on the Cloud IDE server. If unavailable, it falls back to
    IBM Watson NLU or VADER.
    
    Args:
        text_to_analyse: Text string to analyze
        
    Returns:
        JSON string with sentiment analysis results
    """
    # Try Watson Embedded AI Libraries (BERT) first
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        return response.text
    except (requests.exceptions.RequestException,
            requests.exceptions.Timeout) as e:
        print(f"Watson BERT service unavailable: {e}")
        # Fallback to IBM Watson NLU if configured
        return _watson_nlu_analyzer(text_to_analyse)


def _watson_nlu_analyzer(text_to_analyse):
    """Fallback sentiment analyzer using IBM Watson NLU (Cloud)."""
    # Get credentials from environment variables
    api_key = os.getenv('WATSON_NLU_API_KEY')
    service_url = os.getenv('WATSON_NLU_URL')
    
    if not api_key or not service_url:
        # Return error if Watson credentials not configured
        return json.dumps({
            'error': ('Watson NLU credentials not configured. '
                      'Please set WATSON_NLU_API_KEY and WATSON_NLU_URL '
                      'in .env file')
        })
    
    try:
        # Setup Watson NLU
        authenticator = IAMAuthenticator(api_key)
        nlu = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            authenticator=authenticator
        )
        nlu.set_service_url(service_url)
        
        # Analyze sentiment
        response = nlu.analyze(
            text=text_to_analyse,
            features=Features(sentiment=SentimentOptions())
        ).get_result()
        
        # Extract sentiment information
        sentiment = response.get('sentiment', {}).get('document', {})
        label = sentiment.get('label', 'neutral').upper()
        score = abs(sentiment.get('score', 0))
        
        # Format response
        result = {
            'label': f'SENT_{label}',
            'score': score,
            'sentiment': sentiment
        }
        
        return json.dumps(result)
        
    except Exception as e:
        # Return error if Watson API fails
        return json.dumps({
            'error': f'Watson NLU error: {str(e)}'
        })
