from InquirerPy import prompt

def ask_questions():

    questions = [
        {"type": "input", "name": "Project Title", "message": "What is the title of your project?", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Description", "message": "Write a description of your project", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Installation Instructions", "message": "Give the installation instructions", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Usage Information", "message": "Provide some usage information", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "list", "name": "License", "message": "Select the license", "choices": [
            "MIT License", "Apache License 2.0", "GNU GPL v3", "GNU LGPL v3", 
            "Mozilla Public License 2.0", "Creative Commons", "Unlicensed"]},
        {"type": "input", "name": "Author Name", "message": "What is the name of the author?", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
        {"type": "input", "name": "Contact Information", "message": "Provide some contact information", 
            "validate": lambda result: len(result) > 0, "invalid_message": "Input cannot be empty."},
    ]

    return prompt(questions)
