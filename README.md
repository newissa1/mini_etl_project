# Mini ETL Project with Streamlit Dashboard

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built with Python that:
- Extracts data from a CSV file
- Transforms and cleans the data using pandas
- Loads the data into a SQLite database

A Streamlit dashboard visualizes the processed data with interactive charts.

---

## Project Structure

mini_etl_project/
├── data/
│ └── sales.csv # Source data file
├── database.db # SQLite database (auto-generated)
├── etl.py # ETL pipeline script
├── dashboard.py # Streamlit dashboard app
├── query_data.py # Example SQL queries in Python
└── README.md # Project documentation


---

  How to Run

1. Set up your environment

Make sure you have Python 3.x installed.  
Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# OR
venv\Scripts\activate      # Windows

pip install pandas streamlit sqlite3

2. Run the ETL pipeline

```bash
python etl.py

3. Launch the Streamlit dashboard

```bash
streamlit run dashboard.py

---


Features

1. ETL pipeline with pandas and SQLite
2. Total revenue calculation
3. Revenue breakdown by product and customer
4. Interactive dashboard using Streamlit

Future Improvements

1. Add date range filters on dashboard
2. Enable export of filtered data to CSV
3. Deploy dashboard online (e.g., Streamlit Cloud or Heroku)
4. Extend ETL to support other data sources (JSON, APIs)

<img width="1369" height="265" alt="Screenshot 2025-07-14 at 13 47 24" src="https://github.com/user-attachments/assets/820e896a-5ba3-486c-8aea-cdcf2c347b0c" />

<img width="1358" height="388" alt="Screenshot 2025-07-14 at 13 47 27" src="https://github.com/user-attachments/assets/e7675348-4d04-46c9-8136-62f1b3a60702" />

<img width="1378" height="320" alt="Screenshot 2025-07-14 at 13 47 30" src="https://github.com/user-attachments/assets/16447a82-045b-4d9f-8715-01eb929f6717" />







