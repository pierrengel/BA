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
       1. THE BIG BOXES (Home & Ideas Page)
       Targeting buttons inside the .big-box wrapper
       ========================================= */
    div.big-box > div.stButton > button {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: none !important;
        border-radius: 15px !important;
        
        font-size: 22px !important; 
        text-align: left !important;
        white-space: pre-wrap !important;
        font-family: 'Helvetica', sans-serif !important;
        
        width: 100% !important;
        height: 50vh !important;  /* FORCE HUGE HEIGHT */
        padding: 40px !important;
        margin-top: 20px !important;
        
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
        transition: all 0.2s ease-in-out !important;
    }

    div.big-box > div.stButton > button:hover {
        background-color: var(--text-mint) !important; 
        color: var(--text-dark) !important;            
        transform: translateY(-5px) !important;
    }
    
    /* Force text inside button to change color on hover */
    div.big-box > div.stButton > button:hover p {
        color: var(--text-dark) !important;
    }

    /* =========================================
       2. THE BAT BUTTON (Navigation)
       Targeting buttons inside the .nav-btn wrapper
       ========================================= */
    div.nav-btn > div.stButton > button {
        background-color: var(--text-mint) !important; /* MINT BACKGROUND */
        border: none !important;
        border-radius: 12px !important;
        
        /* BLACK BAT TRICK */
        color: transparent !important;  
        text-shadow: 0 0 0 var(--text-dark) !important; /* Dark Blue Silhouette */
        
        font-size: 40px !important;
        line-height: 40px !important;
        
        height: auto !important;
        width: auto !important;
        padding: 5px 15px !important;
        min-height: 0px !important;
    }
    
    div.nav-btn > div.stButton > button:hover {
        transform: scale(1.1) !important; 
        background-color: #ffffff !important; /* White on hover */
    }

    /* =========================================
       3. SELECTION GRID BOXES (Helping Hand Page)
       Targeting buttons inside the .option-box wrapper
       ========================================= */
    
    /* Unselected State */
    div.option-box > div.stButton > button {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: 2px solid var(--text-mint) !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        min-height: 60px !important; /* Fixed small height */
        height: auto !important;
        width: 100% !important;
        transition: all 0.1s ease !important;
    }
    
    /* Hover State */
    div.option-box > div.stButton > button:hover {
        transform: scale(1.02) !important;
        border-color: #ffffff !important;
    }

    /* Selected State (We use type="primary" to mark selected) */
    div.option-box > div.stButton > button[kind="primary"] {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        border: 2px solid var(--text-mint) !important;
    }

    /* =========================================
       4. SUBMIT BUTTON
       ========================================= */
    div.submit-btn > div.stButton > button {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 100% !important;
        padding: 12px !important;
        min-height: 0px !important;
    }
    
    div.submit-btn > div.stButton > button:hover {
        background-color: #ffffff !important;
        transform: scale(1.01) !important;
    }

    /* General Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 2px solid var(--text-mint);
        border-radius: 10px;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 1px solid var(--text-mint);
        border-radius: 8px;
    }

    /* Hide default menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---

def create_selection_grid(options, category_name):
    # Wrap the entire grid in the "option-box" class to keep them small
    st.markdown('<div class="option-box">', unsafe_allow_html=True)
    
    cols_per_row = 4
    rows = [options[i:i + cols_per_row] for i in range(0, len(options), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for idx, option in enumerate(row):
            option_key = f"{category_name}_{option}"
            is_selected = st.session_state.selections.get(option_key, False)
            btn_type = "primary" if is_selected else "secondary"
            
            with cols[idx]:
                # The button itself
                if st.button(option, key=option_key, type=btn_type):
                    toggle_selection(option_key)
                    st.rerun()
                    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PAGE FUNCTIONS ---

def home_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 20px;'>ROBIN</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # WRAPPER FOR BIG BOXES
    st.markdown('<div class="big-box">', unsafe_allow_html=True)
    
    with col1:
        label = f"GIVE US YOUR IDEA\n\nShort placeholder text."
        if st.button(label, key="home_1"):
            navigate_to('ideas')
            
    with col2:
        label = f"HOW ROBIN WORKS\n\nShort placeholder text."
        if st.button(label, key="home_2"):
            navigate_to('how_it_works')
            
    with col3:
        label = f"KEEP TRACK OF SUCCESSFUL IDEAS\n\nShort placeholder text."
        if st.button(label, key="home_3"):
            navigate_to('success')
            
    st.markdown('</div>', unsafe_allow_html=True)

def ideas_page():
    # WRAPPER FOR BAT BUTTON
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🦇", key="back_ideas"):
        navigate_to('home')
    st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-bottom: 60px;'>HOW CAN WE HELP YOU WITH YOUR PROJECT?</h1>", unsafe_allow_html=True)
    
    _, mid1, mid2, _ = st.columns([0.5, 2, 2, 0.5])
    
    # WRAPPER FOR BIG BOXES
    st.markdown('<div class="big-box">', unsafe_allow_html=True)
    with mid1:
        label = f"I NEED FINANCIAL SUPPORT\n\nShort placeholder text."
        if st.button(label, key="idea_money"):
            st.toast("Financial Support Selected")
            
    with mid2:
        label = f"I NEED A HELPING HAND\n\nShort placeholder text."
        if st.button(label, key="idea_help"):
            navigate_to('helping_hand')
    st.markdown('</div>', unsafe_allow_html=True)

def helping_hand_page():
    # WRAPPER FOR BAT BUTTON
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🦇", key="back_help"):
        navigate_to('ideas')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Describe your project</h1>", unsafe_allow_html=True)

    placeholders = ["Let's hear your idea!", "Let's find you your best help!", "Let's find you your partner!"]
    selected_placeholder = random.choice(placeholders)

    assisted_mode = st.toggle("Assisted Mode")
    st.markdown("<br>", unsafe_allow_html=True)

    if not assisted_mode:
        st.text_area("Your Idea", placeholder=selected_placeholder, label_visibility="collapsed", height=200)
    else:
        # 1. Project Type
        with st.expander("1. What kind of project is it?", expanded=True):
            options = ["Quick fix", "Big idea", "Long term", "Community", "Tech", "Art", "Else"]
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
    
    # WRAPPER FOR SUBMIT BUTTON
    st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
    if st.button("Submit Request"):
        st.toast("Request Submitted Successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

def how_it_works_page():
    # WRAPPER FOR BAT BUTTON
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🦇", key="back_how"):
        navigate_to('home')
    st.markdown('</div>', unsafe_allow_html=True)
    
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
    # WRAPPER FOR BAT BUTTON
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🦇", key="back_success"):
        navigate_to('home')
    st.markdown('</div>', unsafe_allow_html=True)
        
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
