import streamlit as st
import time

# Simulate user session
if 'user' not in st.session_state:
    st.session_state['user'] = None

# Try to capture name and email from URL
params = st.query_params
name = params.get('name')
email = params.get('email')

if name and email and not st.session_state['user']:
    st.session_state['user'] = {"name": name, "email": email}
    st.query_params.clear()

# Check login
if st.session_state['user'] is None:
    st.title("Login Required")

    login_url = "http://localhost:8000/login"
    
    if st.button("🔐 Login with Microsoft"):
        with st.spinner('Redirecting to Microsoft login...'):
            time.sleep(0.5)
            st.markdown(f'<meta http-equiv="refresh" content="0; url={login_url}">', unsafe_allow_html=True)
            st.stop()

    st.stop()

# 🔥 Sidebar: Welcome and Log Out
with st.sidebar:
    st.success(f"✅ Logged in as:\n\n{st.session_state['user']['name']}")
    st.write(st.session_state['user']['email'])
    
    if st.button("🚪 Log Out"):
        st.session_state['user'] = None
        st.success("Logged out successfully. Please login again.")
        time.sleep(1)
        st.rerun()

# Restrict by email domain
allowed_domain = "adlvlaw.com.au"

user_email = st.session_state['user']['email']
if not user_email.endswith(f"@{allowed_domain}"):
    st.error("🚫 Access denied. You must use a @yourcompany.com email address.")
    st.stop()

# --- Main App Content ---
st.title("🎯 Your Internal App")
st.write("Here is where your real app content will go!")