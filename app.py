import streamlit as st
import pandas as pd
import joblib

# Load trained model
saved = joblib.load("model.pkl")
model = saved["model"]
columns = saved["columns"]

st.title("Airbnb NYC - Price Predictor")
st.write("Estimate the nightly price of an Airbnb listing in New York.")

# Location
borough = st.selectbox(
    "Borough",
    ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
)

# Get available neighbourhoods from training columns
neighbourhoods = sorted(
    col.replace("neighbourhood_", "", 1)
    for col in columns
    if col.startswith("neighbourhood_")
)

neighbourhood = st.selectbox("Neighbourhood", neighbourhoods)

room_type = st.selectbox(
    "Room type",
    ["Entire home/apt", "Private room", "Shared room"]
)

latitude = st.number_input("Latitude", value=40.75, format="%.5f")
longitude = st.number_input("Longitude", value=-73.98, format="%.5f")

minimum_nights = st.number_input(
    "Minimum nights", min_value=1, value=2
)

number_of_reviews = st.number_input(
    "Total reviews", min_value=0, value=10
)

reviews_per_month = st.number_input(
    "Reviews per month", min_value=0.0, value=1.0
)

host_listings = st.number_input(
    "Host listings count", min_value=1, value=1
)

availability = st.slider(
    "Availability (days/year)", 0, 365, 180
)

# Prepare input data
input_data = pd.DataFrame(0, index=[0], columns=columns)

categorical_values = {
    f"neighbourhood_group_{borough}": 1,
    f"neighbourhood_{neighbourhood}": 1,
    f"room_type_{room_type}": 1
}

for col, value in categorical_values.items():
    if col in columns:
        input_data[col] = value

input_data["latitude"] = latitude
input_data["longitude"] = longitude
input_data["minimum_nights"] = minimum_nights
input_data["number_of_reviews"] = number_of_reviews
input_data["reviews_per_month"] = reviews_per_month
input_data["calculated_host_listings_count"] = host_listings
input_data["availability_365"] = availability

# Predict
if st.button("Predict price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated nightly price: ${prediction:.2f}")
    st.caption(
        "This is a statistical estimate, not a guaranteed market price."
    )