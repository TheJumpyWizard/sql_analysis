import sqlparse
import networkx as nx

async def generate_data_lineage(query):
    """
    Parses the given SQL query and generates data lineage by building a directed graph that shows how data flows through the database.
    """
    # Parse the SQL query
    parsed = await parse_sql_query(query)
    
    # Initialize an empty graph
    graph = nx.DiGraph()
    
    # Traverse the parsed tree and extract information about the tables and columns referenced in the query
    for token in parsed.tokens:
        if isinstance(token, sqlparse.sql.IdentifierList):
            for identifier in token.get_identifiers():
                if identifier.is_keyword:
                    continue
                graph.add_node(str(identifier), type="column")
        elif isinstance(token, sqlparse.sql.Identifier):
            if token.is_keyword:
                continue
            graph.add_node(str(token), type="table")
        elif isinstance(token, sqlparse.sql.Where):
            for comparison in token.tokens:
                if not isinstance(comparison, sqlparse.sql.Comparison):
                    continue
                column, operator, value = comparison.get_identifiers()
                graph.add_edge(str(column), str(value))
    
    # Return the data lineage graph
    return graph

