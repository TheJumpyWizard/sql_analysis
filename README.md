### SQL Analysis
###### SQL Analysis is a Python application that allows you to parse SQL queries, analyze their structure, and generate data lineage to show how data flows through a database. The application is built using the FastAPI framework and the sqlparse and networkx libraries.

### Installation
To install SQL Analysis, clone the repository and install the required dependencies:

1. git clone https://github.com/your-username/sql-analysis.git
2. cd sql-analysis
3. pip install -r requirements.txt

### Usage
* To run the SQL Analysis application, use the following command:

``` uvicorn main:app --reload ```
This will start the application and automatically reload it whenever you make changes to the code. You can then use the /parse endpoint to parse SQL queries and generate data lineage.

* To parse a SQL query and generate data lineage, send a POST request to http://localhost:8000/parse with a JSON request body that contains the query parameter:

``` curl -X POST -H "Content-Type: application/json" -d '{"query": "SELECT name, age FROM users WHERE age > 18"}' http://localhost:8000/parse ```
This will return a JSON response that contains the data lineage graph as an adjacency list.

### Project Structure
The project is structured as follows:

* sql_analysis/parser.py: Contains the parse_sql_query function, which parses a SQL query using the sqlparse library and returns the parsed tree.

* sql_analysis/generate_data_lineage.py: Contains the generate_data_lineage function, which parses a SQL query, extracts information about the tables and columns referenced in the query, and generates data lineage by building a directed graph that shows how data flows through the database.

* routes/routes.py: Contains the FastAPI application and the endpoint for parsing SQL queries.

* requirements.txt: Contains the required dependencies for the project.

### Contributing
Contributions to SQL Analysis are welcome! If you find a bug or have a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository, make your changes, and submit a pull request.

### License
SQL Analysis is released under the MIT License. See the LICENSE file for more information.