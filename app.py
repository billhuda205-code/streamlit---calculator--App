import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations.")

st.divider()

# Number Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Choose an Operation",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division"
    )
)

# Calculate Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")

st.divider()

st.caption("Built with ❤️ using Python & Streamlit")
