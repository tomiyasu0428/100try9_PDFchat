import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# パス設定
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# 環境変数読み込み
load_dotenv(BASE_DIR / ".env")


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # 正しい変数名
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    TEMPERATURE = 0
