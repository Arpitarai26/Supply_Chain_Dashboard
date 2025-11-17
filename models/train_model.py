# -----------------------------------------------------
# models/train_model.py - train and save ML model
# -----------------------------------------------------
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import json
import os

def train_and_save_model():
    """Train and save a regression model to predict TotalRevenue."""
    # Always resolve absolute paths safely
    current_dir = os.path.dirname(os.path.abspath(__file__))  # models/
    root_dir = os.path.dirname(current_dir)  # project root (Dashboard_)
    csv_path = os.path.join(root_dir, "supply_chain_deliveries.csv")
    model_path = os.path.join(current_dir, "model.pkl")
    metadata_path = os.path.join(current_dir, "model_metadata.json")

    # --- Load data ---
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ Dataset not found: {csv_path}")

    df = pd.read_csv(csv_path)
    X = df[["OrderCount", "NumberOfPieces"]]
    y = df["TotalRevenue"]

    # --- Train model ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # --- Save model ---
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    # --- Save metadata ---
    metadata = {
        "model_name": "Revenue Predictor",
        "version": "1.0",
        "algorithm": "LinearRegression",
        "trained_on": str(pd.Timestamp.now()),
        "features": ["OrderCount", "NumberOfPieces"],
        "target": "TotalRevenue"
    }

    with open(metadata_path, "w") as meta_file:
        json.dump(metadata, meta_file, indent=4)

    print(f"✅ Model trained and saved successfully:")
    print(f"   📦 Model path:     {model_path}")
    print(f"   🧾 Metadata path:  {metadata_path}")

if __name__ == "__main__":
    train_and_save_model()
