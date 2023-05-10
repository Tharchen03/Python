# Define a dictionary with questions as keys and answers as values
qa_dict = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue whale",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the boiling point of water in Celsius?": "100",
    "What is the symbol for gold on the periodic table?": "Au"
}

# Loop through the questions and prompt the user for answers
for question in qa_dict:
    user_answer = input(question + " ")
    correct_answer = qa_dict[question]
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", correct_answer)
