import stremlit as st

st.title("こんにちは、吉村ゼミ”）

name = st.text_imput("好きな言葉を入力してください")  
st.write(name)

camera = st.camera_input("写真を撮影します")
if camera:
    st.image(camera,caption="写真", use_colimn_width=True)
    
