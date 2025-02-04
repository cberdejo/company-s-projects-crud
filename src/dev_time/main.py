import csv
import os

import typer
from sqlmodel import Session, SQLModel, create_engine, select
from rich import print
from rich.console import Console
from rich.table import Table

from .model import Project

app = typer.Typer()

console = Console()

err_console = Console(stderr=True)

db_engine = None

db_url = os.getenv("DATABASE_URL", "sqlite:///dev_time.db")

db_debug_flag = bool(os.getenv("DEBUG", False))


def init_db():
    """Database initialization function."""
    global db_engine
    db_engine = create_engine(db_url, echo=db_debug_flag)
    SQLModel.metadata.create_all(db_engine)


def get_project_by_name(session: Session, project_name: str) -> Project | None:
    """Retrieve a project by name from the database."""
    statement = select(Project).where(Project.name == project_name)
    return session.exec(statement).first()


@app.command()
def create_project(name: str) -> None:
    """Create a new project."""
    with Session(db_engine) as session:
        if get_project_by_name(session, name):
            err_console.print(
                f"[bold red]Error:[/bold red] Project '{name}' already exists."
            )
            raise typer.Exit(code=1)

        project = Project(name=name)
        session.add(project)
        session.commit()
        print(f"[green]OK![/green] Project '{name}' created successfully.")


@app.command()
def delete_project(name: str) -> None:
    """Delete a project."""
    with Session(db_engine) as session:
        project = get_project_by_name(session, name)
        if not project:
            err_console.print(
                f"[bold red]Error:[/bold red] Project '{name}' not found."
            )
            raise typer.Exit(code=1)

        session.delete(project)
        session.commit()
        print(f"[green]OK![/green] Project '{name}' deleted successfully. :boom:")


@app.command()
def log_time(name: str, duration: str) -> None:
    """Log time spent on a project."""
    with Session(db_engine) as session:
        project = get_project_by_name(session, name)
        if not project:
            err_console.print(
                f"[bold red]Error:[/bold red] Project '{name}' not found."
            )
            raise typer.Exit(code=1)

        try:
            if "h" in duration:
                minutes = int(float(duration.replace("h", "")) * 60)
            elif "m" in duration:
                minutes = int(duration.replace("m", ""))
            else:
                raise ValueError("Invalid duration format.")
        except ValueError:
            err_console.print(
                "[bold red]Error:[/bold red] Invalid duration format. Usage: '2h' or '30m'."
            )
            raise typer.Exit(code=1)

        project.total_time += minutes
        session.add(project)
        session.commit()

        print(f"[green]OK![/green] Logged {minutes} minutes for '{name}'.")


@app.command()
def summary() -> None:
    """View a summary of all projects and their total logged time."""
    with Session(db_engine) as session:
        projects = session.exec(select(Project)).all()

        if not projects:
            err_console.print("No projects found.")
            return

        table = Table("Project name", "Time logged")
        for project in projects:
            hours, minutes = divmod(project.total_time, 60)
            time_str = f"{hours}h {minutes}m" if hours else f"{minutes}m"
            table.add_row(project.name, time_str)
        console.print(table)


@app.command()
def snapshot(output_file: str) -> None:
    """Export the project data to a CSV file."""
    with Session(db_engine) as session:
        projects = session.exec(select(Project)).all()

        if not projects:
            err_console.print("No projects to export.")
            return

        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Project Name", "Total Time (minutes)"])
            for project in projects:
                writer.writerow([project.name, project.total_time])

        print(f"[green]OK![/green] Snapshot saved to {output_file}.")


def main() -> None:
    """
    Main entry point for the CLI app.
    """
    init_db()
    app()
