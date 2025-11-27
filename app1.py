import streamlit as st

st.title("こんにちわ、吉村ゼミ")

name = st.text_imput("好きな言葉を入力してください")  
st.write(name)

st.checkbox("同意します")

address = st.selectbox("次の中から現住所を教えてください",["映画","音楽","散歩"])
st.write(hobby)

st.slider("この映画を10点満点で評価してください",0,10,5)
st.write(score)

st.ragio("性別を選択してください")


camera = st.camera_input("写真を撮影します")
if camera:
    st.image(camera,caption="写真", use_colimn_width=True)


























































