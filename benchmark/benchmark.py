import time
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from benchmark.queries import (
    TRAVERSAL_1,
    TRAVERSAL_2,
    TRAVERSAL_3,
    POINT_LOOKUP,
    AGGREGATION,
)

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("COGNODB_URI"),
    auth=(
        os.getenv("COGNODB_USER"),
        os.getenv("COGNODB_PASSWORD"),
    ),
)

TEST_NODE = 1001


def run_query(query_name, query, parameters=None):
    with driver.session() as session:
        start = time.perf_counter()

        if parameters:
            session.run(query, **parameters).consume()
        else:
            session.run(query).consume()

        end = time.perf_counter()

        elapsed = (end - start) * 1000

        print(f"{query_name:<20} {elapsed:.2f} ms")


print("\n===== COGNODB BENCHMARK =====\n")

run_query("1-Hop Traversal", TRAVERSAL_1, {"id": TEST_NODE})
run_query("2-Hop Traversal", TRAVERSAL_2, {"id": TEST_NODE})
run_query("3-Hop Traversal", TRAVERSAL_3, {"id": TEST_NODE})
run_query("Point Lookup", POINT_LOOKUP, {"id": TEST_NODE})
run_query("Aggregation", AGGREGATION)

driver.close()