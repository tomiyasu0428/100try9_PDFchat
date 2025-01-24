# 100try9_PDFchat
# PDFチャットアシスタント

自然言語でPDFドキュメントと対話できるAIアシスタントアプリ

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)

## ✨ 特徴

- PDFの内容に対して自然言語で質問可能
- 回答とともに出典ページ番号を提示
- 複数ファイル横断検索対応
- リアルタイムチャットインターフェース
- 文脈を考慮した高精度検索

## 🛠 技術スタック

**バックエンド**  
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.0.350-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-API-grey)

**フロントエンド**  
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-FF4B4B)

**データベース**  
![FAISS](https://img.shields.io/badge/FAISS-1.8.0-yellowgreen)

📚 使用方法
PDFファイルをアップロード

解析完了まで待機（約10-30秒）

チャットボックスに質問を入力

回答と参照ページ番号を確認

🔧 トラブルシューティング
エラー	解決策
ModuleNotFoundError	requirements.txtの再インストール
API認証エラー	.envファイルの再確認
ページ番号不整合	PDFの再アップロード
🌟 今後の展望
画像含むPDF対応（OCR統合）

チーム共有機能

検索履歴保存機能

マルチ言語対応

🤝 貢献方法
リポジトリをフォーク

機能ブランチ作成 (git checkout -b feature/amazing-feature)

変更をコミット (git commit -m 'Add some amazing feature')

ブランチにプッシュ (git push origin feature/amazing-feature)

プルリクエスト作成