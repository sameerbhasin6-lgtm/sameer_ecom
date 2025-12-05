import streamlit as st
import time
import random

# --- 1. Dashboard Configuration (The Visuals) ---
st.set_page_config(page_title="HustleBot Dashboard", page_icon="🎙️", layout="wide")

# Custom CSS for that "Streetwear" vibe
st.markdown("""
<style>
    .stApp {background-color: #0e1117; color: #ffffff;}
    .stChatInput {position: fixed; bottom: 0;}
    h1 {color: #ff4b4b; font-family: 'Helvetica', sans-serif;}
    .voice-btn {border: 2px solid #ff4b4b; padding: 10px; border-radius: 5px; color: #ff4b4b; text-align: center;}
</style>
""", unsafe_allow_html=True)

# --- 2. Sidebar (The Analytics Dashboard) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4600/4600296.png", width=80)
    st.title("Admin Dashboard")
    st.metric(label="Active Users (Tier-2 Cities)", value="1,240", delta="+12%")
    st.metric(label="Voice Queries Today", value="450", delta="+8%")
    st.metric(label="Conversion Rate", value="4.2%", delta="+0.5%")
    st.divider()
    st.write("### 🎙️ Voice Server Status")
    st.success("Online (Latency: 24ms)")

# --- 3. The "Brain" (Intent Logic with Hinglish Support) ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # Intent: Voice/Vernacular Greeting
    if any(word in user_input for word in ["hello", "hi", "bhai", "bro", "sun"]):
        return "Yo! Welcome to The Hustler Store. What are we hunting for? (Hoodies, Tees, or Cargo?)"
    
    # Intent: Product Discovery (Voice: "Show me...")
    elif any(word in user_input for word in ["show", "dikhao", "collection", "new"]):
        return ("Here is the latest **'Urban Hustle'** drop:\n"
                "1. Oversized Graphic Tees (Acid Wash) - ₹999\n"
                "2. Heavyweight Hoodies (Black) - ₹1,499\n"
                "3. Cargo Joggers - ₹1,299\n"
                "Tap the mic to say what you want!")
    
    # Intent: Price/Negotiation (Hinglish: "Sasta", "Discount")
    elif any(word in user_input for word in ["price", "sasta", "cheap", "discount", "kam"]):
        return "I got you. Use code **HUSTLE10** for 10% off. Best quality, best price. Deal?"
    
    # Intent: Closing/COD
    elif any(word in user_input for word in ["buy", "le lo", "cart", "cod", "payment"]):
        return "Done! 🚀 Added **Black Hoodie (L)** to cart. **COD is available**. Proceeding to checkout..."
    
    else:
        return "I didn't catch that style. Try saying 'Show me Hoodies' or 'Price kya hai?'"

# --- 4. The Chat Interface ---
st.title("🔥 HustleBot: Voice & Chat Agent")
st.markdown("### Your personal streetwear stylist (English + Hinglish)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Mic check 1..2.. 🎤 What do you want to buy?"})

# Display Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. Input Area (Text OR Voice Simulation) ---
col1, col2 = st.columns([8, 1])

with col1:
    prompt = st.chat_input("Type or Speak...")

# Voice Button Simulation (Visual Only for Report)
with col2:
    st.write("") # Spacer
    st.write("") # Spacer
    if st.button("🎙️"):
        st.toast("Listening... (Voice Input Activated)")
        # In a real app, this would trigger speech_recognition logic
        time.sleep(1)
        st.toast("Processing Voice Query...")

# Handle Input
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Processing vernacular intent..."):
        time.sleep(0.8) # Simulate AI thinking
        response = get_bot_response(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)