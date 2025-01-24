import streamlit as st
from modules.pdf_processor import process_pdf
from modules.vector_db import create_vector_store
from modules.chat_interface import setup_qa_chain
from config.settings import Settings


# 初期化処理
def initialize_app():
    if not Settings.OPENAI_API_KEY:
        st.error("APIキーが設定されていません")
        st.stop()


# UIレンダリング
def render_interface():
    st.title("PDFチャットアシスタント")
    uploaded_file = st.file_uploader("PDFをアップロード", type="pdf")

    # チャット履歴管理
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # メッセージ表示
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 入力処理
    if prompt := st.chat_input("質問を入力"):
        handle_user_input(prompt, uploaded_file)


# 入力処理関数
def handle_user_input(prompt, uploaded_file):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("処理中..."):
        try:
            texts = process_pdf(uploaded_file)
            vector_store = create_vector_store(texts)
            qa_chain = setup_qa_chain(vector_store)
            response = qa_chain(prompt)

            answer = f"{response['result']}\n\n出典ページ: {[doc.metadata['page']+1 for doc in response['source_documents']]}"

            with st.chat_message("assistant"):
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            st.error(f"エラー発生: {str(e)}")


if __name__ == "__main__":
    initialize_app()
    render_interface()
