#from dotenv import load_dotenv
#load_dotenv()

#API KEY 저장을 위한 os 라이브러리 호출
import os

#from langchain.llms import OpenAI
#llm = OpenAI()

#content = "코딩"
#result = llm.predict(content + "에 대한 시를 써줘")
#print(result)


from langchain_openai import ChatOpenAI

chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens = 512)
answer = chatgpt.invoke("왜 파이썬이 가장 인기있는 프로그래밍 언어야?")
print(answer.content)

import streamlit as st
st.title('인공지능 시인')
st.title('_streamlit_is :blue[cool] :sunglasses:')