def create_streamlit_app():
    st.set_page_config(
        page_title="Context-Aware RAG Chatbot",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Context-Aware RAG Chatbot")
    st.markdown("Upload documents and chat with your AI assistant!")
    
    # Initialize session state
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = RAGChatbot(CLAUDE_API_KEY)
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar for document upload
    with st.sidebar:
        st.header("📚 Knowledge Base")
        
        uploaded_files = st.file_uploader(
            "Upload documents",
            type=['txt', 'pdf'],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            if st.button("Process Documents"):
                with st.spinner("Processing documents..."):
                    # Save uploaded files temporarily
                    temp_paths = []
                    for uploaded_file in uploaded_files:
                        temp_path = f"temp_{uploaded_file.name}"
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.read())
                        temp_paths.append(temp_path)
                    
                    # Load into knowledge base
                    result = st.session_state.chatbot.load_knowledge_base(temp_paths)
                    st.success(result)
                    
                    # Clean up temp files
                    for temp_path in temp_paths:
                        os.remove(temp_path)
        
        if st.button("Clear Conversation"):
            st.session_state.chatbot.reset_conversation()
            st.session_state.messages = []
            st.rerun()
    
    # Chat interface
    st.header("💬 Chat")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.generate_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat
        st.session_state.messages.append({"role": "assistant", "content": response})

# Run the Streamlit app
if __name__ == "__main__":
    create_streamlit_app()