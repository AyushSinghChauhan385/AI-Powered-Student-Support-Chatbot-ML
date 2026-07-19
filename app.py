from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("chatbot_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load vectorizer
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# Responses
responses = {
    "admission": "Admission is open. Visit the admission office or apply through the official website.",
    "fees": "The B.Tech fee structure is available on the college website or admission office.",
    "hostel": "Hostel facilities are available for both boys and girls.",
    "courses": "We offer B.Tech, MBA, MCA and Diploma courses.",
    "placement": "The Training & Placement Cell organizes campus placements every year.",
    "scholarship": "Students can apply for UP Scholarship and NSP Scholarship.",
    "library": "The library is open from 9:00 AM to 5:00 PM on working days.",
    "faculty": "Experienced faculty members are available in every department.",
    "exam": "The examination timetable is announced by the university before exams."
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data["message"]

    # Convert question into TF-IDF features
    vector = vectorizer.transform([question])

    # Predict category
    prediction = model.predict(vector)[0]

    # Get response
    reply = responses.get(prediction, "Sorry, I don't understand your question.")

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)