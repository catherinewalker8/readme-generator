import InquirerPy

# Questions for the README file
# Project Title
# Description
# Installation Instructions
# Usage Information
# License (choose from a dropdown list)
# Author Name
# Contact Information

questions = [
    {"type": "input", "name": "project-title", "message": "What is the title of your project?"},
    {"type": "input", "name": "description", "message": "Write a decsription of your project"},
    {"type": "input", "name": "installation-instructions", "message": "Give the installation instructions"},
    {"type": "input", "name": "usage-info", "message": "Provide come usage information"},
    {"type": "list", "name": "license", "message": "Select the license", "choices": [
        "MIT License", "Apache License 2.0", "GNU GPL v3", "GNU LGPL v3", 
        "Mozilla Public License 2.0", "Creative Commons", "Unlicensed"]},
    {"type": "input", "name": "author-name", "message": "What is the name of the author?"},
    {"type": "input", "name": "contact-info", "message": "Provide some contact imformation"}
]

