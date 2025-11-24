# E-Commerce Daily Sales Analytics Pipeline

## Table of Contents

1. Project Overview
2. Architecture
3. Project Components
4. Datasets
5. Benefits of This Pipeline
6. Dashboard Preview
7. Tech Stack
8. Repository Structure
9. Example Results
10. How to Run Locally
11. Real-World Impact
12. Contact

A production-style, end-to-end data engineering + analytics project that automates the entire workflow of collecting sales data, transforming it, loading it into a data warehouse, and updating a BI dashboard every day.

This project mirrors how modern e-commerce companies manage reporting, analytics, and data-driven decisions.

---

## 🚀 Project Overview

The goal of this project is to automate daily sales reporting by building a complete ETL pipeline that:

* Pulls sales and customer data from a database
* Cleans, transforms, and aggregates it
* Loads it into a warehouse for analytics
* Refreshes a Power BI/Tableau dashboard automatically every morning

This eliminates manual reporting, reduces errors, and supports fast business decisions.

---

## 📌 Architecture

```
E-commerce MySQL Database
        ↓
Python ETL Scripts (Pandas + SQLAlchemy)
        ↓
Data Warehouse (PostgreSQL / BigQuery)
        ↓
Airflow (Daily Scheduled Pipeline)
        ↓
Analytics Tables (Facts + Dimensions)
        ↓
Power BI / Tableau Dashboard (Auto-Refresh)
```

---

## 🧱 Project Components

### **1. Data Sources**

* **customers** table
* **orders** table

### **2. ETL Pipeline (Python)**

* Extract data using SQLAlchemy
* Clean & transform with Pandas
* Aggregate revenue, orders, customer metrics
* Load transformed data into warehouse

### **3. Orchestration (Airflow)**

* Runs the pipeline daily at 06:00
* Tasks:

  * `extract_data`
  * `transform_data`
  * `load_data`

### **4. Data Warehouse Tables**

* **fact_sales_daily**
* **dim_customers**
* **dim_products**

### **5. BI Dashboard**

Power BI / Tableau dashboard featuring:

* Total Revenue
* Total Orders
* Average Order Value
* New vs Returning Customers
* Daily Revenue Trend
* Orders Trend
* Top Products
* Country-Level Insights
* Revenue by Hour

---

## 📊 Dashboard Preview

(Include exported PNG or screenshot in the repo)

---

## 🛠️ Tech Stack

| Layer           | Tools                      |
| --------------- | -------------------------- |
| Programming     | Python, Pandas, SQLAlchemy |
| Orchestration   | Apache Airflow             |
| Storage         | MySQL, PostgreSQL/BigQuery |
| BI              | Power BI / Tableau         |
| Version Control | Git + GitHub               |

---

## 📁 Datasets

### **customers.csv**

Contains customer-level information used to identify new vs returning customers and build demographic insights.

* customer_id
* name
* email
* signup_date
* country

### **orders.csv**

Holds transactional data used for revenue, orders, product performance, and time-based trend analysis.

* order_id
* customer_id
* product
* quantity
* price
* order_datetime

These datasets power every metric in the pipeline, from KPIs to product trends.

---

## 🎯 Benefits of This End-to-End Pipeline

* **Zero manual reporting**: Everything refreshes automatically every day.
* **Reliable decision-making**: Clean, consistent data reduces errors leadership depends on.
* **Scalable architecture**: Easy to plug in new data sources (marketing, inventory, web analytics).
* **Faster insights**: Business can react quickly to product demand and customer behavior.
* **Improved retention tracking**: Clear separation of new vs returning customers.
* **Product strategy alignment**: Identifies top sellers and underperforming items instantly.
* **Operational efficiency**: Analysts save 5–10 hours per week.

---

## 📁 Repository Structure

```
📦 ecommerce-sales-pipeline
│
├── data/
│   ├── customers.csv
│   └── orders.csv
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── airflow/
│   └── dag_daily_sales.py
│
├── dashboard/
│   ├── dashboard.pbix (or .twbx)
│   └── dashboard_screenshot.png
│
├── diagrams/
│   └── architecture.png
│
└── README.md
```

---

## 📈 Example Results

Generated metrics:

* Daily revenue trends
* Order volume trends
* Top-performing products
* New vs returning customer ratios
* Country-level revenue distribution

---

## 🔧 How to Run Locally

### **1. Clone the repository**

```
git clone https://github.com/<your-username>/ecommerce-sales-pipeline.git
cd ecommerce-sales-pipeline
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

### **3. Configure environment variables**

Set DB connection, warehouse credentials, etc.

### **4. Run ETL locally**

```
python etl/extract.py
python etl/transform.py
python etl/load.py
```

### **5. Run with Airflow**

Place the DAG file into your Airflow dags folder and start the scheduler.

---

## 🎯 Real-World Impact

If deployed in a real e-commerce company, this project would:

* Save **5–10 hours/week** of manual reporting
* Ensure **accurate, real-time insights**
* Improve decision-making on pricing, inventory, and marketing
* Give leadership visibility into customer and product performance

---

## 📬 Contact

If you want to collaborate or improve the pipeline, feel free to reach out.
