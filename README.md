# 🛒 Walmart Sales & Interactive Analytics

This project analyzes Walmart retail sales data containing **9,969 transactions** across 5 years using **SQL for advanced business intelligence** and **Python (Streamlit)** for interactive dashboarding and exploratory data analysis.

The goal is to transform raw transactional data into **actionable business insights** related to financial performance, operational efficiency, and customer behavior.

---

# 📊 Visual Showcase: Key Insights

## 1. Macro Trend: Revenue vs. Profit Growth

![Revenue Trend](images/Total_Revenue_vs_Profit_by_Month.png)

**💡 Insight:**
A near-perfect correlation (**0.9487**) between revenue and profit indicates highly stable margins. A **recurring spike every January 12th** suggests a strong annual promotional event.

---

## 2. Category Efficiency: The Core Engines

![Category Performance](images/Total_Revenue_vs_Profit_by_Category.png)

**💡 Insight:**
**Fashion Accessories** and **Home & Lifestyle** generate nearly **$1M** combined revenue and act as the **primary volume drivers** of the business.

---

## 3. Operations: Peak Traffic Windows

![Hourly Trends](images/Number_of_Transactions_by_Hour.png)

**💡 Insight:**
Traffic surges after 11:00 AM, peaking at **15:00 (3 PM)** — the most critical staffing window.

---

## 4. Customer Behavior: Payment Preferences

![Payment Methods](images/Number_of_Transactions_and_Total_Revenue_by_Payment_Methods.png)

**💡 Insight:**
**Credit Cards generate the highest revenue ($488K)**, indicating use for high-value purchases, while E-wallets dominate smaller transactions.

---

# 📌 Business Objectives

### Sales & Financials

* Revenue trends over time
* Profit vs revenue drivers
* Impact of **Quantity vs Unit Price**

### Operations

* Peak shopping hours
* Best-performing days

### Customer & Product Insights

* Customer satisfaction (ratings)
* Average Transaction Value (ATV)
* Category efficiency

---

# 🗄️ Data Structure

| Column         | Description           |
| -------------- | --------------------- |
| invoice_id     | Unique transaction ID |
| branch         | Store branch          |
| city           | Store city            |
| category       | Product category      |
| unit_price     | Price per unit        |
| quantity       | Units sold            |
| date           | Transaction date      |
| time           | Transaction time      |
| payment_method | Payment type          |
| rating         | Customer rating       |
| profit_margin  | Profit percentage     |
| total_price    | Revenue               |
| profit         | Net profit            |

---

# 📈 Executive Summary

### 💰 Financial Performance

* **Revenue:** $1,209,726
* **Profit:** $476,139
* **Correlation (Revenue vs Profit):** **0.9487**

### 🔥 Key Drivers

* **Quantity → Profit (0.7565)** → strongest driver
* Business is **volume-based, not price-based**

### 🏆 Category Insights

* **Top Volume:** Fashion & Home
* **Highest Ratings:** Food & Beverages (~7.11)
* **Best Margins:** Essential goods (~40%)

### ⏱️ Operational Insights

* **Peak Hour:** 15:00
* **Best Day:** Tuesday
* **Seasonality:** Mid-January spike

---

# 📊 Category Performance

| Category            | Revenue | Profit | Rating   |
| ------------------- | ------- | ------ | -------- |
| Fashion accessories | $489K   | $192K  | 5.78     |
| Home & lifestyle    | $489K   | $192K  | 5.74     |
| Food & beverages    | $53K    | $21K   | **7.11** |
| Health & beauty     | $46K    | $18K   | 7.00     |

---

# 📅 Time-Based Insights

### Peak Hours

* **15:00 → highest traffic**
* Afternoon dominates sales

### Weekly Performance

* **Tuesday → best day**
* **Monday → lowest**

### Monthly Trends

* Strong spikes in **January, November, December**

---

# 📈 Correlation Insights

| Metric      | Profit Correlation |
| ----------- | ------------------ |
| Quantity    | **0.7565**         |
| Unit Price  | 0.5007             |
| Total Price | **0.9487**         |

**Conclusion:**
👉 Profit is driven mainly by **sales volume**, not pricing.

---

# 🛠️ Technologies Used

* **SQL (PostgreSQL)** → Aggregation & business logic
* **Python (Pandas)** → Data processing
* **Streamlit** → Dashboard
* **Seaborn & Matplotlib** → Visualization

---

# 🚀 How to Run

```bash
git clone https://github.com/BinEmad7/WalmartSales.git
cd WalmartSales
pip install pandas seaborn matplotlib streamlit
streamlit run app.py
```

---

# 📊 Available Visualizations

Located in `/images`:

* Revenue vs Profit (Month / Year / Day)
* Category Performance
* Hourly Transactions
* Payment Analysis
* Revenue Distribution

---

# 🎯 Key Takeaways

* Business is **volume-driven**
* **Fashion & Home** dominate traffic
* **Essential goods drive loyalty**
* Strong **seasonal pattern (January spike)**
* Peak operations must focus on **afternoon hours**

---

# 👤 Author

Ahmed Alsharif
