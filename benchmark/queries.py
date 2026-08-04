# 1-Hop Traversal
TRAVERSAL_1 = """
MATCH (p:Paper {id:$id})-[:CITES]->(n)
RETURN count(n) AS total
"""

# 2-Hop Traversal
TRAVERSAL_2 = """
MATCH (p:Paper {id:$id})-[:CITES]->()-[:CITES]->(n)
RETURN count(n) AS total
"""

# 3-Hop Traversal
TRAVERSAL_3 = """
MATCH (p:Paper {id:$id})-[:CITES]->()-[:CITES]->()-[:CITES]->(n)
RETURN count(n) AS total
"""

# Point Lookup
POINT_LOOKUP = """
MATCH (p:Paper {id:$id})
RETURN p
"""

# Aggregation
AGGREGATION = """
MATCH (p:Paper)
RETURN count(p) AS total
"""