import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select conversion category", ["Length", "Weight", "Temperature"])
    value = st.number_input("Enter value to convert", min_value=0.0, format="%f")
    
    if category == "Length":
        from_unit = st.selectbox("From Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        to_unit = st.selectbox("To Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        result = length_converter(value, from_unit, to_unit)
    
    elif category == "Weight":
        from_unit = st.selectbox("From Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
        to_unit = st.selectbox("To Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
        result = weight_converter(value, from_unit, to_unit)
    
    elif category == "Temperature":
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(value, from_unit, to_unit)
    
    st.write(f"Converted Value: {result:.4f} {to_unit}")
    
if __name__ == "__main__":
    main()
