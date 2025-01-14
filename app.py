import streamlit as st
import pandas as pd

# Data for the pricing plans
pricing_data = {
    'Standard': {
        'Endpoints': {'Cost Price': 3.5, 'Selling Price': 5.25},
        'Users': {'Cost Price': 2, 'Selling Price': 3},
        'Learners': {'Cost Price': 2, 'Selling Price': 3},
        'Ninja One': {'Cost Price': 3, 'Selling Price': 4.5},
        'Avepoint': {'Cost Price': 4.5, 'Selling Price': 5.85},
    },
    'Premium': {
        'Endpoints': {'Cost Price': 4.82, 'Selling Price': 7.23},
        'Users': {'Cost Price': 2.76, 'Selling Price': 4.14},
        'Learners': {'Cost Price': 2.48, 'Selling Price': 3.72},
        'Ninja One': {'Cost Price': 3.61, 'Selling Price': 5.415},
        'Avepoint': {'Cost Price': 5.76, 'Selling Price': 7.488},
    }
}

# Function to display the package details
def display_package_details():
    # st.subheader("Packages Details")

    # Display the pricing data in a structured way
    for package, facilities in pricing_data.items():
        st.subheader(f"{package} Package")
        df = pd.DataFrame(facilities).T

        # Format the table to show 2 decimal places
        df = df.applymap(lambda x: f"{x:.2f}")
        st.table(df)

# Function to calculate prices and display the result
def calculate_prices(package, num_endpoints, num_users, num_learners, num_ninja_one, num_avepoint):
    facilities = ['Endpoints', 'Users', 'Learners', 'Ninja One', 'Avepoint']
    cost_prices = []
    selling_prices = []
    num_facilities = [num_endpoints, num_users, num_learners, num_ninja_one, num_avepoint]
    
    for facility, num in zip(facilities, num_facilities):
        facility_cost_price = pricing_data[package][facility]['Cost Price']
        facility_selling_price = pricing_data[package][facility]['Selling Price']
        
        # Calculate total for each facility
        total_cost_price = num * facility_cost_price
        total_selling_price = num * facility_selling_price
        
        cost_prices.append(total_cost_price)
        selling_prices.append(total_selling_price)

    return cost_prices, selling_prices, num_facilities

# Main function for the cost calculation
def cost_calculation():
    
    
    st.subheader("Cost and Selling Price Calculation")

    # Step 1: Select the package
    # with col1:
    package_type = st.selectbox("Choose a package", ["Standard", "Premium"])
    
    col1, col2, col3 = st.columns(3)
    # Step 2: User input for the number of facilities
    with col1:
        num_endpoints = st.number_input("Number of Endpoints", min_value=0, value=0, step=1)
        num_ninja_one = st.number_input("Number of Ninja One", min_value=0, value=0, step=1)
        
        
    with col2:
        num_users = st.number_input("Number of Users", min_value=0, value=0, step=1)
        num_avepoint = st.number_input("Number of Avepoint", min_value=0, value=0, step=1)
        
    with col3:
        num_learners = st.number_input("Number of Learners", min_value=0, value=0, step=1)

    # Step 3: Calculate the prices
    cost_prices, selling_prices, num_facilities = calculate_prices(package_type, num_endpoints, num_users, num_learners, num_ninja_one, num_avepoint)

   
    
    # Step 5: Display the output in a table
    summary_data = {
        'Facility': ['Endpoints', 'Users', 'Learners', 'Ninja One', 'Avepoint'],
        'Number of Facilities': num_facilities,
        'Cost Price': cost_prices,
        'Selling Price': selling_prices
    }

    # Create a DataFrame to display the summary
    summary_df = pd.DataFrame(summary_data)
    summary_df['Cost Price'] = summary_df['Cost Price'].apply(lambda x: f"${x:,.2f}")
    summary_df['Selling Price'] = summary_df['Selling Price'].apply(lambda x: f"${x:,.2f}")

    # Calculate total cost and selling price
    total_cost_price = sum(cost_prices)
    total_selling_price = sum(selling_prices)
    margin = total_selling_price - total_cost_price

    st.divider()
    
     # Step 4: Display the selected package
    st.write(f"##### Selected Package: {package_type}")
    
    # Display total prices and margin
    st.write(f"###### Total Cost Price: ${total_cost_price:,.1f}")
    st.write(f"###### Total Selling Price: ${total_selling_price:,.1f}")
    st.write(f"###### Margin: ${margin:,.1f}")
    #st.divider()
    
    # Display the summary table
    st.table(summary_df)

# Streamlit app
st.title("Service Pricing Plan Calculator")

# Create a menu for Packages Details and Cost Calculation using radio buttons
st.sidebar.write(f"## Select the option:")

menu = st.sidebar.radio("", ["Packages Details", "Cost Calculation"])

# Call functions based on menu selection
if menu == "Packages Details":
    display_package_details()
elif menu == "Cost Calculation":
    cost_calculation()
