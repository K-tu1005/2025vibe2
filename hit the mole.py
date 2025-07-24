import streamlit as st
import random
import time

st.set_page_config(page_title="Whack-a-Mole Game", page_icon="🐹")

st.title("🐹 Whack-a-Mole Game")
st.write("Click the mole before it disappears!")

# 게임 설정
GRID_SIZE = 3
GAME_DURATION = 20  # seconds
MOLE_DURATION = 1.0  # seconds per mole

# 세션 상태 초기화
if "game_running" not in st.session_state:
    st.session_state.game_running = False
    st.session_state.start_time = 0.0
    st.session_state.score = 0
    st.session_state.mole_position = (0, 0)
    st.session_state.last_mole_time = 0.0

# 게임 시작 함수
def start_game():
    st.session_state.game_running = True
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.mole_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.last_mole_time = time.time()

# 게임 종료 함수
def end_game():
    st.session_state.game_running = False

# 시작 버튼
if not st.session_state.game_running:
    if st.button("🎮 Start Game"):
        start_game()

# 게임 실행 중일 때
if st.session_state.game_running:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(GAME_DURATION - elapsed)

    if remaining > 0:
        st.markdown(f"⏱️ **Time Left:** `{remaining}` seconds &nbsp;&nbsp;&nbsp; 🎯 **Score:** `{st.session_state.score}`")

        # 두더지 위치 갱신 (MOLE_DURATION이 지났을 때)
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            st.session_state.mole_position = (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            )
            st.session_state.last_mole_time = time.time()

        # 버튼 그리드 출력
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                if (i, j) == st.session_state.mole_position:
                    if cols[j].button("🐹", key=f"mole-{i}-{j}-{time.time()}"):
                        st.session_state.score += 1
                        st.session_state.last_mole_time = 0.0  # 즉시 새 두더지
                else:
                    cols[j].button(" ", key=f"empty-{i}-{j}-{time.time()}")
    else:
        # 게임 종료
        end_game()
        st.success(f"⏱️ Time's up! Final Score: `{st.session_state.score}`")
        if st.button("🔁 Play Again"):
            start_game()
