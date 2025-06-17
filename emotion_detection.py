import requests
import json

def emotion_detector(text_to_analyze) -> {}:
    """
    Use Watson NLP library to process inputted text and return it's response
    in JSON format

    Parameters:
    text_to_analyze (str): Text to pass to Watson NLP to analyze

    Returns:
    {}: dictionary with required emotions and a determined dominant emotion parsed from
        the response object received from Watson NLP
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    data = { "raw_document": { "text": text_to_analyze }}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        json_data = response.json()  # Convert response text to json dictionary

        required_emotions_keys = [
            'anger', 
            'disgust',
            'fear',
            'joy',
            'sadness'
        ]

        required_emotions = {}

        for key in required_emotions_keys:
            required_emotions[key] = json_data.get("emotionPredictions", {})[0].get("emotion", {}).get(key)

        required_emotions['dominant_emotion'] = max(required_emotions, key=required_emotions.get)

        return print(json.dumps(required_emotions, indent=4))
        
    except requests.exceptions.RequestException as returnedException:
        return f"An error occurred: {returnedException}"