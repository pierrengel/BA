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
        --text-mint: #76c8b9;      /* DIMMER Mint (Text Normal / Box Hover) */
        --text-dark: #0d1b2a;      /* Deep Dark Blue (Text Hover) */
    }

    /* Main App Background */
    .stApp {
        background-color: var(--app-bg);
        color: var(--text-mint);
    }

    /* BIG BOX BUTTON STYLING */
    div.stButton > button {
        background-color: var(--box-bg);
        color: var(--text-mint);   /* Mint Text */
        border: none;              /* NO BORDERS */
        border-radius: 15px;
        
        /* TYPOGRAPHY */
        font-size: 22px; 
        text-align: left;
        white-space: pre-wrap;     /* Allows subtitles on new lines */
        font-family: 'Helvetica', sans-serif;
        
        /* SIZING & POSITIONING */
        width: 100%;
        min-height: 50vh;          /* Takes up half the screen height */
        padding: 40px;
        margin-top: 20px;          /* Adds a little space at the top of the button */
        
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* Soft shadow for depth */
    }

    /* HOVER EFFECT */
    div.stButton > button:hover {
        background-color: var(--text-mint) !important; /* Box turns Dimmer Mint */
        color: var(--text-dark) !important;            /* Text turns Dark Blue (Forced) */
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        border: none;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: var(--text-mint) !important;
        font-family: 'Helvetica', sans-serif;
    }

    /* Normal text (outside buttons) */
    p, li {
        color: #e0e1dd; /* Off-white for readability on dark background */
        font-size: 1.1rem;
    }

    /* Expander Styling (for How It Works) */
    .streamlit-expanderHeader {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border-radius: 5px;
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
        # \n\n creates the spacing between Title and Subtitle inside the button
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
    st.markdown("<br>", unsafe_allow_html=True) # Spacer
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
    
    # Placeholders: 3 Titles, 3 Subtitles, 3 Collapsible Texts
    sections = [
        {"title": "1. SUBMISSION", "sub": "Initial concept phase"},
        {"title": "2. REVIEW", "sub": "Feasibility check"},
        {"title": "3. LAUNCH", "sub": "Go to market"}
    ]
    
    gibberish = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    
    for s in sections:
        st.subheader(s["title"])
        st.markdown(f"*{s['sub']}*") # Subtitle in italics
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
