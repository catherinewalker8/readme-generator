from rich.console import Console
import time
from rich.progress import track
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
    for example in  track(questions, total=len(answers)):
        time.sleep(1)
        print(example)
    answers = questions.ask_questions()
    filewrite.write_readme(answers)
    console.print("README.md file completed!")

if __name__ == "__main__":
    main()