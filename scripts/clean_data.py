import duckdb
import os

conn = duckdb.connect("marketing.db")

sql_files = sorted(os.listdir("sql"))

for file in sql_files:
    with open(f"sql/{file}") as f:
        conn.execute(f.read())

conn.close()