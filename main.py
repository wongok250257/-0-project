import streamlit as st
st.title('좋아하는 사람이 있나요?')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 사람이 있나요?:', ['좋아하는 사람O','좋아하는 사람X'])
if st.button('인사말') : 
  st.write(name+'님은 '+menu+'이시군요 잘 부탁드려요')

import pandas as pd

# 메인페이지 
# Iris 사진 경로 - https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 
def main_page():
    st.header('좋아하는 사람이 있으신 분들의 페이지')
    st.image('https://i.namu.wiki/i/DiYExkj1wNJiwl8yxJ_35zdhCk_Zks9GtCa8zqErfpH703Sv7DCcJeeLBBMxLC-eofYKMz3e8w2nHa5uY4bZ4V5nWh74TXtbYnzyHQ5WP2iXQBgTsscz9fxdPeV3jIMlLIz-Q_rsR0wLT8WIHg6t1Q.webp')
    iris = 좋아하는 사람이 있으신 당신을 제가 도와드릴게요!
    st.write(iris)

def page(2):
    st.header('좋아하는 사람이 없으신 분들의 페이지')
    st.image('https://blog.kakaocdn.net/dna/GHQUw/btr35vWC5ng/AAAAAAAAAAAAAAAAAAAAAFWKhDDyeFtlcOIFvUAEwRezSUEhs-5eoOymt5CbnATF/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&amp;expires=1761922799&amp;allow_ip=&amp;allow_referer=&amp;signature=rey%2Bqe%2FNNc3AlVaQte7nh%2F52Ekc%3D')
    iris2 = 당신의 앞날에 희망이 있기를 바랄게요!
    st.write(iris2)
