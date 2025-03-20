import streamlit as st

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Streamlit UI
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number:", step=0.01, format="%.2f")
operator = st.selectbox("Select operation:", ["+", "-", "*", "/"])
num2 = st.number_input("Enter second number:", step=0.01, format="%.2f")

# Calculate button
if st.button("Calculate"):
    result = calculate(num1, operator, num2)
    st.success(f"✅ Result: **{result}**")
