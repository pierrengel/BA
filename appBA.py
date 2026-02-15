import streamlit as st
import random

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

    /* =========================================
       STYLE 1: THE BIG BOXES (Primary Buttons) 
       ========================================= */
    div.stButton > button[kind="primary"] {
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

    /* HOVER for Big Boxes */
    div.stButton > button[kind="primary"]:hover {
        background-color: var(--text-mint) !important; 
        color: var(--text-dark) !important;            
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4) !important;
    }
    
    div.stButton > button[kind="primary"]:hover p {
        color: var(--text-dark) !important;
    }

    /* =========================================
       STYLE 2: THE BACK BUTTON (Secondary Buttons) 
       ========================================= */
    div.stButton > button[kind="secondary"] {
        background-color: var(--text-mint) !important; 
        border: none !important;
        border-radius: 12px !important;
        
        /* THE BLACK BAT TRICK */
        color: transparent !important;  
        text-shadow: 0 0 0 var(--text-dark) !important; 
        
        /* TYPOGRAPHY & SIZE */
        font-size: 50px !important;
        line-height: 50px !important;
        
        /* SIZING - COMPACT BOX */
        height: auto !important;
        width: auto !important;
        padding: 10px 20px !important;
        min-height: 0px !important;
        
        transition: transform 0.2s ease !important;
    }
    
    div.stButton > button[kind="secondary"]:hover {
        transform: scale(1.1) !important; 
        background-color: #ffffff !important; 
    }

    /* Headings */
    h1, h2, h3 {
        color: var(--text-mint) !important;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 2px solid var(--text-mint);
        border-radius: 10px;
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 2px solid var(--text-mint);
        border-radius: 10px;
        min-height: 150px;
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
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 20px;'>ROBIN</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        label = f"GIVE US YOUR IDEA\n\n{lorem_short}"
        if st.button(label, type="primary"):
            navigate_to('ideas')
            
    with col2:
        label = f"HOW ROBIN WORKS\n\n{lorem_short}"
        if st.button(label, type="primary"):
            navigate_to('how_it_works')
            
    with col3:
        label = f"KEEP TRACK OF SUCCESSFUL IDEAS\n\n{lorem_short}"
        if st.button(label, type="primary"):
            navigate_to('success')

def ideas_page():
    if st.button("🦇", type="secondary"):
        navigate_to('home')
        
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-bottom: 60px;'>HOW CAN WE HELP YOU WITH YOUR PROJECT?</h1>", unsafe_allow_html=True)
    
    _, mid1, mid2, _ = st.columns([0.5, 2, 2, 0.5])
    
    with mid1:
        label = f"I NEED FINANCIAL SUPPORT\n\n{lorem_short}"
        if st.button(label, type="primary"):
            st.toast("Financial Support Selected")
            
    with mid2:
        label = f"I NEED A HELPING HAND\n\n{lorem_short}"
        if st.button(label, type="primary"):
            navigate_to('helping_hand')  # Changed navigation here!

def helping_hand_page():
    if st.button("🦇", type="secondary"):
        navigate_to('ideas')
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Describe your project</h1>", unsafe_allow_html=True)

    # Pick a random placeholder
    placeholders = [
        "Let's hear your idea!",
        "Let's find you your best help!",
        "Let's find you your partner!"
    ]
    selected_placeholder = random.choice(placeholders)

    # Layout: Toggle on Left, Input in Center
    col_toggle, col_input = st.columns([1, 3])

    with col_toggle:
        st.markdown("<br><br>", unsafe_allow_html=True) # Spacer to align with text box
        assisted_mode = st.toggle("Assisted Mode")

    with col_input:
        user_text = st.text_area("Your Idea", placeholder=selected_placeholder, label_visibility="collapsed")

    # If Assisted Mode is ON, show the dropdowns
    if assisted_mode:
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.subheader("1. Project Type")
            st.multiselect(
                "What kind of project is it?",
                ["Quick fix", "Big idea", "Else"],
                label_visibility="collapsed"
            )

        with c2:
            st.subheader("2. Resources Needed")
            resources = [
                "Hammer", "Workspace", "Drill", "3D Printer", 
                "Paint", "Wood", "Metal", "Soldering Iron", 
                "Sewing Machine", "Laptop"
            ]
            st.multiselect(
                "What resources do you need?",
                resources,
                label_visibility="collapsed"
            )

        with c3:
            st.subheader("3. Meeting Preference")
            st.radio(
                "Do you want to meet face to face?",
                ["Yes", "No"],
                label_visibility="collapsed"
            )
            
    # Submit Button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Submit Request", type="primary"):
        st.toast("Request Submitted Successfully!")

def how_it_works_page():
    if st.button("🦇", type="secondary"):
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
    if st.button("🦇", type="secondary"):
        navigate_to('home')
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 5rem;'>OUR SUCCESS STORIES</h1>", unsafe_allow_html=True)

# --- 5. MAIN CONTROLLER ---

if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'ideas':
    ideas_page()
elif st.session_state.page == 'helping_hand':
    helping_hand_page()
elif st.session_state.page == 'how_it_works':
    how_it_works_page()
elif st.session_state.page == 'success':
    success_page()
