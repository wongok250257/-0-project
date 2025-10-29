import streamlit as st
import pandas as pd

# 메인페이지 
# Iris 사진 경로 - https://images.pexels.com/photos/5677011/pexels-photo-5677011.jpeg?auto=compress&cs=tinysrgb&w=200
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 나타내기 
def main_page():
    st.header('좋아하는 사람이 있으신 분들의 페이지')
    st.image('https://i.namu.wiki/i/DiYExkj1wNJiwl8yxJ_35zdhCk_Zks9GtCa8zqErfpH703Sv7DCcJeeLBBMxLC-eofYKMz3e8w2nHa5uY4bZ4V5nWh74TXtbYnzyHQ5WP2iXQBgTsscz9fxdPeV3jIMlLIz-Q_rsR0wLT8WIHg6t1Q.webp')
    iris = pd.read_csv('좋아하는 사람이 있으신 당신을 제가 도와드릴게요!')
    st.write(iris)
    
# 2페이지: 세 개의 columns으로 나누어 꽃 이름과 사진 나타내기
def page2():
    st.header('좋아하는 사람이 없으신 분들의 페이지')
    st.image('https://blog.kakaocdn.net/dna/GHQUw/btr35vWC5ng/AAAAAAAAAAAAAAAAAAAAAFWKhDDyeFtlcOIFvUAEwRezSUEhs-5eoOymt5CbnATF/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&amp;expires=1761922799&amp;allow_ip=&amp;allow_referer=&amp;signature=rey%2Bqe%2FNNc3AlVaQte7nh%2F52Ekc%3D')
    iris2 = pd.read_csv('당신의 앞날에 희망이 있기를 바랄게요!')
    st.write(iris2)


# 3페이지: 세 개의 tab을 사용하여 iris 3가지 꽃 나타내기 (width=500)
def page3():
    st.header('Page 3')
    tab1, tab2, tab3 = st.tabs(['Setosa', 'Versicolor', 'Virginica'])
    with tab1:
        st.text('Setosa')
        st.image('https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_.jpg')
    with tab2:
        st.text('Versicolor')
        st.image('https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg')
    with tab3:
        st.text('Virginica')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1920px-Iris_virginica_2.jpg')

        
# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = {'Main Page':main_page, 'Page2':page2, 'Page3':page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a Page.', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-3.layouts.py
