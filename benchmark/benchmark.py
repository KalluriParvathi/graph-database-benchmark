import os
import time
import statistics
import csv

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
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD"),
    ),
)

DATABASE = os.getenv("NEO4J_DATABASE")

TEST_NODE = 1001
RUNS = 10

results = []


def benchmark(query_name, query, parameters=None):
    times = []

    with driver.session(database=DATABASE) as session:

        for _ in range(RUNS):

            start = time.perf_counter()

            if parameters:
                session.run(query, **parameters).consume()
            else:
                session.run(query).consume()

            end = time.perf_counter()

            times.append((end - start) * 1000)

    average = statistics.mean(times)
    p50 = statistics.median(times)
    p95 = sorted(times)[int(0.95 * len(times)) - 1]

    print(f"{query_name:<20} Avg={average:.2f} ms")

    results.append([
        query_name,
        round(average, 2),
        round(p50, 2),
        round(p95, 2)
    ])


print("\n===== NEO4J AURA BENCHMARK =====\n")

benchmark("1-Hop Traversal", TRAVERSAL_1, {"id": TEST_NODE})
benchmark("2-Hop Traversal", TRAVERSAL_2, {"id": TEST_NODE})
benchmark("3-Hop Traversal", TRAVERSAL_3, {"id": TEST_NODE})
benchmark("Point Lookup", POINT_LOOKUP, {"id": TEST_NODE})
benchmark("Aggregation", AGGREGATION)

os.makedirs("results", exist_ok=True)

with open("results/results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Query",
        "Average (ms)",
        "p50 (ms)",
        "p95 (ms)"
    ])

    writer.writerows(results)

print("\nResults saved to results/results.csv")

driver.close()