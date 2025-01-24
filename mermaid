%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#FFC107'}}}%%
graph TD
    A[ユーザー] -->|PDFアップロード| B[Streamlit UI]
    B --> C{PDF処理モジュール}
    C -->|PyPDF2で解析| D[テキスト抽出]
    D -->|LangChain TextSplitter| E[チャンク分割]
    E --> F{ベクトルDB構築}
    F -->|OpenAI Embeddings| G[ベクトル化]
    G -->|FAISS| H[(ベクトルDB保存)]
    
    A -->|質問入力| I[チャットインターフェース]
    I --> J{LangChain QAシステム}
    J -->|ベクトル検索| H
    J -->|OpenAI LLM| K[回答生成]
    K -->|結果返却| I
    
    subgraph バックエンド処理
        C
        D
        E
        F
        G
        J
        K
    end
    
    subgraph データストレージ
        H
    end
    
    style A fill:#4CAF50,stroke:#388E3C
    style B fill:#2196F3,stroke:#1976D2
    style I fill:#2196F3,stroke:#1976D2
    style C fill:#FF5722,stroke:#F4511E
    style J fill:#FF5722,stroke:#F4511E
    style H fill:#9C27B0,stroke:#7B1FA2