from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)


def insert_batch(tx, batch):
    tx.run("""
    UNWIND $rows AS row

    MERGE (a:Paper {id: row.source})
    MERGE (b:Paper {id: row.target})
    MERGE (a)-[:CITES]->(b)
    """, rows=batch)


def load_dataset():

    batch = []
    total = 0

    with open("dataset/Cit-HepTh.txt", "r") as file:

        for line in file:

            if line.startswith("#"):
                continue

            source, target = line.strip().split()

            batch.append({
                "source": int(source),
                "target": int(target)
            })

            if len(batch) == 1000:

                with driver.session(database=DATABASE) as session:
                    session.execute_write(insert_batch, batch)

                total += len(batch)
                print(f"{total} relationships loaded...")

                batch = []

        if batch:

            with driver.session(database=DATABASE) as session:
                session.execute_write(insert_batch, batch)

            total += len(batch)

    print("--------------------------------")
    print("Dataset Loaded Successfully")
    print(f"Total Relationships : {total}")


if __name__ == "__main__":
    try:
        load_dataset()
    finally:
        driver.close()