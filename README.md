# Nobel Prize Data Analysis & Interactive Dashboard

An interactive data analytics web application built with **Python**, **Pandas**, **Plotly**, and **Dash** that explores historical trends in Nobel Prize laureates across categories, decades, demographics, and academic institutions.

## Key Research Questions Explored
1. **Nationalities Over Time (`rq1.py`):** Tracks which countries have shown the strongest growth in Nobel Prize laureates across decades.
2. **Age Trends by Category (`rq2.py`):** Analyzes how the average age of Nobel Prize winners at the time of award has shifted over time across different disciplines.
3. **Gender Representation Over Decades (`rq3.py`):** Examines both the absolute count of women laureates per decade and the percentage split between male and female winners via an interactive toggle.
4. **Gender Distribution by Category (`rq4.py`):** Compares male vs. female laureate counts across prize categories (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences).
5. **Top Affiliated Institutions (`rq5.py`):** Identifies the universities and research institutions most frequently affiliated with Nobel Prize recipients.

## Project Structure
- `main.py` — Interactive Dash + Bootstrap web dashboard integrating all visualizations and callbacks.
- `data_modelling.py` — Unified data cleaning pipeline (deduplication, missing value standardization, column formatting, and datetime parsing).
- `rq1.py` – `rq5.py` — Modular analysis and Plotly Express visualization scripts for each research question.
- `nobel_dataset.csv` — Historical Nobel Prize laureates dataset.
- `requirements.txt` — Python dependencies.

## How to Run Locally
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Dash application:
   ```bash
   python main.py
   ```
3. Open your browser at `http://127.0.0.1:8050/`.
