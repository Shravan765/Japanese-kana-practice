import streamlit as st

hiragana_romaji = st.Page("hiragana_from_romaji_practice.py", title="Practice Writing Hiragana (か) from Romaji!", icon="✍🏻")
katakana_romaji = st.Page("katakana_from_romaji_practice.py", title="Practice Writing Katakana (カ) from Romaji!", icon="✍🏻")
romaji_hiragana = st.Page("romaji_from_hiragana_practice.py", title="Practice Writing Romaji from Hiragana (か)!", icon="✍🏻")
romaji_katakana = st.Page("romaji_from_katakana_practice.py", title="Practice Writing Romaji from Katakana (カ)!", icon="✍🏻")
hiragana_katakana = st.Page("hiragana_from_katakana.py", title="Practice Writing Hiragana (か) from Katakana (カ)!", icon="✍🏻")
katakana_hiragana = st.Page("katakana_from_hiragana.py", title="Practice Writing Katakana (カ) from Hiragana (か)!", icon="✍🏻")

main = st.navigation([hiragana_romaji, katakana_romaji, romaji_hiragana, romaji_katakana, hiragana_katakana, katakana_hiragana])
main.run()