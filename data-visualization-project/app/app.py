import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Data Visualization App",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/processed/cleaned_dataset.csv")
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        return df
    except FileNotFoundError:
        st.error("❌ Processed dataset not found. Please run data_preprocessing.py first.")
        return None

df = load_data()

if df is not None:

    # -------------------------
    # Sidebar Filters
    # -------------------------
    st.sidebar.header("Filters")

    selected_category = st.sidebar.multiselect(
        "Select Category:",
        options=df["category"].unique(),
        default=df["category"].unique()
    )

    selected_location = st.sidebar.multiselect(
        "Select Location:",
        options=df["location"].unique(),
        default=df["location"].unique()
    )

    # Filter data
    filtered_df = df[
        (df["category"].isin(selected_category)) &
        (df["location"].isin(selected_location))
    ]

    # -------------------------
    # Title
    # -------------------------
    st.title("📊 Data Visualization Dashboard")
    st.write("Explore trends and insights from the dataset using interactive charts.")

    # -------------------------
    # Dataset Preview
    # -------------------------
    st.subheader("📁 Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True)

    # -------------------------
    # Summary Statistics
    # -------------------------
    st.subheader("📈 Summary Statistics")
    st.write(filtered_df.describe())

    # -------------------------
    # Line Chart
    # -------------------------
    st.subheader("📉 Value Over Time")
    if "date" in filtered_df.columns:

        fig_line = px.line(
            filtered_df.sort_values("date"),
            x="date",
            y="value",
            color="category",
            title="Value Trends by Category"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    # -------------------------
    # Category Distribution
    # -------------------------
    st.subheader("📦 Category Distribution")
    fig_bar = px.bar(
        filtered_df,
        x="category",
        y="value",
        color="category",
        title="Total Value per Category",
        barmode="group"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # -------------------------
    # Scatter Plot
    # -------------------------
    st.subheader("🔵 Scatter Plot: Value by Location")
    fig_scatter = px.scatter(
        filtered_df,
        x="location",
        y="value",
        color="category",
        size="value",
        title="Value Distribution Across Locations"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # -------------------------
    # Download Filtered Data
    # -------------------------
    st.subheader("⬇️ Download Filtered Data")
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

else:
    st.stop()
