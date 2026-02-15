def write_readme(answers):

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
            f"{answers['License']}"
        )