import streamlit as st

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(page_title="ROBIN", layout="wide", page_icon="🐦")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. CUSTOM CSS (Dark Blue & Mint Design) ---
# This CSS transforms standard buttons into "Cards" and sets the color scheme.
st.markdown("""
    <style>
    /* Global Color Variables */
    :root {
        --primary-color: #0d1b2a; /* Darkest Blue */
        --secondary-color: #1b263b; /* Medium Dark Blue */
        --accent-color: #41ead4;   /* Mint Green */
        --text-color: #e0e1dd;     /* Off-white/Grey */
    }

    /* Main App Background */
    .stApp {
        background-color: var(--primary-color);
        color: var(--text-color);
    }

    /* Custom "Box" Styling for Buttons */
    /* We target the buttons inside the main columns to look like cards */
    div.stButton > button {
        background-color: var(--secondary-color);
        color: var(--accent-color);
        border: 2px solid var(--accent-color);
        border-radius: 15px;
        padding: 40px 20px;
        font-size: 24px;
        font-weight: 600;
        width: 100%;
        height: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    /* Hover effect for the boxes */
    div.stButton > button:hover {
        background-color: var(--accent-color);
        color: var(--primary-color);
        border-color: var(--text-color);
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(65, 234, 212, 0.4);
    }

    /* Headings */
    h1, h2, h3 {
        color: var(--accent-color) !important;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Text styling */
    p {
        color: var(--text-color);
        font-size: 1.1rem;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: var(--secondary-color);
        color: var(--accent-color);
        border-radius: 10px;
    }
    
    /* Hide default menu for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- 3. PAGE FUNCTIONS ---

def home_page():
    st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 50px;'>ROBIN</h1>", unsafe_allow_html=True)
    
    # Use columns to create the layout for the 3 boxes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # The button returns True when clicked
        if st.button("Give us your Idea! 💡"):
            navigate_to('ideas')
            
    with col2:
        if st.button("How ROBIN works! ⚙️"):
            navigate_to('how_it_works')
            
    with col3:
        if st.button("Keep Track of Ideas! 🚀"):
            navigate_to('success')

def ideas_page():
    # Back button (smaller, simpler style logic could be applied here if needed)
    if st.button("← Back to Home"):
        navigate_to('home')
        
    st.markdown("---")
    
    # Big Font Header
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 60px;'>How can we help you with your project?</h1>", unsafe_allow_html=True)
    
    # Center Layout using columns. 
    # Using empty columns on the side to center the middle two.
    _, mid1, mid2, _ = st.columns([1, 2, 2, 1])
    
    with mid1:
        if st.button("I need financial support! 💰"):
            st.toast("Financial support path selected!") # Placeholder action
            
    with mid2:
        if st.button("I need a helping hand! 🤝"):
            st.toast("Volunteer support path selected!") # Placeholder action

def how_it_works_page():
    if st.button("← Back to Home"):
        navigate_to('home')
    
    st.markdown("---")
    st.title("How ROBIN Works")
    
    # Placeholder content
    sections = [
        {
            "title": "1. Submission Phase",
            "subtitle": "Getting your thoughts on paper",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        },
        {
            "title": "2. The Review Process",
            "subtitle": "Quality assurance and feasibility",
            "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
        {
            "title": "3. Execution & Launch",
            "subtitle": "Bringing the dream to reality",
            "text": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo."
        }
    ]
    
    for section in sections:
        st.header(section["title"])
        st.subheader(section["subtitle"])
        with st.expander(f"Read more about {section['title']}"):
            st.write(section["text"])
        st.markdown("<br>", unsafe_allow_html=True) # Spacing

def success_page():
    if st.button("← Back to Home"):
        navigate_to('home')
        
    # Spacer to push title down slightly
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Big Title as requested
    st.markdown("<h1 style='text-align: center; font-size: 5rem;'>Our Success Stories</h1>", unsafe_allow_html=True)

# --- 4. MAIN APP CONTROLLER ---

if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'ideas':
    ideas_page()
elif st.session_state.page == 'how_it_works':
    how_it_works_page()
elif st.session_state.page == 'success':
    success_page()
