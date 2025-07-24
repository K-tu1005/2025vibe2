import streamlit as st
import random

st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎯")

st.title("🎯 숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자를 맞혀보세요!")

# 세션 상태 초기화
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

# 입력받기
guess = st.number_input("당신의 추측은?", min_value=1, max_value=100, step=1)

# 버튼 누르면 결과 확인
if st.button("맞춰보기") and not st.session_state.game_over:
    st.session_state.tries += 1
    if guess < st.session_state.target_number:
        st.warning("너무 작아요! 📉")
    elif guess > st.session_state.target_number:
        st.warning("너무 커요! 📈")
    else:
        st.success(f"정답입니다! 🎉 {st.session_state.tries}번 만에 맞췄어요!")
        st.session_state.game_over = True

# 다시 시작 버튼
if st.button("게임 다시 시작"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False
    st.experimental_rerun()
