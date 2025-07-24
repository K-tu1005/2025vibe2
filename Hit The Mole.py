import streamlit as st
import random
import time
import os

# 설정
GRID_SIZE = 3
GAME_DURATION = 20
MOLE_DURATION = 1.0
MOLE_IMAGE = "mole.png"
MOLE_IMAGE_SIZE = 100  # px, 이미지와 버튼 크기를 일치시킴

st.set_page_config(page_title="Whack-a-Mole", page_icon="🐹", layout="centered")
st.title("🎯 Whack-a-Mole")

# 이미지 파일 확인
if not os.path.exists(MOLE_IMAGE):
    st.warning("⚠️ mole.png 파일이 프로젝트 폴더에 없습니다!")
    st.stop()

# 세션 상태 초기화
if "game_running" not in st.session_state:
    st.session_state.game_running = False
    st.session_state.score = 0
    st.session_state.start_time = 0
    st.session_state.mole_position = (0, 0)
    st.session_state.last_mole_time = 0
    st.session_state.high_score = 0
    st.session_state.score_history = []

def start_game():
    st.session_state.game_running = True
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.last_mole_time = 0
    st.session_state.mole_position = (
        random.randint(0, GRID_SIZE - 1),
        random.randint(0, GRID_SIZE - 1)
    )

def end_game():
    st.session_state.game_running = False
    final_score = st.session_state.score
    st.session_state.score_history.append(final_score)
    if final_score > st.session_state.high_score:
        st.session_state.high_score = final_score

if not st.session_state.game_running:
    if st.button("🎮 Start Game"):
        start_game()

if st.session_state.game_running:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(GAME_DURATION - elapsed)

    if remaining > 0:
        st.markdown(f"⏱️ **Time Left:** `{remaining}` seconds")
        st.markdown(f"🏹 **Score:** `{st.session_state.score}`")

        # 두더지 위치 갱신
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            st.session_state.mole_position = (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            )
            st.session_state.last_mole_time = time.time()

        # 게임판 그리드
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                with cols[j]:
                    if (i, j) == st.session_state.mole_position:
                        # 두더지 클릭 이미지
                        clicked = st.button(
                            label="",
                            key=f"mole-{i}-{j}"
                        )
                        st.image(MOLE_IMAGE, width=MOLE_IMAGE_SIZE)

                        if clicked:
                            st.session_state.score += 1
                            st.session_state.last_mole_time = 0
                    else:
                        st.empty()  # 빈칸은 아무것도 없음

    else:
        end_game()
        st.success(f"🧨 Time's up! Your Score: `{st.session_state.score}`")
        st.markdown(f"🏆 **High Score:** `{st.session_state.high_score}`")

        if st.session_state.score_history:
            st.markdown("## 📊 Score History")
            for i, score in enumerate(reversed(st.session_state.score_history[-5:]), 1):
                st.markdown(f"**Game {i}:** `{score}` points")

        if st.button("🔁 Play Again"):
            start_game()
