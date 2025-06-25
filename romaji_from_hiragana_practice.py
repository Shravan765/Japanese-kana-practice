import streamlit as st
import pandas as pd
import random

#to fetch questions randomly from the csv_file
def get_questions_from_csv(csv_name:str):
    df = pd.read_csv(csv_name)
    full_hiragana_list = list(df["Hiragana"])
    full_romaji_list = list(df["Romaji"])

    questions_set = random.sample(range(len(full_romaji_list)) , 10)

    romaji_lis = [full_romaji_list[i] for i in questions_set]
    hiragana_lis = [full_hiragana_list[i] for i in questions_set]
    return romaji_lis, hiragana_lis

csv_file_name = "kana.csv"

#to ensure we only load if needed
#keys are written as say hiragana_list_5 to ensure different pages have different lists loaded
if "romaji_list_5" not in st.session_state or "hiragana_list_5" not in st.session_state:
    romaji_list , hiragana_list = get_questions_from_csv(csv_file_name)
    st.session_state.romaji_list_5 = romaji_list
    st.session_state.hiragana_list_5 = hiragana_list

romaji_list = st.session_state.romaji_list_5
hiragana_list = st.session_state.hiragana_list_5

st.write("### Let's start! \n\n\n\n")
st.write("##### Write the correct romaji (english representation) of the given hiragana! \n\n")
st.write("Press enter or click submit to check your answers 📝")

cnt = 1
keys_to_retrive_answers = [f"q{i}" for i in range(1,11)]
submitted = None
with st.form(key="quiz"):
    for kana in hiragana_list:
        question_string = str(cnt)+". "+kana+"  :  "
        st.text_input(question_string, key=f"q{cnt}")
        cnt+=1

    submitted = st.form_submit_button("Submit your answers")

if(submitted):
    answers = [st.session_state[key] for key in keys_to_retrive_answers]
    score:int = 0
    incorrect_answer_indexes = list()
    for i in range(len(answers)):
        if(answers[i].strip().lower() == romaji_list[i].strip().lower()):
            score+=1
        else:
            incorrect_answer_indexes.append(i)

    st.write("#### Your score : ", score, "✅")
    st.balloons()
    if(score == len(answers)):
        st.write("You made no mistakes! 🎯")
    else:
        st.write("#### You made the following mistakes ‼️")
        for i in incorrect_answer_indexes:
            if(answers[i] != ""):
                st.write("For ", hiragana_list[i], " , you wrote ", answers[i])
                st.write("The correct answer is ", romaji_list[i])
                st.write("\n\n")
            else:
                st.write("For ", hiragana_list[i], " , you wrote nothing")
                st.write("The correct answer is ", romaji_list[i])
                st.write("\n\n")
        
if(st.button("### Retry")):
    del st.session_state.romaji_list_5
    del st.session_state.hiragana_list_5
    for key in keys_to_retrive_answers:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

