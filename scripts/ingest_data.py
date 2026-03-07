import duckdb
import pandas as pd

# connect (this automatically creates marketing.db if it doesn't exist)
conn = duckdb.connect("marketing.db")

# read CSV files
users = pd.read_csv("data/users.csv")
events = pd.read_csv("data/events.csv")
campaigns = pd.read_csv("data/campaigns.csv")

# load into database tables
conn.execute("CREATE OR REPLACE TABLE users AS SELECT * FROM users")
conn.execute("CREATE OR REPLACE TABLE events AS SELECT * FROM events")
conn.execute("CREATE OR REPLACE TABLE campaigns AS SELECT * FROM campaigns")

print("Data successfully ingested into marketing.db")