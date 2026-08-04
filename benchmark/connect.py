from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("COGNODB_URI")
USER = os.getenv("COGNODB_USER")
PASSWORD = os.getenv("COGNODB_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected Successfully' AS message")
        print(result.single()["message"])

if __name__ == "__main__":
    test_connection()