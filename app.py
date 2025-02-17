from flask import Flask, render_template, request, jsonify
import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
# Load FAQs
with open("faqs.json", "r") as f:
    faq_data = json.load(f)

questions = [q["question"] for q in faq_data]
answers = [q["answer"] for q in faq_data]
# Vectorize FAQs
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

def get_best_response(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, faq_vectors)
    best_match_idx = similarities.argmax()
    
    if similarities[0][best_match_idx] > 0.2:  # Threshold for relevance
        return answers[best_match_idx]
    else:
        return "Sorry, I don't have an answer for that. Try rephrasing!"

@app.route("/")
def index():
    return render_template("chat.html")
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "")
    response = get_best_response(user_message)
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(debug=True)
