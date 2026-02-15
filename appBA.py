import streamlit as st

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(page_title="ROBIN", layout="wide", page_icon="🐦")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. CUSTOM CSS (White, Dark Blue & Mint) ---
st.markdown("""
    <style>
    /* Global Color Variables */
    :root {
        --main-bg-color: #ffffff;      /* White Background */
        --box-color: #0d1b2a;          /* Dark Blue for the Boxes */
        --text-color-main: #0d1b2a;    /* Dark Blue for page text */
        --text-color-box: #ffffff;     /* White text inside the boxes */
        --accent-color: #41ead4;       /* Mint Green for borders/accents */
    }

    /* Main App Background */
    .stApp {
        background-color: var(--main-bg-color);
        color: var(--text-color-main);
    }

    /* Custom "Box" Styling for Buttons */
    div.stButton > button {
        background-color: var(--box-color);
        color: var(--text-color-box);
        border: 2px solid var(--accent-color); /* Mint border */
        border-radius: 15px;
        padding: 40px 20px;
        font-size: 24px;
        font-weight: 600;
        width: 100%;
        height: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Hover effect for the boxes */
    div.stButton > button:hover {
        background-color: var(--accent-color); /* Turn Mint on hover */
        color: var(--box-color);               /* Text turns Dark Blue */
        border-color: var(--box-color);
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.2);
    }

    /* Headings (H1, H2, H3) */
    h1, h2, h3 {
        color: var(--text-color-main) !important; /* Dark Blue Headings */
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Paragraph text */
    p {
        color: var(--text-color-main);
        font-size: 1.1rem;
    }

    /* Expander styling (for the FAQ section) */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        color: var(--text-color-main);
        border-radius: 10px;
        font-weight: bold;
    }
    
    /* Hide default menu for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- 3. PAGE FUNCTIONS ---

def home_page():
    # Title in Dark Blue
    st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 50px;'>ROBIN</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Give us your Idea! 💡"):
            navigate_to('ideas')
            
    with col2:
        if st.button("How ROBIN works! ⚙️"):
            navigate_to('how_it_works')
            
    with col3:
        if st.button("Keep Track of Ideas! 🚀"):
            navigate_to('success')

def ideas_page():
    # Simple Back button
    if st.button("← Back to Home"):
        navigate_to('home')
        
    st.markdown("---")
    
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 60px;'>How can we help you with your project?</h1>", unsafe_allow_html=True)
    
    _, mid1, mid2, _ = st.columns([1, 2, 2, 1])
    
    with mid1:
        if st.button("I need financial support! 💰"):
            st.toast("Financial support selected!") 
            
    with mid2:
        if st.button("I need a helping hand! 🤝"):
            st.toast("Volunteer support selected!") 

def how_it_works_page():
    if st.button("← Back to Home"):
        navigate_to('home')
    
    st.markdown("---")
    st.title("How ROBIN Works")
    
    sections = [
        {
            "title": "1. Submission Phase",
            "subtitle": "Getting your thoughts on paper",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        },
        {
            "title": "2. The Review Process",
            "subtitle": "Quality assurance and feasibility",
            "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
        },
        {
            "title": "3. Execution & Launch",
            "subtitle": "Bringing the dream to reality",
            "text": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium."
        }
    ]
    
    for section in sections:
        st.header(section["title"])
        st.subheader(section["subtitle"])
        with st.expander(f"Read more about {section['title']}"):
            st.write(section["text"])
        st.markdown("<br>", unsafe_allow_html=True)

def success_page():
    if st.button("← Back to Home"):
        navigate_to('home')
        
    st.markdown("<br><br>", unsafe_allow_html=True)
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
