import streamlit as st

import matplotlib.pyplot as plt

# Function to calculate SIP returns

def calculate_sip_returns(monthly_investment, expected_return, time_period):

    total_amount = monthly_investment * time_period * 12

    estimated_return = total_amount * (expected_return / 100)

    return estimated_return, total_amount

# Streamlit App

def main():

    # Page Title

    st.title("SIP Return Calculator")

    # Sidebar Inputs

    st.sidebar.title("Inputs")

    monthly_investment = st.sidebar.slider("Monthly Investment", min_value=500, max_value=100000, step=500, value=5000)

    expected_return = st.sidebar.slider("Expected Return (%)", min_value=0.1, max_value=30.0, step=0.1, value=10.0)

    time_period = st.sidebar.slider("Time Period (Years)", min_value=1, max_value=30, step=1, value=5)

    # Calculate SIP Returns

    estimated_return, total_amount = calculate_sip_returns(monthly_investment, expected_return, time_period)

    # Display Results

    st.header("Results")

    st.subheader("Estimated Return:")

    st.write(f"${estimated_return:,.2f}")

    st.subheader("Total Amount:")

    st.write(f"${total_amount:,.2f}")

    # Circular Graph

    fig, ax = plt.subplots()

    labels = ['Investment', 'Return']

    sizes = [total_amount, estimated_return]

    colors = ['#ff9999', '#66b3ff']

    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

    ax.axis('equal')

    st.pyplot(fig)

# Run the app

if __name__ == '__main__':

    main()

