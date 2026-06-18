import streamlit as st
from modules.requirement_generator import generate_user_story
from modules.acceptance_criteria import generate_acceptance_criteria
from modules.email_drafter import draft_stakeholder_email

st.set_page_config(page_title="AI BA Workflow", page_icon="🤖", layout="wide")
st.title("🤖 End-to-End AI Business Analyst Workflow")
st.markdown("---")

st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox("Choose Model", ["gemini-2.5-flash (Free)", "gemini-2.5-pro (Better)"])
st.sidebar.info("✅ Using Google Gemini - Free Tier!")

requirement = st.text_area(
    "Enter your business requirement:",
    placeholder="Example: I want an e-commerce app where users can buy products...",
    height=120
)

if st.button("🚀 Run Complete BA Workflow", type="primary"):
    if requirement:
        with st.spinner("AI is analyzing and generating all modules... ⏳"):
            # 1. User Story
            user_story = generate_user_story(requirement, model_choice)
            st.session_state['user_story'] = user_story
            
            # 2. Acceptance Criteria
            ac = generate_acceptance_criteria(user_story)
            st.session_state['ac'] = ac
            
            # 3. Email
            email = draft_stakeholder_email(user_story, ac)
            st.session_state['email'] = email
            
        st.success("🎉 All Modules Generated Successfully!")
    else:
        st.warning("⚠️ Please enter a requirement first!")

st.markdown("---")

if 'user_story' in st.session_state:
    tab1, tab2, tab3 = st.tabs(["📝 1. User Story", "📋 2. Acceptance Criteria", "✉️ 3. Stakeholder Email"])
    
    with tab1:
        st.subheader("User Story Details")
        st.markdown(st.session_state['user_story'])
        
    with tab2:
        st.subheader("Detailed Acceptance Criteria (Given-When-Then)")
        st.markdown(st.session_state['ac'])
        
    with tab3:
        st.subheader("Drafted Email for Stakeholders")
        st.markdown(st.session_state['email'])
