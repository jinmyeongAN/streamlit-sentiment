import streamlit as st
from transformers import pipeline
from util import get_movie, get_temperature

# 여러분의 모델. 현재는 허깅페이스 감정분석 모델 사용 (한국어 파인튜닝)
# https://huggingface.co/sangrimlee/bert-base-multilingual-cased-nsmc
classifier = pipeline(
    "sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc"
)

# 웹 페이지 제목
st.title("오늘 뭐 볼까? 👀")
# 웹 페이지 부제목
st.subheader('오늘 기분에 따라 영화를 추천해줄께요.😉')

# 웹 페이지에 입력
with st.form(key="form"):
    sentence = st.text_input(label="내 기분은..!", placeholder="나는 오늘 기분이 좋다 ㅎㅎ")
    submit = st.form_submit_button("Go!")

# 버튼을 눌렀을 때, 작동되는 코드
if submit:
    st.write("오늘의 추천 영화는..! 🔥")

    # 모델의 inference가 끝날 때까지 기다림
    with st.spinner("오늘의 추천 영화는..! 🔥"):
        # classifier 라는 이름의 딥러닝 모델사용.
        # 원하는 모델로 변경할 수 있다.
        results = classifier(sentence)[0]

    label = results["label"]
    score = results["score"]
    
    # 모델로부터 얻은 결과를 원하는 방식, 폰트, 배치대로 화면에 보여줌
    # 나만의 디자인을 원한다면 아래 링크 참고
    # https://docs.streamlit.io/library/api-reference/layout
    col1, col2 = st.columns(2)
    temperature = get_temperature(score, label)
    movie = get_movie(label)

    if label == "positive": col1.metric("나의 기분 온도", "😁", f"{temperature} °C")
    elif label == "negative": col1.metric("나의 기분 온도", "😭", f"{temperature} °C")
        
    col2.metric("오늘의 추천 영화", movie)
