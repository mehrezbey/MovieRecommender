import streamlit as st
from questions import Questions
from utils import return_poster
from expert_system import selectMovies
import pandas as pd
import time

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = -1
    st.session_state.path=""

if "responses" not in st.session_state:
    st.session_state.responses = [""] * 10 

if "submitted" not in st.session_state:
    st.session_state.submitted = False

questions = Questions.questions

# Handler for buttons
def start_quiz():
    st.session_state.current_question = 0
    
def navigate(offset):
    st.session_state.current_question += offset
    
def show_result():
    st.session_state.submitted = True
    selectMovies(st.session_state["responses"])

def try_again():
    st.session_state.current_question = -1
    st.session_state.responses = [""] * 10 
    st.session_state.submitted = False
def another_one():
    time.sleep(0.5)

# Welcome Page
if st.session_state.current_question == -1 and not st.session_state.submitted:
    st.title("Welcome to Movie Recommander!")
    st.write("You can’t decide between thousands of movies available for streaming?")
    st.image(
        "https://media1.tenor.com/m/zDZRlH-tT1sAAAAd/despicable-me-minions.gif",
        width=390
    )
    st.write("Answer 7 questions and let us do the work!. Click **Start** to begin!")
    left, middle, right = st.columns(3)
    middle.button("Start",on_click=start_quiz,icon="😃")

        
# Questions Page
elif 0 <= st.session_state.current_question < len(questions) and not st.session_state.submitted:
    current_question = st.session_state.current_question
    st.title(f"Question {current_question + 1}: {questions[current_question]['question']}")
    
    response = st.radio (
        "Your Answer:",
        options=questions[current_question]["options"],
        index=questions[current_question]["options"].index(st.session_state.responses[current_question])
        if st.session_state.responses[current_question] in questions[current_question]["options"]
        else 0,
    )

    # Update the response in session state
    st.session_state.responses[current_question] = response

    # Navigation buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if current_question > 0:
            st.button("Back", on_click=navigate, args=(-1,))

    with col2:
        if current_question < len(questions) - 1:
            st.button("Next", on_click=navigate, args=(1,))

    with col3:
        if current_question == len(questions) - 1:
            st.button("Submit",on_click=show_result)

# Results Page
elif st.session_state.submitted:
    res = pd.read_csv("data/output.csv")
    if not res.empty:
        row = res.sample(n=1).to_dict(orient="records")[0]
        st.session_state.path =return_poster(row["id"])

        st.title("Recommended for you 😎:")
        st.divider()
        left, middle = st.columns(2)

        left.title(row["original_title"])
        left.image(
            st.session_state.path,
            width=300,
            caption=row["tagline"]
        )

        middle.write("**Overview:** " + row["overview"])
        middle.write("**Directed By:** " + row["director"])
        middle.write("**Cast:** " + row["cast"])
        middle.write("**Release Date:** " + row["release_date"])
        st.button("Try Again !", on_click=try_again)
        if left.button(" Another one ↻",on_click=another_one):
            row = res.sample(n=1).to_dict(orient="records")[0]
            st.session_state.path = return_poster(row["id"])
    else:
        st.title("Oops!😔")
        st.title("Sorry We Did Not Find Any Movie According To Your Preferences!")
        st.divider()
        st.button("Try Again !", on_click=try_again)