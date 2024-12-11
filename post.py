import streamlit as st
from openai import OpenAI

openAi_APIKEY=st.secrets['openAi_APIKEY']

client = OpenAI(
    api_key=openAi_APIKEY
)
st.title('농담 생성기')
input_text=st.text_area("주제를 정해주세요")

if st.button('농담 생성') :
    with st.spinner('농담 생성중...'):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
            messages= [
                {"role": "system", "content": "너는 농담을 잘하는 유쾌한 AI야 내가 던진 주제에 맞는 농담을 생성해줘"},
                {"role":"user", "content" : input_text}
            ]
        )
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=input_text+'에 어울리는 웃기는 이미지 생성.',
            size="1024x1024",
            n=1,
            )

        st.success(f"재밌는 사실 : {response.choices[0].message.content}")
        image_url = img_response.data[0].url
        st.image(image_url)