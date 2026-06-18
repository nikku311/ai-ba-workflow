import streamlit as st
from modules import (
    generate_user_story,
    generate_acceptance_criteria,
    validate_story_completeness,
    draft_stakeholder_email,
    draft_meeting_minutes,
    get_email_template_options
)

# ============== PAGE CONFIG ==============
st.set_page_config(
    page_title="AI BA Workflow",
    page_icon="🤖",
    layout="wide",  # Poori screen use karega
    initial_sidebar_state="expanded"
)

# ============== CUSTOM CSS ==============
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .module-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        border-bottom: 2px solid #ff7f0e;
        padding-bottom: 0.5rem;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ============== SIDEBAR ==============
with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
    st.markdown("## 🤖 AI BA Workflow")
    st.markdown("---")
    
    # Navigation
    st.markdown("### 📍 Navigation")
    page = st.radio(
        "Select Module:",
        ["🏠 Home", "📝 User Stories", "✅ Acceptance Criteria", "📧 Email Drafting"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    model_choice = st.selectbox(
        "AI Model",
        ["gemini-1.5-flash (Free & Fast)", "gemini-1.5-pro (Better Quality)"]
    )
    
    st.markdown("---")
    st.info("💡 **Tip:** Har module ke liye alag-alag prompts optimized hain!")

# ============== HOME PAGE ==============
if page == "🏠 Home":
    st.markdown('<p class="main-header">Welcome to AI BA Workflow! 🚀</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 1rem; border-radius: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <h3>📝 Module 1</h3>
            <h4>User Story Generator</h4>
            <p>Requirements se professional user stories banao with story points & priority</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 1rem; border-radius: 1rem; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white;">
            <h3>✅ Module 2</h3>
            <h4>Acceptance Criteria</h4>
            <p>Given-When-Then format mein detailed ACs generate karo with edge cases</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 1rem; border-radius: 1rem; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white;">
            <h3>📧 Module 3</h3>
            <h4>Email Drafting</h4>
            <p>Professional stakeholder emails & meeting minutes banao</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="info-box">👈 Left sidebar se module select karo aur shuru karo!</p>', unsafe_allow_html=True)

# ============== MODULE 1: USER STORIES ==============
elif page == "📝 User Stories":
    st.markdown('<p class="module-header">📝 User Story Generator</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        requirement = st.text_area(
            "🎯 Business Requirement:",
            placeholder="Example: I need an e-commerce app where users can browse products, add to cart, and make payments...",
            height=120
        )
    
    with col2:
        st.markdown("**💡 Tips:**")
        st.markdown("""
        - Specific raho
        - User ka goal batao
        - Benefit mention karo
        - Constraints batao
        """)
    
    col_btn1, col_btn2, _ = st.columns([1, 1, 2])
    
    with col_btn1:
        generate_btn = st.button("🚀 Generate User Story", type="primary", use_container_width=True)
    
    with col_btn2:
        validate_btn = st.button("🔍 Validate Story", type="secondary", use_container_width=True)
    
    if generate_btn and requirement:
        with st.spinner("🤖 AI user story bana raha hai... ⏳"):
            result = generate_user_story(requirement, model_choice)
        
        st.markdown('<p class="success-box">✅ User Story Generated!</p>', unsafe_allow_html=True)
        st.markdown("### 📋 Output:")
        st.markdown(result)
        st.code(result, language="markdown")
        
        # Copy to clipboard button (workaround)
        st.download_button(
            "📥 Download as Text",
            result,
            file_name="user_story.txt",
            mime="text/plain"
        )
    
    elif validate_btn and requirement:
        with st.spinner("🔍 INVEST criteria check ho raha hai... ⏳"):
            validation = validate_story_completeness(requirement)
        
        st.markdown('<p class="success-box">🔍 Validation Report!</p>', unsafe_allow_html=True)
        st.markdown(validation)

# ============== MODULE 2: ACCEPTANCE CRITERIA ==============
elif page == "✅ Acceptance Criteria":
    st.markdown('<p class="module-header">✅ Acceptance Criteria Generator</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📝 From User Story", "🔄 Direct Input"])
    
    with tab1:
        user_story_input = st.text_area(
            "📋 Paste User Story here:",
            placeholder="As a [user], I want [goal] so that [benefit]...",
            height=150
        )
        
        additional_context = st.text_area(
            "💡 Additional Context (Optional):",
            placeholder="Technical constraints, specific validations, etc.",
            height=80
        )
        
        if st.button("✅ Generate ACs", type="primary"):
            if user_story_input:
                with st.spinner("🤖 Detailed ACs bana raha hai... ⏳"):
                    ac_result = generate_acceptance_criteria(user_story_input, additional_context)
                
                st.markdown('<p class="success-box">✅ Acceptance Criteria Generated!</p>', unsafe_allow_html=True)
                st.markdown(ac_result)
                st.code(ac_result, language="markdown")
                
                st.download_button(
                    "📥 Download ACs",
                    ac_result,
                    file_name="acceptance_criteria.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ Pehle user story paste karo!")
    
    with tab2:
        st.info("💡 Direct requirement se ACs generate karna - coming soon!")

# ============== MODULE 3: EMAIL DRAFTING ==============
elif page == "📧 Email Drafting":
    st.markdown('<p class="module-header">📧 Professional Email Drafting</p>', unsafe_allow_html=True)
    
    email_tab1, email_tab2 = st.tabs(["📨 Stakeholder Email", "📋 Meeting Minutes"])
    
    # ---- Tab 1: Stakeholder Email ----
    with email_tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            email_type = st.selectbox(
                "📧 Email Type:",
                options=get_email_template_options(),
                format_func=lambda x: x.replace("_", " ").title()
            )
            
            recipient = st.text_input(
                "👤 Recipient:",
                placeholder="e.g., Product Owner, Dev Team, Client"
            )
            
            tone = st.select_slider(
                "🎭 Tone:",
                options=["Formal", "Professional", "Friendly", "Urgent"],
                value="Professional"
            )
        
        with col2:
            subject_context = st.text_input(
                "📝 Subject/Context:",
                placeholder="e.g., Sprint 5 Status Update"
            )
            
            st.markdown("**Key Points:**")
            point1 = st.text_input("Point 1:", placeholder="Main update or request")
            point2 = st.text_input("Point 2:", placeholder="Additional info")
            point3 = st.text_input("Point 3:", placeholder="Action needed")
        
        key_points = [p for p in [point1, point2, point3] if p]
        
        if st.button("📨 Draft Email", type="primary"):
            if recipient and subject_context and key_points:
                with st.spinner("🤖 Professional email draft ho raha hai... ⏳"):
                    email_draft = draft_stakeholder_email(
                        email_type=email_type,
                        recipient=recipient,
                        subject_context=subject_context,
                        key_points=key_points,
                        tone=tone.lower()
                    )
                
                st.markdown('<p class="success-box">📨 Email Draft Ready!</p>', unsafe_allow_html=True)
                st.markdown("### 📧 Your Email:")
                st.markdown(email_draft)
                st.code(email_draft, language="markdown")
                
                st.download_button(
                    "📥 Download Email",
                    email_draft,
                    file_name=f"{email_type}_email.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ Recipient, Subject, aur at least 1 Key Point chahiye!")
    
    # ---- Tab 2: Meeting Minutes ----
    with email_tab2:
        meeting_title = st.text_input("📋 Meeting Title:", placeholder="Sprint Planning - Sprint 5")
        
        col1, col2 = st.columns(2)
        with col1:
            attendees = st.text_area(
                "👥 Attendees (comma separated):",
                placeholder="John Doe (PO), Jane Smith (Dev Lead), ...",
                height=80
            )
        with col2:
            agenda = st.text_area(
                "📌 Agenda:",
                placeholder="1. Sprint goals\n2. Story estimation\n3. Capacity planning",
                height=80
            )
        
        st.markdown("**🎯 Decisions Made:**")
        dec1 = st.text_input("Decision 1:")
        dec2 = st.text_input("Decision 2:")
        dec3 = st.text_input("Decision 3:")
        decisions = [d for d in [dec1, dec2, dec3] if d]
        
        st.markdown("**✅ Action Items:**")
        with st.container():
            cols = st.columns([3, 2, 2])
            with cols[0]: task1 = st.text_input("Task 1", key="t1")
            with cols[1]: owner1 = st.text_input("Owner", key="o1")
            with cols[2]: due1 = st.date_input("Due", key="d1")
            
            with cols[0]: task2 = st.text_input("Task 2", key="t2")
            with cols[1]: owner2 = st.text_input("Owner", key="o2")
            with cols[2]: due2 = st.date_input("Due", key="d2")
        
        action_items = []
        if task1 and owner1: action_items.append({"task": task1, "owner": owner1, "due_date": str(due1)})
        if task2 and owner2: action_items.append({"task": task2, "owner": owner2, "due_date": str(due2)})
        
        if st.button("📋 Generate Minutes", type="primary"):
            if meeting_title and attendees and decisions:
                with st.spinner("🤖 Meeting minutes bana raha hai... ⏳"):
                    minutes = draft_meeting_minutes(
                        meeting_title=meeting_title,
                        attendees=[a.strip() for a in attendees.split(",")],
                        agenda=agenda,
                        decisions=decisions,
                        action_items=action_items
                    )
                
                st.markdown('<p class="success-box">📋 Meeting Minutes Ready!</p>', unsafe_allow_html=True)
                st.markdown(minutes)
                st.code(minutes, language="markdown")
            else:
                st.warning("⚠️ Meeting Title, Attendees, aur Decisions chahiye!")

# ============== FOOTER ==============
st.markdown("---")
st.caption("🤖 Powered by Google Gemini | Built for Future BAs | Made with ❤️")