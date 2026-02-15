import streamlit as st
import random

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(page_title="ROBIN", layout="wide", page_icon="🐦")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'selections' not in st.session_state:
    st.session_state.selections = {}

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def toggle_selection(key):
    st.session_state.selections[key] = not st.session_state.selections.get(key, False)

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    /* Global Variables */
    :root {
        --app-bg: #1b263b;
        --box-bg: #0d1b2a;
        --text-mint: #76c8b9;
        --text-dark: #0d1b2a;
    }

    .stApp {
        background-color: var(--app-bg);
        color: var(--text-mint);
    }

    /* =========================================
       1. GLOBAL BIG BOXES (Home/Ideas)
       Target: Any 'primary' button. 
       Effect: Makes it HUGE (50vh) and Mint on Hover.
       ========================================= */
    div.stButton > button[kind="primary"] {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: none !important;
        border-radius: 15px !important;
        font-size: 22px !important; 
        text-align: left !important;
        white-space: pre-wrap !important;
        font-family: 'Helvetica', sans-serif !important;
        width: 100% !important;
        min-height: 50vh !important; /* THE GIANT HEIGHT */
        padding: 40px !important;
        margin-top: 20px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }

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
       2. BACK BUTTON (The Bat)
       Target: Any 'secondary' button.
       ========================================= */
    div.stButton > button[kind="secondary"] {
        background-color: var(--text-mint) !important; 
        border: none !important;
        border-radius: 12px !important;
        color: transparent !important;  
        text-shadow: 0 0 0 var(--text-dark) !important; 
        font-size: 50px !important;
        line-height: 50px !important;
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

    /* =========================================
       3. SUBMIT BUTTON (Tertiary)
       ========================================= */
    div.stButton > button[kind="tertiary"] {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: auto !important;
        padding: 15px !important;
        min-height: 0px !important;
        margin-top: 20px !important;
    }
    
    div.stButton > button[kind="tertiary"]:hover {
        background-color: #ffffff !important;
        transform: scale(1.01) !important;
    }

    /* =========================================
       4. SMALL SELECTION GRID OVERRIDES
       This targets buttons ONLY when they are inside the 'small-grid' div.
       This overrides the global settings above.
       ========================================= */
    
    /* Reset size for ALL buttons in the grid */
    div.small-grid div.stButton > button {
        min-height: 0px !important;  /* KILL THE GIANT HEIGHT */
        height: auto !important;
        padding: 15px !important;
        font-size: 16px !important;
        text-align: center !important;
        width: 100% !important;
        margin-top: 5px !important;
        box-shadow: none !important;
    }

    /* UNSELECTED (Dark Blue) */
    /* We reuse 'secondary' type but override the Bat style */
    div.small-grid div.stButton > button[kind="secondary"] {
        background-color: var(--box-bg) !important; 
        color: var(--text-mint) !important;         
        border: 2px solid var(--text-mint) !important;
        text-shadow: none !important; /* Remove Bat Shadow */
        border-radius: 8px !important;
    }

    /* SELECTED (Mint) */
    /* We reuse 'primary' type but override the Giant Box style */
    div.small-grid div.stButton > button[kind="primary"] {
        background-color: var(--text-mint) !important; 
        color: var(--text-dark) !important;            
        border: 2px solid var(--text-mint) !important;
        border-radius: 8px !important;
    }

    div.small-grid div.stButton > button:hover {
        transform: scale(1.02) !important;
        border-color: #ffffff !important;
    }

    /* Headings */
    h1, h2, h3 {
        color: var(--text-mint) !important;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 2px solid var(--text-mint);
        border-radius: 10px;
    }
    .stTextArea > div > div > textarea {
        min-height: 200px;
        font-size: 18px;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 1px solid var(--text-mint);
        border-radius: 8px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---

def create_selection_grid(options, category_key):
    """
    Creates a grid of clickable toggle buttons wrapped in 'small-grid'
    to prevent them from becoming giant.
    """
    # WRAPPER: This div class triggers the CSS overrides above
    st.markdown('<div class="small-grid">', unsafe_allow_html=True)
    
    cols_per_row = 4
    rows = [options[i:i + cols_per_row] for i in range(0, len(options), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for idx, option in enumerate(row):
            full_key = f"{category_key}_{option}"
            is_selected = st.session_state.selections.get(full_key, False)
            
            # Logic: If selected, be 'primary' (Mint). If not, be 'secondary' (Dark).
            # The CSS 'small-grid' class ensures they stay small regardless of type.
            btn_type = "primary" if is_selected else "secondary"
            
            with cols[idx]:
                if st.button(option, key=full_key, type=btn_type):
                    toggle_selection(full_key)
                    st.rerun()
                    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PAGE FUNCTIONS ---
lorem_short = "Short placeholder text to describe this section briefly."

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
            navigate_to('helping_hand')

def helping_hand_page():
    if st.button("🦇", type="secondary"):
        navigate_to('ideas')
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Describe your project</h1>", unsafe_allow_html=True)

    placeholders = ["Let's hear your idea!", "Let's find you your best help!", "Let's find you your partner!"]
    selected_placeholder = random.choice(placeholders)

    assisted_mode = st.toggle("Assisted Mode")
    st.markdown("<br>", unsafe_allow_html=True)

    if not assisted_mode:
        st.text_area("Your Idea", placeholder=selected_placeholder, label_visibility="collapsed")
    else:
        # 1. Project Type
        with st.expander("1. What kind of project is it?", expanded=True):
            options = ["Quick fix", "Big idea", "Long Term", "Community", "Tech", "Art", "Else"]
            create_selection_grid(options, "type")

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. Resources
        with st.expander("2. What resources do you need?", expanded=True):
            resources = [
                "Hammer", "Workspace", "Drill", "3D Printer", 
                "Paint", "Wood", "Metal", "Soldering Iron", 
                "Sewing Machine", "Laptop", "Vehicle", "Ladder"
            ]
            create_selection_grid(resources, "resource")
            
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. Meeting Preference
        with st.expander("3. Do you want to meet face to face?", expanded=True):
            create_selection_grid(["Yes", "No"], "meeting")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Submit Request", type="tertiary"):
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
