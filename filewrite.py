from rich.progress import Progress
import time

def write_readme(answers):
    markdown = (
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
    
    lines = markdown.split("\n")
    with Progress() as progress:
        task = progress.add_task("[green]Generating file...", total=len(lines))
        with open("README.md", "w") as file:
            for line in lines:
                file.write(line + "\n")
                time.sleep(0.02)
                progress.update(task, advance=1)