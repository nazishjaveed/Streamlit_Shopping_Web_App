import streamlit as st

# Sample products to display
products = {
    'Laptop': {'price': 999.99, 'description': 'A high-performance laptop for work and play'},
    'Smartphone': {'price': 799.99, 'description': 'Latest smartphone with top-notch features'},
    'Headphones': {'price': 199.99, 'description': 'Noise-cancelling headphones for a premium audio experience'},
    'Smart Watch': {'price': 149.99, 'description': 'Track your fitness with this smartwatch'},
}

# Create a session state to store the cart
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Function to add items to the cart
def add_to_cart(product_name, price):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name]['quantity'] += 1
    else:
        st.session_state.cart[product_name] = {'price': price, 'quantity': 1}

# Function to remove items from the cart
def remove_from_cart(product_name):
    if product_name in st.session_state.cart:
        del st.session_state.cart[product_name]

# Function to calculate total price
def calculate_total():
    total = 0
    for item in st.session_state.cart.values():
        total += item['price'] * item['quantity']
    return total

# Display the product catalog
st.title('Streamlit Shopping Web App')
st.subheader('Browse our amazing products!')

# Display product list
for product_name, product_info in products.items():
    st.write(f"### {product_name}")
    st.write(f"**Price**: ${product_info['price']}")
    st.write(f"**Description**: {product_info['description']}")
    
    # Add to cart button
    if st.button(f"Add {product_name} to Cart"):
        add_to_cart(product_name, product_info['price'])
        st.success(f"{product_name} added to cart!")

# Display cart
st.sidebar.title('Your Cart')
if len(st.session_state.cart) == 0:
    st.sidebar.write("Your cart is empty.")
else:
    total_price = 0
    for product_name, product_info in st.session_state.cart.items():
        st.sidebar.write(f"{product_name} x {product_info['quantity']}: ${product_info['price'] * product_info['quantity']}")
        total_price += product_info['price'] * product_info['quantity']
    
    st.sidebar.write(f"### Total: ${total_price:.2f}")
    
    # Checkout button
    if st.sidebar.button('Checkout'):
        st.sidebar.write("Thank you for your purchase!")
        st.session_state.cart.clear()  # Clear the cart after checkout

# Option to view cart and remove items
st.sidebar.title('Manage Cart')
for product_name in st.session_state.cart.keys():
    if st.sidebar.button(f"Remove {product_name} from Cart"):
        remove_from_cart(product_name)
        st.sidebar.write(f"{product_name} removed from cart.")
