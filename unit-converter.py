import streamlit as st

st.title("🔄 Unit Converter APP 🌍")
st.markdown("Converts Length, Weight, and Time instantly.")
st.write("Welcome! Select a category, and get the value converted instantly!")

# Category selection
category = st.selectbox("📂 Select a category", ["Length", "Weight", "Time"]) 

# User input value
value = st.number_input("🔢 Enter a value")

# Unit conversion options
length_units = ["Kilometers to Miles", "Miles to Kilometers"]
weight_units = ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Kilograms", 
                "Kilograms to Grams", "Pounds to Grams", "Grams to Pounds"]
time_units = ["Seconds to Minutes", "Minutes to Seconds", "Hours to Seconds", "Seconds to Hours", 
              "Minutes to Hours", "Hours to Minutes", "Days to Hours", "Hours to Days"]

# Select unit based on category
if category == "Length":
    unit = st.selectbox("📏 Select a unit", length_units)
elif category == "Weight":
    unit = st.selectbox("⚖️ Select a unit", weight_units)
elif category == "Time":
    unit = st.selectbox("⏳ Select a unit", time_units)

# Function to convert units
def convert_units(category, value, unit):
    if category == "Length":
        conversions = {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value * 1.60934
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value * 0.453592,
            "Grams to Kilograms": value / 1000,
            "Kilograms to Grams": value * 1000,
            "Pounds to Grams": value * 453.592,
            "Grams to Pounds": value / 453.592
        }
    elif category == "Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Hours to Seconds": value * 3600,
            "Seconds to Hours": value / 3600,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Days to Hours": value * 24,
            "Hours to Days": value / 24
        }
    return conversions.get(unit, "Invalid selection")

# Perform conversion and display result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"🔄 Converted Value: **{result:.1f}**")
