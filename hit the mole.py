import streamlit as st
import random
import time

st.set_page_config(page_title="Whack-a-Mole", page_icon="🐹")

st.title("🐹 Whack-a-Mole Game")
st.write("Click the mole before it disappears!")

# 설정값
GRID_SIZE = 3
GAME_DURATION = 20  # seconds
MOLE_DURATION = 1.0  # seconds per mole
MOLE_IMAGE_PATH = "mole.png"  # 이미지 파일 경로 (같은 폴더에 있어야 함)

# 세션 상태 초기화
if "game_running" not in st.session_state:
    st.session_state.game_running = False
    st.session_state.start_time = 0.0
    st.session_state.score = 0
    st.session_state.mole_position = (0, 0)
    st.session_state.last_mole_time = 0.0
    st.session_state.score_history = []
    st.session_state.high_score = 0  # 최고 점수 저장

# 게임 시작 함수
def start_game():
    st.session_state.game_running = True
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.mole_position = (
        random.randint(0, GRID_SIZE - 1),
        random.randint(0, GRID_SIZE - 1),
    )
    st.session_state.last_mole_time = time.time()

# 게임 종료 함수
def end_game():
    st.session_state.game_running = False
    current_score = st.session_state.score
    st.session_state.score_history.append(current_score)
    if current_score > st.session_state.high_score:
        st.session_state.high_score = current_score

# 게임 시작 버튼
if not st.session_state.game_running:
    if st.button("🎮 Start Game"):
        start_game()

# 게임 실행 중
if st.session_state.game_running:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(GAME_DURATION - elapsed)

    if remaining > 0:
        st.markdown(f"⏱️ **Time Left:** `{remaining}` seconds &nbsp;&nbsp;&nbsp; 🎯 **Score:** `{st.session_state.score}`")

        # 두더지 위치 갱신
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            st.session_state.mole_position = (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1),
            )
            st.session_state.last_mole_time = time.time()

        # 버튼 그리드 표시
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                key = f"{i}-{j}-{time.time()}"
                if (i, j) == st.session_state.mole_position:
                    with cols[j]:
                        clicked = st.button(" ", key=key)
                        st.image(MOLE_IMAGE_PATH, width=100)
                        if clicked:
                            st.session_state.score += 1
                            st.session_state.last_mole_time = 0.0
                else:
                    cols[j].button(" ", key=key)
    else:
        # 게임 종료 처리
        end_game()
        st.success(f"⏱️ Time's up! Final Score: `{st.session_state.score}`")

        # 최고 점수
        st.markdown(f"🏆 **High Score:** `{st.session_state.high_score}`")

        # 점수 히스토리 표시
        if st.session_state.score_history:
            st.markdown("## 📝 Score History")
            for idx, score in enumerate(reversed(st.session_state.score_history[-5:]), 1):
                st.markdown(f"**Game {idx}:** `{score}` points")

        if st.button("🔁 Play Again"):
            start_game()
