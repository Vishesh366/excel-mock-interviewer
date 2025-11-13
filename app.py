#AIzaSyDEQqNQ0yP2ykenZblVhbPXQImENYqTm_E
from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai
import os

# Initialize the GenAI client
genai.configure(api_key="Your key")

app = Flask(__name__)
RESULTS_FILE = "interview_results.json"



questions = [
    "What are the different types of data in Excel?",
    "Can you explain the difference between a relative, absolute, and mixed cell reference?",
    "How would you use VLOOKUP in a practical scenario?",
    "What is the difference between COUNT, COUNTA, COUNTIF, and COUNTIFS?",
    "How do you create and format pivot tables in Excel?",
    "Explain conditional formatting and when you would use it.",
    "What is the difference between Excel formulas and Excel functions?",
    "How would you protect a worksheet or workbook in Excel?",
    "What are macros in Excel and how do you record one?",
    "Can you explain the difference between XLSX and CSV file formats?"
]

results = []
current_index = -1
intro_done = False  # Track whether introduction has been spoken

@app.route("/")
def index():
    return render_template("index.html")

# Step 1: Speak introduction
@app.route("/start_interview", methods=["POST"])
def start_interview():
    global results, current_index, intro_done
    results = []
    current_index = -1
    intro_done = True
    intro_text = "Hello, I am your AI Excel interviewer. Let's begin the mock interview."
    return jsonify({"intro": intro_text})

# Step 2: Get next question
@app.route("/get_question", methods=["GET"])
def get_question():
    global current_index
    current_index += 1
    if current_index < len(questions):
        return jsonify({"question": questions[current_index], "done": False})
    else:
        # Interview finished
        return jsonify({"done": True, "results": results})

@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    global current_index
    data = request.get_json()
    user_answer = data.get("answer", "")

    # Repeat logic
    if user_answer.lower() in ["repeat", "say again", "once more"]:
        return jsonify({"repeat": True, "question": questions[current_index]})

    # Evaluate with Gemini
    try:
        prompt = f"Question: {questions[current_index]}\nAnswer: {user_answer}\nEvaluate in 2-3 sentences."

        model = genai.GenerativeModel("gemini-1.5-flash")  # 👈 correct way
        response = model.generate_content(prompt)

        # response.text contains the model output
        evaluation = response.text.strip()
    except Exception as e:
        evaluation = f"Evaluation failed: {e}"

    # Save result
    results.append({
        "question": questions[current_index],
        "answer": user_answer,
        "evaluation": evaluation
    })

    return jsonify({"repeat": False, "evaluation": evaluation})



if __name__ == "__main__":
    app.run(debug=True)
