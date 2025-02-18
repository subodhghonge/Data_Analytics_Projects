import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/airbnb_cleaned.csv")

def plot_price_distribution():
    plt.figure(figsize=(8,5))
    sns.histplot(df["price"], bins=50, kde=True)
    plt.title("Price Distribution")
    plt.show()


if __name__ == "__main__":
    plot_price_distribution()