
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Property Sniper", layout="wide")
st.title("📍 Property Sniper – Live Listing Preview")

# Load real listings
df = pd.read_csv("real_listings.csv")

# Sidebar filters
st.sidebar.header("🔎 Filter Properties")
states = st.sidebar.multiselect("State", options=df["State"].unique(), default=df["State"].unique())
min_price = st.sidebar.number_input("Min Price", value=300000, step=10000)
max_price = st.sidebar.number_input("Max Price", value=500000, step=10000)
min_score = st.sidebar.slider("Min Investment Score", min_value=0.0, max_value=20.0, value=16.0)

# Apply filters
filtered = df[
    (df["Price"] >= min_price) &
    (df["Price"] <= max_price) &
    (df["State"].isin(states)) &
    (df["Investment Score"] >= min_score)
].sort_values(by="Investment Score", ascending=False)

st.markdown(f"### Showing {len(filtered)} results")

# Display listings
for idx, row in filtered.iterrows():
    with st.container():
        st.markdown(f"**🏡 {row['Address']}** — {row['Suburb']}, {row['State']}")
        st.markdown(f"💰 ${row['Price']:,} | 📐 {row['Land Size (m²)']} m² | 🧠 Score: **{row['Investment Score']}**")
        st.markdown(f"🛏 {row['Beds']} | 🛁 {row['Baths']} | 🚗 {row['Car']}")
        st.markdown(f"[🔗 View Listing]({row['Listing Link']})")
        st.markdown("---")
