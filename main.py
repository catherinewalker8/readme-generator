from rich.console import Console
import questions
import filewrite

# Questions for the README.md file:
# Project Title
# Description
# Installation Instructions
# Usage Information
# License (choose from a dropdown list)
# Author Name
# Contact Information

console = Console()

def main():
    console.print("[bold blue] Welcome to the README.md generator![/bold blue]")
    answers = questions.ask_questions()
    filewrite.write_readme(answers)
    console.print("[bold blue] README.md file completed! [/bold blue]")

if __name__ == "__main__":
    main()