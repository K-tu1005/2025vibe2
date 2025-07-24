import streamlit as st
import random
import time
import os

# 설정
GRID_SIZE = 3
GAME_DURATION = 20  # seconds
MOLE_DURATION = 1.0  # seconds
MOLE_IMAGE = "mole.png"  # 두더지 이미지 파일 (같은 폴더에 있어야 함)

st.set_page_config(page_title="Whack-a-Mole", page_icon="🐹")
st.title("🎯 Whack-a-Mole")
st.caption("Click the mole as fast as you can!")

# 이미지 확인
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

# 게임 시작 함수
def start_game():
    st.session_state.game_running = True
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.last_mole_time = 0
    st.session_state.mole_position = (
        random.randint(0, GRID_SIZE - 1),
        random.randint(0, GRID_SIZE - 1)
    )

# 게임 종료 함수
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

        # 일정 시간마다 두더지 위치 변경
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            st.session_state.mole_position = (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            )
            st.session_state.last_mole_time = time.time()

        # 그리드 생성
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                with cols[j]:
                    if (i, j) == st.session_state.mole_position:
                        if st.button("", key=f"mole-{i}-{j}"):
                            st.session_state.score += 1
                            st.session_state.last_mole_time = 0
                        st.image(MOLE_IMAGE, use_column_width=True)
                    else:
                        st.button(" ", key=f"empty-{i}-{j}")

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
