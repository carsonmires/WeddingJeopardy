# streamlit_app.py
import streamlit as st

# ========= Data copied from your original script =========
categories = {
    "The Bride": {
        100: "What is Sara's favorite TV show?",
        200: "How tall is Sara?",
        300: "True or False: Sara made the first move on Zach?",
        400: "What is the first memorable gift Sara received from Zach?",
        500: "What exact date did Sara move to Texas?"
    },
    "The Couple": {
        100: "What restaurant did Sara and Zach meet at?",
        200: "What is Sara and Zach's anniversary?",
        300: "What is the height difference between Sara and Zach (in inches)?",
        400: "What is Sara and Zach's favorite thing to do together?",
        500: "How many children do Sara and Zach want to have?"
    },
    "The Bridesmaids": {
        200: "Where did Andre and Sara first meet?",
        201: "What is Jacqui and Sara's go-to car song?",
        202: "What was the first ever abandoned location Sara took Brina?",
        203: "What fandoms do Pohai and Sara have in common?",
        204: "How old was Michelle when Sara started colorguard?"
    },
    "The Groom": {
        100: "What is Zach's favorite sport?",
        200: "What is Zach's favorite thing about Sara?",
        300: "True or False: Zach is the better cook?",
        400: "What is one thing Zach does that annoys Sara?",
        500: "If Zach could swap with Sara for the day, what is one thing he would be excited to do?"
    }
}

answers = {
    "The Bride": {
        100: "Friends",
        200: "5'1",
        300: "True",
        400: "The necklace Sara wears everyday",
        500: "August 13th, 2016"
    },
    "The Couple": {
        100: "Whistle Britches",
        200: "March 8th, 2022",
        300: "17 inches",
        400: "Drinking margaritas and going Pokemon Go hunting",
        500: "2"
    },
    "The Bridesmaids": {
        200: "Black Gold rehearsal in 2016",
        201: "MCR - The Black Parade",
        202: "Profanity Houses",
        203: "3: Lord of the Rings, Harry Potter, Game of Thrones",
        204: "4 years old"
    },
    "The Groom": {
        100: "Basketball",
        200: "The way she cares about things",
        300: "False, unless he is cooking protein then it is true",
        400: "Sing annoying songs all day long",
        500: "Zach would hide in the smallest place ever and scare Sara"
    }
}

FINAL_JEOPARDY_QUESTION = 'What is the exact number of days Sara and Zach have known each other?'
FINAL_JEOPARDY_ANSWER = '1,265 to 1,292 days'
FINAL_JEOPARDY_VALUE = 1000  # match your Tk app

# ========= Helpers =========
def display_value(category, value):
    # Bridesmaids category always shows "$200" and scores as 200 in your Tk app
    return 200 if category == "The Bridesmaids" else value

def score_value(category, value):
    return 200 if category == "The Bridesmaids" else value

# ========= App state =========
if "team_a" not in st.session_state:
    st.session_state.team_a = 0
if "team_b" not in st.session_state:
    st.session_state.team_b = 0
if "answered" not in st.session_state:
    st.session_state.answered = set()  # (category, value) pairs
if "current_q" not in st.session_state:
    st.session_state.current_q = None  # (category, value)
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "final_mode" not in st.session_state:
    st.session_state.final_mode = False

st.set_page_config(page_title="Wedding Jeopardy 💍", layout="wide")
st.title("💍 Wedding Jeopardy")

# Sidebar scoreboard and controls
with st.sidebar:
    st.header("Scoreboard")
    col_a, col_b = st.columns(2)
    col_a.metric("Team A", st.session_state.team_a)
    col_b.metric("Team B", st.session_state.team_b)

    st.header("Controls")
    if st.button("Restart game"):
        st.session_state.team_a = 0
        st.session_state.team_b = 0
        st.session_state.answered = set()
        st.session_state.current_q = None
        st.session_state.show_answer = False
        st.session_state.final_mode = False
        st.experimental_rerun()

    st.markdown("---")
    if st.button("Final Jeopardy"):
        st.session_state.final_mode = True
        st.session_state.current_q = ("FINAL", "FINAL")
        st.session_state.show_answer = False

# ======= Board =======
board_cols = st.columns(len(categories))

for idx, (category, qa_map) in enumerate(categories.items()):
    with board_cols[idx]:
        st.subheader(category)
        for value in qa_map.keys():
            key = (category, value)
            disabled = key in st.session_state.answered or st.session_state.current_q == key
            label = f"${display_value(category, value)}"
            if st.button(label, disabled=disabled, key=f"btn_{category}_{value}"):
                st.session_state.current_q = key
                st.session_state.show_answer = False

# ======= Question/Answer panel =======
st.markdown("---")
panel = st.container()

def clear_current():
    st.session_state.current_q = None
    st.session_state.show_answer = False

with panel:
    # Final Jeopardy flow
    if st.session_state.final_mode and st.session_state.current_q == ("FINAL", "FINAL"):
        st.subheader("Final Jeopardy 💍")
        st.write(FINAL_JEOPARDY_QUESTION)
        c1, c2, c3, c4 = st.columns([1,1,1,2])
        if c1.button("Show answer"):
            st.session_state.show_answer = True
        if st.session_state.show_answer:
            st.info(f"**Answer:** {FINAL_JEOPARDY_ANSWER}")
            d1, d2, d3 = st.columns(3)
            if d1.button("Team A correct (+1000)"):
                st.session_state.team_a += FINAL_JEOPARDY_VALUE
                st.session_state.final_mode = False
                clear_current()
            if d2.button("None"):
                st.session_state.final_mode = False
                clear_current()
            if d3.button("Team B correct (+1000)"):
                st.session_state.team_b += FINAL_JEOPARDY_VALUE
                st.session_state.final_mode = False
                clear_current()
        if c4.button("Cancel Final"):
            st.session_state.final_mode = False
            clear_current()

    # Normal questions
    elif st.session_state.current_q:
        category, value = st.session_state.current_q
        q = categories[category][value]
        a = answers[category][value]
        st.subheader(f"Question — **{category}** for ${display_value(category, value)}")
        st.write(q)
        c1, c2, c3, c4 = st.columns([1,1,1,2])
        if c1.button("Show answer", key="show_ans"):
            st.session_state.show_answer = True

        if st.session_state.show_answer:
            st.info(f"**Answer:** {a}")
            d1, d2, d3 = st.columns(3)
            if d1.button("Team A correct"):
                st.session_state.team_a += score_value(category, value)
                st.session_state.answered.add((category, value))
                clear_current()
            if d2.button("None"):
                st.session_state.answered.add((category, value))
                clear_current()
            if d3.button("Team B correct"):
                st.session_state.team_b += score_value(category, value)
                st.session_state.answered.add((category, value))
                clear_current()

# ======= Footer =======
st.markdown("———")
st.caption("Built from your original Tkinter game. Streamlit version for easy web sharing.")
