import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=headers)
    if not text_to_analyse or text_to_analyse.isspace():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None,
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }