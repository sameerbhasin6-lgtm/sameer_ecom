import streamlit as st
import time
import random

# --- 1. PAGE CONFIGURATION & THEME ---
st.set_page_config(
    page_title="HustleBot | The Hustler Store",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (THE HUSTLER AESTHETIC) ---
# Colors: Pitch Black (#000000), Dark Grey (#121212), Hustle Red (#FF3B30), Text (#FFFFFF)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Chat Input Bar - Fixed at bottom */
    .stChatInput {
        position: fixed;
        bottom: 20px;
        z-index: 1000;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #333;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Custom Red Accent for Highlights */
    .highlight {
        color: #FF3B30;
        font-weight: bold;
    }
    
    /* Chat Bubbles */
    .stChatMessage {
        background-color: #1E1E1E;
        border-radius: 10px;
        border: 1px solid #333;
    }
    
    /* Button Styling */
    .stButton>button {
        color: white;
        background-color: #FF3B30;
        border: none;
        border-radius: 0px;
        font-weight: bold;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (STORE STATS) ---
with st.sidebar:
    st.title("THE HUSTLER STORE")
    st.markdown("### ⚡ LIVE DASHBOARD")
    
    # Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Users Online", value="842", delta="▲ 12%")
    with col2:
        st.metric(label="Avg Order", value="₹1.2k", delta="▲ 5%")
        
    st.divider()
    
    st.markdown("### 🔥 TRENDING NOW")
    st.image("https://images.unsplash.com/photo-1571945153262-39015c277685?q=80&w=300&auto=format&fit=crop", caption="Acid Wash Oversized Tee")
    st.info("Stock Alert: Only 12 units left in Size L")

# --- 4. THE AI BRAIN (Advanced Clothing Logic) ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # 1. GREETING / VIBE CHECK
    if any(word in user_input for word in ["hi", "hello", "yo", "bhai", "hustler"]):
        return random.choice([
            "Yo! Welcome to **The Hustler Store**. We grinding or shopping today? 🚀",
            "What's good? Ready to upgrade your drip? Tell me what you need."
        ])

    # 2. DISCOVERY (General Clothing)
    elif any(word in user_input for word in ["show", "collection", "new", "clothes", "kapde"]):
        return ("Fresh drops just landed. Check these out:\n\n"
                "1. **Oversized Tees** (Graphic/Plain) - Starting ₹699\n"
                "2. **Cargo Joggers** (6-Pocket) - ₹1,299\n"
                "3. **Varsity Jackets** (Winter Drop) - ₹2,499\n\n"
                "Tap the mic or type **'Show me Joggers'**.")

    # 3. SPECIFIC CATEGORY: HOODIES
    elif "hoodie" in user_input:
        return ("Our **Heavyweight Cotton Hoodies** are sick. 🔥\n"
                "- 360 GSM (Super Thick)\n"
                "- Puff Print on back\n"
                "- Available in **Pitch Black** and **Charcoal Grey**.\n\n"
                "Want to see the size chart?")

    # 4. SIZING & FIT (Critical for Clothing)
    elif any(word in user_input for word in ["size", "fit", "chart", "medium", "large", "xl"]):
        return ("📏 **Size Guide:**\n"
                "We follow **Indian Sizing** but with a streetwear cut.\n"
                "- If you want that **Baggy/Oversized look** -> Go for your regular size.\n"
                "- If you want a **Standard fit** -> Size Down.\n\n"
                "Trust me, stick to your regular size for the vibe.")

    # 5. WASH CARE (Clothing Maintenance)
    elif any(word in user_input for word in ["wash", "care", "shrink", "iron", "dhona"]):
        return ("⚠️ **Care Instructions:**\n"
                "Bro, handle with care:\n"
                "1. **Cold Wash Only** (Machine ok).\n"
                "2. Do NOT iron directly on the print (Flip it inside out).\n"
                "3. Do not bleach.\n"
                "Follow this and the print will last forever.")

    # 6. RETURN POLICY (Trust Building)
    elif any(word in user_input for word in ["return", "exchange", "wapas", "policy"]):
        return ("No stress. We have a **7-Day Easy Exchange Policy**.\n"
                "If the size doesn't fit, we'll swap it for free. Just keep the tags on!\n\n"
                "Want me to create a return ticket?")

    # 7. PRICE & DISCOUNTS (Hinglish Negotiation)
    elif any(word in user_input for word in ["price", "discount", "sasta", "coupon", "code"]):
        return ("For the fam, use code **HUSTLE10** at checkout for flat 10% OFF.\n"
                "Best prices for 240 GSM quality in the market. Bet.")

    # 8. CHECKOUT (Closing)
    elif any(word in user_input for word in ["buy", "cart", "le lo", "bill", "cod"]):
        return ("Done. 🛒 Added to your cart.\n\n"
                "**Total:** ₹1,499 (COD Available)\n"
                "[Click here to Secure Your Order](#)")

    else:
        return "My bad, didn't catch that. Ask me about **Hoodies**, **Sizing**, or **Returns**."

# --- 5. MAIN CHAT INTERFACE ---

st.title("🔥 HUSTLEBOT")
st.markdown("##### YOUR PERSONAL STREETWEAR STYLIST")
st.divider()

# Initialize Chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Welcome to the tribe. What are we copping today? (Tees, Hoodies, Accessories)"
    })

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input Logic
if prompt := st.chat_input("Type here... e.g., 'Show black hoodies'"):
    # User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot Logic
    with st.spinner("Processing style match..."):
        time.sleep(0.8) # Simulate AI thinking
        response = get_bot_response(prompt)
    
    # Bot Response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# --- 6. VOICE INPUT SIMULATION BUTTON (Footer) ---
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    if st.button("🎙️ TAP TO SPEAK (Hinglish Supported)"):
        st.toast("🎤 Listening... Try saying 'Bhai, oversized t-shirt dikhao'")
