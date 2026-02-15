from InquirerPy import prompt
import markdown

# Questions for the README file
# Project Title
# Description
# Installation Instructions
# Usage Information
# License (choose from a dropdown list)
# Author Name
# Contact Information

questions = [
    {"type": "input", "name": "Project Title", "message": "What is the title of your project?"},
    {"type": "input", "name": "Description", "message": "Write a description of your project"},
    {"type": "input", "name": "Installation Instructions", "message": "Give the installation instructions"},
    {"type": "input", "name": "Usage Information", "message": "Provide some usage information"},
    {"type": "list", "name": "License", "message": "Select the license", "choices": [
        "MIT License", "Apache License 2.0", "GNU GPL v3", "GNU LGPL v3", 
        "Mozilla Public License 2.0", "Creative Commons", "Unlicensed"]},
    {"type": "input", "name": "Author Name", "message": "What is the name of the author?"},
    {"type": "input", "name": "Contact Information", "message": "Provide some contact information"},
]

answers = prompt(questions)

keys = list(answers.keys())

print(keys)

print(answers)
print(answers["Project Title"])

print(type(answers))

with open("README.md", "w") as file:
    file.write(
        f"# {answers['Project Title']}\n"
        f"*{answers['Author Name']}*- \n"
        f"*{answers['Contact Information']}*\n\n"
        f"{answers['Description']}\n\n"
        f"## Installation Instructions\n"
        f"{answers['Installation Instructions']}\n\n"
        f"## Usage Information\n"
        f"{answers['Usage Information']}\n\n"
        f"## License\n"
        f"{answers['License']}\n"
    )

# with open("README.md", "w") as file:
#     for key, value in answers.items():
#         file.write(f"## {key} : ###### {value} \n")



# with open("README.md", "w") as file:
#     file.write(answers)

# with open("README.md") as file:
#     print(file.read())