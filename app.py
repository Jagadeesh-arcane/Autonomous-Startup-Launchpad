import streamlit as st
from src.main import run
from src.utils.pdf_generator import generate_business_plan_pdf

st.set_page_config(page_title="Autonomous Startup Launchpad", layout="wide")

st.title("🚀 Autonomous Startup Launchpad")
st.caption("Turn a startup idea into a business plan using autonomous AI agents")

# --- Session State ---
if "business_plan" not in st.session_state:
    st.session_state.business_plan = None

idea = st.text_area(
    "Enter your startup idea",
    placeholder="Example: A mobile app that helps small retail shop owners track daily sales using voice input",
    height=120,
)

col1, col2 = st.columns([1, 1])

with col1:
    generate_clicked = st.button("⚙️ Generate Business Plan")

with col2:
    reset_clicked = st.button("🔄 Reset")

# --- Generate ---
if generate_clicked:
    if not idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Agents are working..."):
            st.session_state.business_plan = run(idea)

# --- Reset ---
if reset_clicked:
    st.session_state.business_plan = None
    st.rerun()

# --- Display Output ---
if st.session_state.business_plan:
    st.divider()
    st.subheader("📄 Generated Business Plan")

    st.markdown(
        f"""
        <div style="max-height: 450px; overflow-y: auto; padding: 16px; border: 1px solid #ddd; border-radius: 6px;">
        <pre>{st.session_state.business_plan}</pre>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # --- PDF Download ---
    pdf_buffer = generate_business_plan_pdf(st.session_state.business_plan)

    st.download_button(
        label="⬇️ Download Business Plan as PDF",
        data=pdf_buffer,
        file_name="business_plan.pdf",
        mime="application/pdf",
    )
