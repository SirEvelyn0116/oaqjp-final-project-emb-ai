import requests

def emotion_detector(text_to_analyze) -> str:
    """
    Use Watson NLP library to process inputted text and respond with it's response

    Parameters:
    text_to_analyze (str): Text to pass to Watson NLP to analyze

    Returns:
    str: The text attribute of the response object received from Watson NLP
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    data = { "raw_document": { "text": text_to_analyze }}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        return response.text
    except requests.exceptions.RequestException as returnedException:
        return f"An error occurred: {returnedException}"