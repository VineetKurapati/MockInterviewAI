from flask import Flask, render_template, request, jsonify
import openai
import time

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

questions = []  # Stores the generated questions
time_limit = 60  # Time limit for the interview (in seconds)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_interview', methods=['POST'])
def start_interview():
    data = request.json
    name = data['fullName']
    company = data['company']
    openai.api_key = data['apiKey']
    coding_language = data['Language']
    print(coding_language)
    # Generate 3 questions using OpenAI's API
    questions.clear()
    for _ in range(3):
        prompt = f"As an interviewer at {company}, generate a coding question , they should be challenging and but not hard but not easy. The user will use {coding_language}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        question = response.choices[0].text.strip()
        questions.append(question)

    # Reset the timer for the new interview
    start_time = time.time()

    return jsonify({'question': questions[0], 'time_limit': time_limit})

@app.route('/check_code', methods=['POST'])
def check_code():
    print("Checking code...")
    print(len(questions))
    print(questions)
    data = request.json
    if 'code' not in data or 'questionNumber' not in data:
        return jsonify({'error': 'Code or question number not provided'})

    user_code = data['code']
    question_number = int(data['questionNumber'])
    
    # Create a prompt using the user's code and the question
    prompt = f"Check if the following code:\n{user_code}\n\nfor the question:\n{questions[question_number]}\n\nis correct or not. If it is correct just say True else just say False"
    
    # Get AI response to evaluate correctness of the code
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    # Check the response text to determine correctness
    response_text = response.choices[0].text.strip()
    print(response_text)
    print(questions[question_number])
    if response_text == "True":
        if question_number < 2:
            next_question = questions[question_number + 1]
            print("Sent True")
            return jsonify({'correct': True, 'next_question': next_question})
            
        else:
            print("Sent True, Interview Over")
            return jsonify({'correct': True, 'next_question': None})  # No more questions
            
    else:
        print("Sent False")
        return jsonify({'correct': False})

    
if __name__ == '__main__':
    app.run(debug=True)
