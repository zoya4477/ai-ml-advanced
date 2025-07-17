import streamlit as st
import os

# Mock RAGChatbot class 
class RAGChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.knowledge_base = []
        self.conversation_history = []

    def load_knowledge_base(self, docs):
        self.knowledge_base.extend(docs)
        return f"{len(docs)} document(s) added to the knowledge base."

    def generate_response(self, prompt):
        # Dummy response using past knowledge
        response = f"🤖 This is a dummy response to your question: '{prompt}'\n\n"
        if self.knowledge_base:
            response += "\n📚 Based on knowledge:\n" + self.knowledge_base[0][:300] + "..."
        else:
            response += "\n⚠️ (No knowledge base loaded yet.)"
        return response

    def reset_conversation(self):
        self.conversation_history = []

# Load your API key (you can ignore this in mock version)
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "API KEY")


def create_streamlit_app():
    st.set_page_config(
        page_title="Context-Aware RAG Chatbot",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 Context-Aware RAG Chatbot")
    st.markdown("Upload documents and chat with your AI assistant!")

    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = RAGChatbot(CLAUDE_API_KEY)

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Sidebar for uploading documents
    with st.sidebar:
        st.header("📚 Knowledge Base")

        uploaded_files = st.file_uploader(
            "Upload documents",
            type=['txt'],
            accept_multiple_files=True
        )

        if uploaded_files:
            if st.button("Process Documents"):
                with st.spinner("Processing documents..."):
                    texts = []
                    for uploaded_file in uploaded_files:
                        content = uploaded_file.read()
                        try:
                            text = content.decode("utf-8")
                        except UnicodeDecodeError:
                            text = content.decode("latin1")  # Fallback for other encodings
                        texts.append(text)

                    result = st.session_state.chatbot.load_knowledge_base(texts)
                    st.success(result)

        if st.button("Clear Conversation"):
            st.session_state.chatbot.reset_conversation()
            st.session_state.messages = []
            st.rerun()

    # Main chat interface
    st.header("💬 Chat")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.generate_response(prompt)
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


# Run the Streamlit app
if __name__ == "__main__":
    create_streamlit_app()
