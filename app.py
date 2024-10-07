import streamlit as st

def checkUruu(birth):
    if not birth.isdigit():
        st.write('無効な文字列です')
        return
    if int(birth) < 1582: # 定義されていない年代
        st.write(f'{birth}年は閏年という概念が存在しません')
    elif int(birth) % 400 == 0:
        st.write(f'{birth}年は閏年です')
    elif int(birth) % 100 == 0:# 平年
        st.write(f'{birth}年は閏年ではありません')
    elif int(birth) % 4 == 0:
        st.write(f'{birth}年は閏年です')
    # その他すべて平年
    else: 
        st.write(f'{birth}年は平年です')

# -- UI --
st.title('閏年判定app')

birth = st.text_input('西暦を入力してください')
btn = st.button('かくにん')
if btn:
    checkUruu(birth)
