import streamlit as st
st.title('좋아하는 사람이 있나요?')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 사람이 있나요?:', ['좋아하는 사람O','좋아하는 사람X'])
if st.button('인사말') : 
  st.write(name+'님은 '+menu+ '이시군요 잘 부탁드려요')
