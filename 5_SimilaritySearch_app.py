import streamlit as st
import spacy
import ginza
import pandas as pd

# タイトル
st.title('類似度計算')

nlp = spacy.load('ja_ginza')
# col1, col2 = st.columns(2)

# Input
# with col1:
#     input_text1 = st.text_input('文章1')
# with col2:
#     input_text2 = st.text_input('文章2')
input_text = st.text_input('検索')
texts = input_text.split(',')
# st.write(input_text.split(','))
uploaded_file = st.file_uploader('CSVを選択', type='csv')

# Process
# if st.button('実行'):
#     doc1 = nlp(input_text1)
#     doc2 = nlp(input_text2)
#     similarity = doc1.similarity(doc2)
if uploaded_file is not None:
    tg_data = pd.read_csv(uploaded_file, encoding='cp932')
    tg_col = st.selectbox('対象列選択', tg_data.columns)
    if tg_col is not None:
        if st.button('実行'):
            tg_data = tg_data.dropna()
            tg_data.reset_index(drop=True, inplace=True)
            for cnt,j in enumerate(texts):
                tg_data[f'{j}との類似度'] = 0
                doc1 = nlp(j)
                for i in range(len(tg_data)):
                    # st.write(tg_data.columns)
                    doc2 = nlp(tg_data[tg_col][i])
                    similarity = doc1.similarity(doc2)
                    tg_data[f'{j}との類似度'][i] = similarity
                tg_data.sort_values(f'{j}との類似度',ascending=False,inplace=True)
                # tg_data.set_index(tg_col, inplace=True)
                
    
    # Output
        # st.write(f'類似度：{round(similarity, 2)}')
                # st.write(input_text)
                # st.write(tg_col)
                # st.dataframe(tg_data)
            tg_data.reset_index(inplace=True)
            st.dataframe(tg_data)
            
