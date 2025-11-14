from db import DB
import pandas as pd
import os

if __name__ == "__main__":
    db = DB(host='localhost', port=5433, database="bd_etl", user="postgres", password="postgres")

    for file in os.listdir("02-silver-validated"):
        df = pd.read_parquet(f"02-silver-validated/{file}")

        db.create_table(
            file.replace(".parquet", ""),
            df.columns.tolist()
        )

        db.insert_data(
            file.replace(".parquet", ""),
            df
        )

    db.close()