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

    /* ============================================================
       1. GLOBAL BUTTON COLORS (Applies to ALL buttons)
       This ensures the toggle logic (Blue <-> Mint) works everywhere.
       ============================================================ */
    
    /* DEFAULT STATE (Secondary) -> Dark Blue Box, Mint Text */
    div.stButton > button[kind="secondary"] {
        background-color: var(--box-bg) !important;
        color: var(--text-mint) !important;
        border: 2px solid var(--box-bg) !important; 
        border-radius: 15px !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* SELECTED/ACTIVE STATE (Primary) -> Mint Box, Dark Blue Text */
    div.stButton > button[kind="primary"] {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        border: 2px solid var(--text-mint) !important;
        border-radius: 15px !important;
    }

    /* HOVER STATE (For Secondary) -> Turns Mint on Hover */
    div.stButton > button[kind="secondary"]:hover {
        background-color: var(--text-mint) !important;
        color: var(--text-dark) !important;
        transform: translateY(-2px);
    }
    div.stButton > button[kind="secondary"]:hover p {
        color: var(--text-dark) !important;
    }

    /* ============================================================
       2. LAYOUT WRAPPER: BIG BOXES (.big-box)
       Forces buttons inside this wrapper to be HUGE (50vh).
       ============================================================ */
    div.big-box button {
        min-height: 50vh !important; /* The Big Height */
        height: 50vh !important;
        width: 100% !important;
        font-size: 24px !important;
        text-align: left !important;
        padding: 40px !important;
        white-space: pre-wrap !important; /* Allows text wrapping */
    }

    /* ============================================================
       3. LAYOUT WRAPPER: SMALL GRID (.small-grid)
       Forces buttons inside this wrapper to be SMALL (Normal).
       ============================================================ */
    div.small-grid button {
        min-height: 0px !important;
        height: auto !important;
        width: 100% !important;
        font-size: 16px !important;
        text-align: center !important;
        padding: 15px 10px !important;
        margin-top: 5px !important;
    }
    
    /* Ensure small grid borders look right */
    div.small-grid button[kind="secondary"] {
        border: 2px solid var(--text-mint) !important; /* Visible Mint Border for small boxes */
    }

    /* ============================================================
       4. LAYOUT WRAPPER: BAT NAVIGATION (.bat-nav)
       Specific styles for the Back Button.
       ============================================================ */
    div.bat-nav button {
        background-color: var(--text-mint) !important; /* Mint Background */
        width: auto !important;
        height: auto !important;
        min-height: 0px !important;
        padding: 5px 20px !important;
        
        /* The Black Bat Trick */
        color: transparent !important;
        text-shadow: 0 0 0 var(--text-dark) !important; /* Dark Blue Shadow = Black Bat */
        font-size: 40px !important;
        line-height: 40px !important;
    }
    
    div.bat-nav button:hover {
        background-color: #ffffff !important;
        transform: scale(1.1) !important;
    }

    /* ============================================================
       5. GENERAL UI (Inputs, Headings)
       ============================================================ */
    h1, h2, h3 { color: var(--text-mint) !important; font-family: 'Helvetica', sans-serif; }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: var(--box-bg);
        color: var(--text-mint);
        border: 2px solid var(--text-mint);
        border-radius: 10px;
    }
    .stTextArea > div > div > textarea { min-height: 200px; font-size: 18px; }
    
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

def big_card_button(col, label, key):
    """Renders a Big Box button inside a column."""
    with col:
        st.markdown('<div class="big-box">', unsafe_allow_html=True)
        # Type is secondary (Dark Blue) by default
        clicked = st.button(label, key=key, type="secondary")
        st.markdown('</div>', unsafe_allow_html=True)
    return clicked

def bat_button(key):
    """Renders the Bat Back Button."""
    st.markdown('<div class="bat-nav">', unsafe_allow_html=True)
    clicked = st.button("🦇", key=key)
    st.markdown('</div>', unsafe_allow_html=True)
    return clicked

def create_selection_grid(options, category_key):
    """Renders the grid of small toggle boxes."""
    st.markdown('<div class="small-grid">', unsafe_allow_html=True)
    
    cols_per_row = 4
    rows = [options[i:i + cols_per_row] for i in range(0, len(options), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for idx, option in enumerate(row):
            full_key = f"{category_key}_{option}"
            is_selected = st.session_state.selections.get(full_key, False)
            
            # LOGIC: 
            # If selected -> Type Primary (Mint)
            # If not selected -> Type Secondary (Dark Blue)
            # This allows the "Click to turn back" behavior.
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
    
    # We use the helper function to ensure the DIV wrapper applies correctly inside the column
    if big_card_button(col1, f"GIVE US YOUR IDEA\n\n{lorem_short}", "home_1"):
        navigate_to('ideas')
        
    if big_card_button(col2, f"HOW ROBIN WORKS\n\n{lorem_short}", "home_2"):
        navigate_to('how_it_works')
        
    if big_card_button(col3, f"KEEP TRACK OF SUCCESSFUL IDEAS\n\n{lorem_short}", "home_3"):
        navigate_to('success')

def ideas_page():
    if bat_button("back_ideas"):
        navigate_to('home')
        
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-bottom: 60px;'>HOW CAN WE HELP YOU WITH YOUR PROJECT?</h1>", unsafe_allow_html=True)
    
    _, mid1, mid2, _ = st.columns([0.5, 2, 2, 0.5])
    
    if big_card_button(mid1, f"I NEED FINANCIAL SUPPORT\n\n{lorem_short}", "idea_money"):
        st.toast("Financial Support Selected")
        
    if big_card_button(mid2, f"I NEED A HELPING HAND\n\n{lorem_short}", "idea_help"):
        navigate_to('helping_hand')

def helping_hand_page():
    if bat_button("back_help"):
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
    
    # Submit button - Reuse small grid styling so it isn't huge
    st.markdown('<div class="small-grid">', unsafe_allow_html=True)
    if st.button("Submit Request", type="primary", use_container_width=True):
        st.toast("Request Submitted Successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

def how_it_works_page():
    if bat_button("back_how"):
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
    if bat_button("back_success"):
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
