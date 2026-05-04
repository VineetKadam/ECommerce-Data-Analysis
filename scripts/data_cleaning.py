import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../data/raw_data.csv")

print("Columns in dataset:")
print(df.columns)

df = df.drop_duplicates()

df = df.dropna()

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

if 'Sales' in df.columns:
    df['Revenue'] = df['Sales']

df.to_csv("../data/cleaned_data.csv", index=False)

print("Cleaned data saved successfully!")
print("Final shape:", df.shape)


# Database connection
username = "postgres"
password = "qpmzty1290" 
host = "localhost"
port = "5432"
database = "ecommerce_db"

# Create connection
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

# Load cleaned data into PostgreSQL
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data successfully loaded into PostgreSQL!")

