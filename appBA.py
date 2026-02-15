import streamlit as st

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(page_title="ROBIN", layout="wide", page_icon="🐦")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    /* Global Variables */
    :root {
        --app-bg: #1b263b;         /* Lighter Dark Blue (Background) */
        --box-bg: #0d1b2a;         /* Deep Dark Blue (Box Normal) */
        --text-mint: #76c8b9;      /* Dimmer Mint (Text Normal / Box Hover) */
        --text-dark: #0d1b2a;      /* Deep Dark Blue (Text Hover) */
    }

    /* Main App Background */
    .stApp {
        background-color: var(--app-bg);
        color: var(--text-mint);
    }

    /* BIG BOX BUTTON STYLING (Rest State) */
    div.stButton > button {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: none !important;
        border-radius: 15px !important;
        
        /* TYPOGRAPHY */
        font-size: 22px !important; 
        text-align: left !important;
        white-space: pre-wrap !important;
        font-family: 'Helvetica', sans-serif !important;
        
        /* SIZING & POSITIONING */
        width: 100% !important;
        min-height: 50vh !important;
        padding: 40px !important;
        margin-top: 20px !important;
        
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }

    /* HOVER EFFECT - FORCE TEXT COLOR CHANGE */
    div.stButton > button:hover {
        background-color: var(--text-mint) !important; /* Box becomes Mint */
        color: var(--text-dark) !important;            /* Text becomes Dark Blue */
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4) !important;
    }
    
    /* Make the specific text inside the button inherit the hover color */
    div.stButton > button:hover p {
        color: var(--text-dark) !important;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: var(--text-mint) !important;
        font-family: 'Helvetica', sans-serif;
    }

    /* Hide default menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- 3. TEXT PLACEHOLDERS ---
lorem_short = "Short placeholder text to describe this section briefly."

# --- 4. PAGE FUNCTIONS ---

def home_page():
    # Spacer to lower the content
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 20px;'>ROBIN</h1>", unsafe_allow_html=True)
    
    # Another spacer to push boxes down further
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        label = f"GIVE US YOUR IDEA\n\n{lorem_short}"
        if st.button(label):
            navigate_to('ideas')
            
    with col2:
        label = f"HOW ROBIN WORKS\n\n{lorem_short}"
        if st.button(label):
            navigate_to('how_it_works')
            
    with col3:
        label = f"KEEP TRACK OF SUCCESSFUL IDEAS\n\n{lorem_short}"
        if st.button(label):
            navigate_to('success')

def ideas_page():
    if st.button("← BACK", key="back_btn"):
        navigate_to('home')
        
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-bottom: 60px;'>HOW CAN WE HELP YOU WITH YOUR PROJECT?</h1>", unsafe_allow_html=True)
    
    _, mid1, mid2, _ = st.columns([0.5, 2, 2, 0.5])
    
    with mid1:
        label = f"I NEED FINANCIAL SUPPORT\n\n{lorem_short}"
        if st.button(label):
            st.toast("Financial Support Selected")
            
    with mid2:
        label = f"I NEED A HELPING HAND\n\n{lorem_short}"
        if st.button(label):
            st.toast("Volunteer Support Selected")

def how_it_works_page():
    if st.button("← BACK", key="back_btn"):
        navigate_to('home')
    
    st.markdown("---")
    st.title("HOW ROBIN WORKS")
    
    sections = [
        {"title": "1. SUBMISSION", "sub": "Initial concept phase"},
        {"title": "2. REVIEW", "sub": "Feasibility check"},
        {"title": "3. LAUNCH", "sub": "Go to market"}
    ]
    
    gibberish = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    for s in sections:
        st.subheader(s["title"])
        st.markdown(f"*{s['sub']}*")
        with st.expander("Read details"):
            st.write(gibberish)
        st.markdown("<br>", unsafe_allow_html=True)

def success_page():
    if st.button("← BACK", key="back_btn"):
        navigate_to('home')
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 5rem;'>OUR SUCCESS STORIES</h1>", unsafe_allow_html=True)

# --- 5. MAIN CONTROLLER ---

if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'ideas':
    ideas_page()
elif st.session_state.page == 'how_it_works':
    how_it_works_page()
elif st.session_state.page == 'success':
    success_page()
