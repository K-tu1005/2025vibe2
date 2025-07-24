import streamlit as st
import random
import time

st.set_page_config(page_title="두더지 잡기 게임", page_icon="🪓")

st.title("🪓 두더지 잡기 게임")
st.write("랜덤으로 나타나는 두더지를 제한 시간 내에 클릭해서 잡으세요!")

# 게임 세팅
GRID_SIZE = 3
GAME_DURATION = 20  # 초
MOLE_DURATION = 1.0  # 두더지가 한 칸에 머무는 시간(초)

# 세션 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = None
    st.session_state.score = 0
    st.session_state.mole_position = (0, 0)
    st.session_state.last_mole_time = 0.0

# 게임 시작 버튼
if st.button("게임 시작"):
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.experimental_rerun()

# 게임 중일 때
if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(GAME_DURATION - elapsed)

    if remaining > 0:
        st.markdown(f"⏰ 남은 시간: `{remaining}초` &nbsp;&nbsp;&nbsp; 🎯 점수: `{st.session_state.score}`")
        
        # 두더지 위치 갱신
        if time.time() - st.session_state.last_mole_time > MOLE_DURATION:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            st.session_state.mole_position = (row, col)
            st.session_state.last_mole_time = time.time()

        # 버튼 그리드
        for i in range(GRID_SIZE):
            cols = st.columns(GRID_SIZE)
            for j in range(GRID_SIZE):
                if (i, j) == st.session_state.mole_position:
                    if cols[j].button("두더지!", key=f"{i}-{j}-{time.time()}"):
                        st.session_state.score += 1
                        st.session_state.last_mole_time = 0  # 다음 두더지를 빠르게 띄우기 위해
                else:
                    cols[j].button(" ", key=f"{i}-{j}-empty")
    else:
        st.success(f"⏱️ 게임 종료! 최종 점수: `{st.session_state.score}`점")
        if st.button("다시 하기"):
            st.session_state.start_time = None
            st.session_state.score = 0
            st.session_state.mole_position = (0, 0)
            st.experimental_rerun()
else:
    st.info("👆 위의 '게임 시작' 버튼을 눌러주세요!")
