import streamlit as st
from calculator_logic import add, subtract, multiply, divide

st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

result = None
operation = None

# Operation buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("+"):
        operation = "add"
with col2:
    if st.button("_"):
        operation = "subtract"
with col3:
    if st.button("x"):
        operation = "multiply"
with col4:
    if st.button("/"):
        operation = "divide"

if operation:
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        st.success(f"Result: {result}")
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception:
        st.error("An unexpected error occurred.")
