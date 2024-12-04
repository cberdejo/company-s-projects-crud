from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
import os

load_dotenv()


# Get environment variables
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOSTNAME")
sid = os.getenv("DB_SID")
port = os.getenv("DB_PORT")


def create_connection(provider: str):
    # Validate provider
    if provider not in ["oracle", "postgres"]:
        raise ValueError("Providers allowed: 'oracle', 'postgres'")

    # Choose protocol based on provider
    protocol = "oracle+oracledb" if provider == "oracle" else "postgresql+psycopg"

    # Create database connection URL
    database_url = f"{protocol}://{username}:{password}@{hostname}:{port}/{sid}"
    print(database_url)
    # Create SQLAlchemy engine
    engine = create_engine(database_url)

    # Create tables from SQLModel metadata
    SQLModel.metadata.create_all(engine)

    return engine
