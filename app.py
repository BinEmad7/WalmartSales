import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Page Setup
st.set_page_config(page_title="Walmart Sales Dashboard", layout="wide")
st.title("🛒 Walmart Interactive Analysis")
st.markdown("This dashboard provides real-time insights into transaction volume, profitability, and customer behavior.")
    
# 2. Load Data
@st.cache_data
def load_data():
    # Loading the cleaned dataset
    df = pd.read_csv("Walmart_clean_data.csv")
    df.columns = [col.strip().lower() for col in df.columns]
    
    # Ensuring date and hour are numeric/datetime for calculations
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    if 'hour' in df.columns:
        df['hour'] = pd.to_numeric(df['hour'])
        
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Options")

city_filter = st.sidebar.multiselect("Select Cities:", options=sorted(df["city"].unique()), default=df["city"].unique())
category_filter = st.sidebar.multiselect("Select Categories:", options=sorted(df["category"].unique()), default=df["category"].unique())
year_filter = st.sidebar.multiselect("Select Years:", options=sorted(df['year'].unique()), default=df['year'].unique())

# NEW: Payment Method Slicer
payment_filter = st.sidebar.multiselect("Select Payment Methods:", 
                                        options=sorted(df["payment_method"].unique()), 
                                        default=df["payment_method"].unique())

# Update the Filtering Logic to include payment_method
df_filtered = df[
    (df["city"].isin(city_filter)) & 
    (df["category"].isin(category_filter)) & 
    (df["year"].isin(year_filter)) &
    (df["payment_method"].isin(payment_filter))
]

# Safety Check: Stop if no data matches filters
if df_filtered.empty:
    st.warning("No data matches the selected filters. Please adjust your slicers.")
    st.stop()

# 4. Key Metrics (The "Top Bar")
# Row 1: Totals
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Revenue", f"${df_filtered['total_price'].sum():,.2f}")
m2.metric("Total Profit", f"${df_filtered['profit'].sum():,.2f}")
m3.metric("Total Transactions", f"{df_filtered['invoice_id'].nunique():,}")

# Dynamic Peak Hour Calculation
peak_h = int(df_filtered['hour'].mode()[0])
m4.metric("Peak Shopping Hour", f"{peak_h}:00")

# Row 2: Averages
a1, a2, a3, a4 = st.columns(4)
a1.metric("Avg Transaction Value (ATV)", f"${df_filtered['total_price'].mean():,.2f}")
a2.metric("Avg Profit per Sale", f"${df_filtered['profit'].mean():,.2f}")
a3.metric("Avg Unit Price", f"${df_filtered['unit_price'].mean():,.2f}")
a4.metric("Avg Customer Rating", f"{df_filtered['rating'].mean():.2f} ⭐")

st.markdown("---")

# 5. Visualizations
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Revenue by Payment Method")
    fig, ax = plt.subplots()
    # Highlighting how people prefer to pay
    sns.barplot(data=df_filtered, x='payment_method', y='total_price', estimator=sum, palette="viridis", ax=ax)
    ax.set_ylabel("Total Revenue ($)")
    st.pyplot(fig)

with right_chart:
    st.subheader("Average Rating by Category")
    category_rating = df_filtered.groupby("category")["rating"].mean().reset_index().sort_values("rating", ascending=False)
    fig2, ax2 = plt.subplots()
    sns.barplot(data=category_rating, x='rating', y='category', palette="gist_earth", ax=ax2)
    ax2.set_xlim(0, 10) # Ratings are out of 10
    st.pyplot(fig2)

# 5.2 Revenue vs Profit Over Time
st.markdown("---")
st.subheader("Monthly Revenue vs. Profit Trends")

# Grouping by Year-Month
df_year_month = df_filtered.groupby(df_filtered["date"].dt.to_period('M'))[["profit", "total_price"]].sum().reset_index()
df_year_month["date"] = df_year_month["date"].dt.to_timestamp()

# Preparing data for Seaborn (Melting)
df_melted_year_month = df_year_month.melt(id_vars="date", var_name="Attribute", value_name="Total_Amount")

fig4, ax4 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=df_melted_year_month, x="date", y="Total_Amount", hue="Attribute", marker='o', ax=ax4)
ax4.set_title("Total Revenue vs Profit by Month")
ax4.set_ylabel("Amount ($)")
st.pyplot(fig4)

# 5.3 Weekly Revenue vs Profit (NEW)
st.markdown("---")
st.subheader("Revenue vs. Profit by Day of Week")

# 1. Group and Sort by Calendar Order
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df_day_of_week = df_filtered.groupby("day_of_week")[["profit", "total_price"]].sum().reset_index()

# Convert day_of_week to categorical to ensure Monday-Sunday order
df_day_of_week["day_of_week"] = pd.Categorical(
    df_day_of_week["day_of_week"], categories=order, ordered=True
)
df_day_of_week = df_day_of_week.sort_values("day_of_week")

# 2. Prepare data for Seaborn
df_melted_day = df_day_of_week.melt(id_vars="day_of_week", var_name="Attribute", value_name="Total_Amount")

# 3. Plot
fig5, ax5 = plt.subplots(figsize=(12, 4))
sns.barplot(data=df_melted_day, x="day_of_week", y="Total_Amount", hue="Attribute", palette="muted", ax=ax5)
ax5.set_ylabel("Total Amount ($)")
st.pyplot(fig5)

# 5.5 Hourly Trends (Dynamic Peak Line)
st.markdown("---")
st.subheader("Transaction Volume by Hour")
fig3, ax3 = plt.subplots(figsize=(12, 4))
hourly_counts = df_filtered.groupby('hour').size().reset_index(name='transaction_count')

sns.lineplot(data=hourly_counts, x='hour', y='transaction_count', marker='o', color='#2ecc71', ax=ax3)
plt.xticks(range(int(df['hour'].min()), int(df['hour'].max()) + 1))
ax3.set_xlabel("Hour of Day (24h Format)")
ax3.set_ylabel("Number of Transactions")

# The Dynamic Vertical Line
ax3.axvline(peak_h, color='red', linestyle='--', label=f'Peak Hour ({peak_h}:00)')
plt.legend()
st.pyplot(fig3)

# 6. Advanced Category Deep-Dive
st.markdown("---")
st.header("📊 Category Efficiency Analysis")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Profitability Index by Category")
    # Profit Margin % per category
    df_filtered['margin_pct'] = (df_filtered['profit'] / df_filtered['total_price']) * 100
    avg_margin = df_filtered.groupby("category")["margin_pct"].mean().sort_values(ascending=False)
    st.bar_chart(avg_margin)

with col_b:
    st.subheader("Average Units per Receipt")
    # Shows if customers bulk-buy certain categories
    avg_units = df_filtered.groupby("category")["quantity"].mean().sort_values(ascending=False)
    st.bar_chart(avg_units)

# 7. Data Table
st.markdown("---")
st.subheader("Raw Data Preview")
st.dataframe(df_filtered.head(12), use_container_width=True)