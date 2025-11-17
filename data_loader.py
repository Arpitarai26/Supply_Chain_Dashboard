# -----------------------------------------------------
# data_loader.py - load and preprocess dataset
# -----------------------------------------------------
import pandas as pd
import warnings

warnings.filterwarnings("ignore", message="Parsing dates involving a day of month without a year")

def load_data(file_path="supply_chain_deliveries.csv"):
    """Load and clean supply chain data."""
    df = pd.read_csv(file_path)
    df["WorkDate"] = pd.to_datetime(df["WorkDate"], format="%d-%m-%Y")

    # City → State mapping
    city_to_state = {
        "Chicago": "IL", "Sacramento": "CA", "Detroit": "MI", "Atlanta": "GA",
        "Houston": "TX", "Seattle": "WA", "San Francisco": "CA", "New York": "NY",
        "Los Angeles": "CA", "Dallas": "TX", "Miami": "FL", "Phoenix": "AZ",
        "Boston": "MA", "Denver": "CO", "Minneapolis": "MN", "Portland": "OR"
    }
    df["State"] = df["Location"].map(city_to_state)
    df.dropna(subset=["State"], inplace=True)
    return df
