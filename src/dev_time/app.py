import typer

app = typer.Typer()


@app.command()
def create_project(name: str):
    """Create a new project by given name."""
    pass


@app.command
def summary():
    """Prints a summary of projects."""
    pass


@app.command
def log_time(name_project: str, time: str):
    """
    Adds time to a project.
    Time must be in the format: num+'h' num+'m' or num+'s' (e.g., 2h p30m 15s).
    """
    # Validate the time format using regex
    # if not re.match(r"^\d+[hms]$", time):
    #     typer.echo("Error: Time must be in the format num+h, num+m, or num+s (e.g., 2h, 30m, 15s).")
    #     raise typer.Exit(code=1)

    # typer.echo(f"Logging {time} to project {name_project}")

    pass


def main():
    app()


if __name__ == "__main__":
    main()
