import streamlit as st

# Chat area section
st.title('Chat Area')

# Placeholder for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history
for message in st.session_state['chat_history']:
    st.write(message)

# User input
user_input = st.text_input('Type your message:')

# Button to send the message
if st.button('Send'):
    if user_input:
        # Add the new message to chat history
        st.session_state['chat_history'].append(f'User: {user_input}')
        # Simulated response
        st.session_state['chat_history'].append('Bot: This is a simulated response.')
        # Clear input
        st.experimental_rerun()pip install -r requirements.1