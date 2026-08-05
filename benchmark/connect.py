from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read Neo4j credentials from .env
URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

# Create Neo4j driver
driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

# Test connection
def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected Successfully' AS message")
        print(result.single()["message"])

# Run the connection test
if __name__ == "__main__":
    test_connection()