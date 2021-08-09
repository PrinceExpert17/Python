import sqlite3
import pandas as pd

conn = sqlite3.connect('amztracker.db')

df = pd.read_sql_query('''SELECT * FROM prices''', conn)
print(df)