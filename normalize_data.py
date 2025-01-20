import pandas as pd
from datetime import datetime
from pymongo import MongoClient
import pycountry
import phonenumbers

# Function definitions...

MONGO_URI = "mongodb+srv://amoosavage:testadcore2025@cluster0.tespa.mongodb.net/"
DATABASE_NAME = "payment_db"
COLLECTION_NAME = "payments"

def main():
    try:
        # Load the CSV file
        csv_file = "payment_information.csv"
        df = pd.read_csv(csv_file)
        print(f"Loaded CSV with shape: {df.shape}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        return
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # Drop rows where all columns are NaN
    df.dropna(how='all', inplace=True)

    # Ensure DataFrame has expected columns
    expected_columns = [
        'payee_first_name', 'payee_last_name', 'payee_payment_status',
        'payee_added_date_utc', 'payee_due_date', 'payee_address_line_1',
        'payee_address_line_2', 'payee_city', 'payee_country',
        'payee_province_or_state', 'payee_postal_code', 'payee_phone_number',
        'payee_email', 'currency', 'discount_percent', 'tax_percent',
        'due_amount'
    ]
    if len(df.columns) != len(expected_columns):
        print("CSV columns do not match the expected schema.")
        return
    df.columns = expected_columns

    # Preprocessing and validations...

    if df.empty:
        print("DataFrame is empty after preprocessing.")
        return

    payment_data = df.to_dict(orient='records')
    if not payment_data:
        print("No valid data to insert into MongoDB.")
        return

    # MongoDB insertion
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_many(payment_data)

    print("Data normalization and insertion completed successfully!")

if __name__ == "__main__":
    main()
