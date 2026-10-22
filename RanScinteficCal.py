import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

operation = st.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Sine",
        "Cosine",
        "Tangent",
        "Log",
        "Natural Log"
    ]
)

if operation in ["Square Root", "Sine", "Cosine", "Tangent", "Log", "Natural Log"]:
    num = st.number_input("Enter Number")

    if st.button("Calculate"):
        try:
            if operation == "Square Root":
                result = math.sqrt(num)

            elif operation == "Sine":
                result = math.sin(math.radians(num))

            elif operation == "Cosine":
                result = math.cos(math.radians(num))

            elif operation == "Tangent":
                result = math.tan(math.radians(num))

            elif operation == "Log":
                result = math.log10(num)

            elif operation == "Natural Log":
                result = math.log(num)

            st.success(f"Result = {result}")

        except:
            st.error("Invalid Input")

else:
    num1 = st.number_input("First Number")
    num2 = st.number_input("Second Number")

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
                result = None

        elif operation == "Power":
            result = num1 ** num2

        if result is not None:
            st.success(f"Result = {result}")
