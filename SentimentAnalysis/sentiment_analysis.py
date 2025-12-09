"""Sentiment analysis using IBM Watson Natural Language Understanding."""
import os
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import (
    Features, SentimentOptions
)
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException

# Load environment variables
load_dotenv()


def sentiment_analyzer(text_to_analyse):
    """Analyze sentiment using IBM Watson NLU.

    Args:
        text_to_analyse: Text string to analyze

    Returns:
        Dictionary with 'label' and 'score' keys.
        Returns None for both if analysis fails.
    """
    # Get credentials from environment variables
    api_key = os.getenv('WATSON_NLU_API_KEY')
    service_url = os.getenv('WATSON_NLU_URL')

    if not api_key or not service_url:
        # Return error if Watson credentials not configured
        return {
            'label': None,
            'score': None
        }

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
        label = sentiment.get('label', 'neutral')
        score = sentiment.get('score', 0)

        # Format label to match expected format (SENT_POSITIVE, etc.)
        label_map = {
            'positive': 'SENT_POSITIVE',
            'negative': 'SENT_NEGATIVE',
            'neutral': 'SENT_NEUTRAL'
        }
        formatted_label = label_map.get(label.lower(), 'SENT_NEUTRAL')

        # Return formatted response with label and score
        return {
            'label': formatted_label,
            'score': score
        }

    except ApiException as ex:
        # Handle Watson API errors (500, 400, etc.)
        print(f"Watson NLU API error: {ex.code} - {ex.message}")
        return {
            'label': None,
            'score': None
        }

    except (KeyError, ValueError, TypeError) as ex:
        # Return error format if response parsing fails
        print(f"Response parsing error: {ex}")
        return {
            'label': None,
            'score': None
        }
