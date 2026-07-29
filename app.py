import streamlit as st
import google.generativeai as genai

# 스트림릿 클라우드에 숨겨둔 마스터 키를 자동으로 불러옵니다.
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = ""

if not api_key:
    st.warning("⚠️ API 키가 설정되지 않았습니다.")
    st.stop()

genai.configure(api_key=api_key)

# --- 이후 기존에 작성하셨던 앱 화면 및 대화 로직 코드들 ---
st.title("내 AI 코치 서비스")
# (하단에 기존 소장님의 앱 소스코드 이어붙이기)