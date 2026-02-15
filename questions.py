from InquirerPy import prompt

def ask_questions():

    questions = [
        {"type": "input", "name": "Project Title", "message": "What is the title of your project?", "instruction": "Question 1 of 7",
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Description", "message": "Write a description of your project", "instruction": "Question 2 of 7", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Installation Instructions", "message": "Give the installation instructions", "instruction": "Question 3 of 7", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Usage Information", "message": "Provide some usage information", "instruction": "Question 4 of 7", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "list", "name": "License", "message": "Select the license", "instruction": "Question 5 of 7", "choices": [
            "MIT License", "Apache License 2.0", "GNU GPL v3", "GNU LGPL v3", 
            "Mozilla Public License 2.0", "Creative Commons", "Unlicensed"]},
        {"type": "input", "name": "Author Name", "message": "What is the name of the author?", "instruction": "Question 6 of 7", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Contact Information", "message": "Provide some contact information", "instruction": "Question 7 of 7", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
    ]

    answers = prompt(questions)
    return answers

