from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    emotions_dict = response["emotionPredictions"][0]["emotion"]
    # moods
    anger = emotions_dict["anger"]
    disgust = emotions_dict["disgust"]
    fear = emotions_dict["fear"]
    joy = emotions_dict["joy"]
    sadness = emotions_dict["sadness"]
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    if dominant_emotion:
        return
    else:
        return "The given text has been identified as {} with a score of {}.".format(
            emotions_dict[dominant_emotion], dominant_emotion
        )


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
