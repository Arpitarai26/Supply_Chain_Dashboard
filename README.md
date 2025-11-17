    Business Performance Dashboard

An interactive analytics dashboard built using Python Dash, designed for real-time exploration of multi-year supply-chain data.
The package provides modular components for preprocessing, KPI computation, filtering logic, and visualizations including time-series trends, bar charts, and a U.S. choropleth map.

Features

Dynamic Filters
Filter data by Customer, Location, and Business Type with instant graph updates.

Theme Switching
Built-in dark and light themes using modular color palettes.

KPIs
Pre-built components to compute and display:

Total Orders

Total Pieces

Total Revenue

Average Revenue per Order

Unique Customers

Interactive Visualizations

Revenue over time

Revenue by location

Revenue by business type

U.S. state-level revenue map

Modular Structure
Clear separation between:

Preprocessing

KPI logic

Graph modules

Callbacks

Layout/UI

Installation
pip install business-performance-dashboard


(Replace above with your actual PyPI package name.)

Usage Example
from dashboard.app import run_dashboard

# Launch the dashboard at http://127.0.0.1:8051/
run_dashboard("supply_chain_deliveries.csv")


If your package structure is different, I’ll adjust this snippet.

Project Structure
your_package/
│
├── app.py
├── callbacks.py
├── layout.py
├── preprocessing.py
├── components/
│   ├── kpis.py
│   ├── colors_dark.py
│   ├── colors_light.py
│   └── graphs/
│       ├── revenue_trend.py
│       ├── revenue_bar.py
│       ├── revenue_business_type.py
│       └── us_map.py
└── ...

Dataset Requirements

Your CSV must contain these columns:

WorkDate

Customer

Location

BusinessType

OrderCount

NumberOfPieces

TotalRevenue

State (optional but required for the US map)

Running the Dashboard Manually
python app.py


App runs at:

http://127.0.0.1:8051/

Preprocessing Pipeline

The preprocessing module handles:

Date parsing (dayfirst=True)

Normalizing text fields (Customer, Location)

Mapping cities → U.S. state codes

Converting numeric fields

Basic quality checks and outlier inspection

Visual Components
1. Revenue Over Time

Line chart with markers and optional area shading.

2. Revenue by Location

Grouped bar chart with color encoding by customer.

3. Revenue by Business Type

Aggregated revenue per business segment.

4. U.S. Revenue Map

Choropleth map showing revenue distribution across states.

KPI Cards

Each KPI is styled as a compact, shadowed card:

Responsive layout

Custom background colors

Clean typography

Theme Support

Two built-in palettes:

colors_dark.py

colors_light.py

Loaded dynamically using:

import importlib
theme = importlib.import_module(f"components.colors_{selected_theme}")

Requirements
dash
pandas
plotly


Add any others from your code if needed.

License

MIT License (or whichever you choose).

Author

Arpita Rai
M.Sc. Data Science
Central University of Haryana