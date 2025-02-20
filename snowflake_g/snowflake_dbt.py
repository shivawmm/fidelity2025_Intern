import pandas as pd
import snowflake.connector

# Snowflake connection parameters
con = snowflake.connector.connect(
    user="shivawmm",
    password="Shivamsingh@181002",
    account="zg03012.ap-southeast-1",
    warehouse="compute_WH",
    database="fil_DB",
    schema="fil_schema"
)

cur = con.cursor()
cur.execute("SELECT * FROM CUSTOMERS")
data = cur.fetchall()

# Extract column names from cursor description
columns = [desc[0] for desc in cur.description]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)
print(df)

# Close the cursor and connection
cur.close()
con.close()