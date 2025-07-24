import streamlit as st
import random
import time
import os

# 설정
GRID_SIZE = 3
GAME_DURATION = 20  # 게임 시간 (초)
MOLE_DURATION = 0.9  # 두더지 지속 시간 (초)
MOLE_IMAGE = "mole.png"
MOLE_IMAGE_SIZE = 100  # 이미지 크기 (px)

# 페이지 설정
st.set_page_config(page_title="Whack-a-Mole", page_icon="🐹", layout="centered")
st.title("🎯 Whack-a-Mole Game")

# 이미지 확인
if not os.path.exists(MOLE_IMAGE):
    st.warning("⚠️ mole.png 파일이 프로젝트 폴더에 없습니다!")
    st.stop()

# 세션 초기화
if "game_running" not in st.session_state:
    st.session_state.update({
        "game_running": False,
        "score": 0,
        "start_time": 0.0,
        "mole_position": (0, 0),
        "last_mole_time": 0.0,
        "high_score": 0,
        "score_history": []
    })

def start_game():
    st.session_state.update({
        "game_running": True,
        "score": 0,
        "start_time": time.time(),
        "last_mole_time": 0.0,
        "mole_position": (
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1)
        )
    })

def end_game():
    st.session_state.game_running = False
    final_score = st.session_state.score
    st.session_state.score_history.append(final_score)
    if final_score > st.session_state.high_score:
        st.session_state.high_score = final_score

# 게임 시작 버튼
if not st.session_state.game_running:
    if st.button("🎮 Start Game"):
        start_game()

# 게임 실행 중
if st.session_state.game_running:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(GAME_DURATION - elapsed)

    if remaining > 0:
        st.markdown(f"⏱️ **Time Left:** `{remaining}` seconds")
        st.markdown(f"🏹 **Score:** `{st.session_state.score}`")

        # 두더지 갱신
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            st.session_state.mole_position = (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            )
            st.session_state.last_mole_time = time.time()

        # 게임판 그리기
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                with cols[j]:
                    if (i, j) == st.session_state.mole_position:
                        clicked = st.button(" ", key=f"mole-{i}-{j}")
                        st.image(MOLE_IMAGE, width=MOLE_IMAGE_SIZE)
                        if clicked:
                            st.session_state.score += 1
                            st.session_state.last_mole_time = 0
                    else:
                        st.markdown(f"<div style='height:{MOLE_IMAGE_SIZE}px'></div>", unsafe_allow_html=True)

    else:
        end_game()
        st.success(f"✅ Game Over! Final Score: `{st.session_state.score}`")
        st.markdown(f"🏆 **High Score:** `{st.session_state.high_score}`")

        if st.session_state.score_history:
            st.markdown("📈 **Recent Scores:**")
            for i, score in enumerate(reversed(st.session_state.score_history[-5:]), 1):
                st.markdown(f"- Game {i}: `{score}` pts")

        if st.button("🔁 Play Again"):
            start_game()
