import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.fillna({"reviews_per_month": 0}, inplace=True)
    df.drop(["id", 'host_name'], axis=1, inplace=True)
    df = df[df['price'] < df['price'].quantile(0.99)]
    df.to_csv("../data/processed/airbnb_cleaned.csv", index=False)
    print("Data Cleaning Completed!")

if __name__ == "__main__":
    clean_data("../data/raw/listings.csv")