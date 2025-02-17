import requests
import json
import operator

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json= input_json, headers= header,timeout = 30)

    json_output = json.loads(response.text)

    emotion_extract = json_output['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_extract.items(), 
                            key=operator.itemgetter(1))[0]
    result = {
        "anger": emotion_extract["anger"],
        "disgust": emotion_extract["disgust"],
        "fear": emotion_extract["fear"],
        "joy": emotion_extract["joy"],
        "sadness": emotion_extract["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return result
