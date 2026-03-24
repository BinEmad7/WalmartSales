# 🛒 Walmart Sales & Interactive Analytics

This project analyzes Walmart retail sales data containing **9,969 transactions** using **SQL for database-level business intelligence** and **Python (Streamlit) for interactive data visualization and exploratory analysis**.

The goal is to transform raw transactional data into **actionable business insights** related to:

*   Financial performance and profitability
*   Category efficiency and margin analysis
*   Hourly traffic and seasonal sales patterns
*   Customer behavior and payment preferences
*   Store and branch performance across 98 cities

---

# Data Structure

The project analyzes a comprehensive dataset with 13 key attributes representing retail operations.

| Column Name      | Description                                           |
| ---------------- | ----------------------------------------------------- |
| invoice_id       | Unique identifier for each transaction                |
| branch           | Unique identifier for the store branch (100 branches) |
| city             | City where the branch is located (98 cities)          |
| category         | Product category (Food, Fashion, Electronics, etc.)   |
| unit_price       | Price of a single unit of the product                 |
| quantity         | Number of units purchased                             |
| date             | Date of the transaction                               |
| time             | Time of the transaction                               |
| payment_method   | Method used (Cash, E-wallet, Credit card)             |
| rating           | Customer satisfaction rating (1–10)                   |
| profit_margin    | Percentage of profit on the transaction               |
| total_price      | Total revenue from the sale (Price × Quantity)        |
| profit           | Total profit earned from the sale                     |

---

# How to Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/BinEmad7/WalmartSales/tree/main
    ```

2.  **Install Dependencies**
    ```bash
    pip install pandas seaborn matplotlib streamlit
    ```

3.  **Run the Interactive Dashboard**
    ```bash
    streamlit run app.py
    ```

4.  **Execute SQL Queries**
    Open the provided `.sql` file in your preferred SQL editor (PostgreSQL/MySQL/SQL Server) to run the business logic queries.

---

# Business Questions & Objectives

This project aims to answer critical questions regarding **operational efficiency and revenue growth**.

### Sales & Financials
*   What is the **Total Revenue and Profit** across the 5-year span?
*   What are the **quarterly and yearly revenue trends**?
*   How strong is the **correlation between sales volume (Quantity) and Profit**?

### Operational Trends
*   What is the **Peak Shopping Hour** to optimize staffing levels?
*   Which **days of the week** drive the most revenue?
*   Is there a recurring **seasonal anomaly** in the daily sales data?

### Category & Product Performance
*   Which categories act as **Volume Engines** vs. **High-Ticket Drivers**?
*   Which categories maintain the **highest customer satisfaction (ratings)**?
*   What is the **Aggregate Margin** of essential vs. luxury goods?

### Customer & Store Insights
*   Which **payment methods** are preferred for high-value transactions?
*   Which **cities and branches** are the top revenue contributors?
*   Does transaction size impact **customer ratings**?

---

# Data Processing & Analysis

The dataset was processed using **Python (Pandas)** and **SQL** to ensure high data integrity:

*   **Feature Engineering:** Created `hour`, `month`, `year`, and `day_of_week` columns from timestamp data.
*   **Metric Calculation:** Developed the **Profitability Index** and **Aggregate Margin** formulas.
*   **Data Cleaning:** Standardized column naming conventions and handled datetime conversions.
*   **Normalization:** Categorized days of the week to ensure chronological sorting in visualizations.

---

# Visual Showcase

These charts are generated from the Streamlit Interactive Dashboard and Python Analysis.

---

## 1. Monthly Revenue vs. Profit Trends
![Monthly Trend](https://via.placeholder.com/800x300?text=Monthly+Revenue+vs+Profit+Trend+Chart)
**Insight:** 
Analysis reveals a consistent growth pattern with massive recurring spikes every **mid-January (specifically Jan 12th)**. This suggests a highly successful annual New Year promotion or restock event.

---

## 2. Category Efficiency: Volume vs. Value
![Category Analysis](https://via.placeholder.com/800x300?text=Category+Efficiency+Analysis+Chart)
**Insight:** 
**Fashion and Home** items are the store's "Core Engines," making up **90% of foot traffic** but with lower ticket sizes ($108). Conversely, **Sports and Food** items are low-volume but high-ticket ($316), representing a significant cross-selling opportunity.

---

## 3. Hourly Transaction Volume
![Hourly Trend](https://via.placeholder.com/800x300?text=Hourly+Traffic+Volume+Chart)
**Insight:** 
The store experiences a sharp surge starting at 11:00 AM, reaching a **Daily Peak at 15:00 (3 PM)**. This identifies the most critical window for floor staffing and checkout management.

---

# Executive Summary (Main Findings)

### Strategic Growth
Total Revenue reached **$1,209,726.38** with a profit of **$476,139.43**. A near-perfect correlation (0.9487) between Total Price and Profit indicates highly stable and predictable pricing margins across the board.

### The Volume Engine
Profitability is driven primarily by **Quantity (0.7565 correlation)**. High-frequency sales in Fashion and Home accessories dictate the bottom line, proving that Walmart's model remains volume-dependent.

### Customer Loyalty
**Food & Beverages** and **Health & Beauty** are the "Customer Favorites," boasting the highest average ratings (~7.11) and the strongest aggregate margins (40.3%). These "Essential Goods" are the primary drivers of customer retention.

### Operational Peaks
**Tuesday** is the highest revenue-generating day of the week, while **Monday** consistently sees the lowest traffic.

---

# SQL Analytics Highlights

Advanced SQL queries were utilized to extract deep-tier business intelligence:
*   **City Performance:** Identified **Weslaco and Waxahachie** as the top revenue-generating cities.
*   **Payment Preferences:** Analyzed how **Credit Card** transactions drive the highest revenue ($488K) compared to Cash and E-wallet.
*   **Branch Metrics:** Ranked the top 100 branches by efficiency and unit sales.
*   **Transaction Volume:** Aggregated unit sales per category, revealing **Fashion Accessories** as the volume leader with 9,653 units sold.

---

# Technologies Used

**SQL (PostgreSQL)**
*   Data Aggregation & Filtering
*   City/Branch Performance Ranking
*   Named Aggregations

**Python**
*   **Streamlit:** For building the interactive web dashboard.
*   **Pandas:** For data manipulation and cleaning.
*   **Seaborn/Matplotlib:** For statistical data visualization.

---

# Author

**Ahmed Alsharif**
