# =====================================================
# app.py - Main Entry Point for Business Dashboard
# =====================================================
from dash import Dash
from data_loader import load_data
from layout import create_layout
from callbacks import register_callbacks
import os

# -----------------------------------------------------
# Initialize the Dash Application
# -----------------------------------------------------
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    assets_folder=os.path.join(os.getcwd(), "assets")
)
app.title = "Business Performance Dashboard"

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------
try:
    df = load_data("supply_chain_deliveries.csv")
except FileNotFoundError:
    raise SystemExit("❌ Dataset 'supply_chain_deliveries.csv' not found.")

# -----------------------------------------------------
# Set Layout and Register Callbacks
# -----------------------------------------------------
app.layout = create_layout(df)
register_callbacks(app, df)

# -----------------------------------------------------
# Run Server
# -----------------------------------------------------
if __name__ == "__main__":
    print("\n🚀 Launching Business Performance Dashboard...")
    print("Access it at: http://127.0.0.1:8051/\n")
    app.run(debug=True, port=8051)
