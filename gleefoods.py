
import streamlit as st

# Welcome page
st.title("Welcome to Foodie Frenzy!")
st.image("food_image.jpg", width=300)
st.write("Order your favorite food now!")

# Order page
order_page = st.selectbox("Choose a page", ["Order", "About Us"])

if order_page == "Order":
	# Food options
	food_options = st.selectbox("Select food", ["Pizza", "Burger", "Salad"])

	# Quantity
	quantity = st.number_input("Quantity", min_value=1, max_value=10)

	# Place order button
if st.button("Place Order"):
		st.write(f"Order placed! {quantity} {food_options} coming your way!")
elif order_page == "About Us":
	st.write("Welcome to Foodie Frenzy! We are a team of food enthusiasts dedicated to serving you the best food in town.")