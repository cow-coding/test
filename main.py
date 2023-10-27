import json

import streamlit as st

database = st.session_state

# To-Do List를 저장할 리스트 생성
if 'todo_list' not in database:
    database['todo_list'] = []

if 'option' not in database:
    database['option'] = ''


c1, c2 = st.columns([6, 2])
# Streamlit 앱 제목 설정
with c1:
    st.title('To-Do List 앱',)

with c2:
    if st.button("이전 목록 불러오기"):
        with open('save.json', 'r', encoding='utf-8') as f:
            database['todo_list'] = json.loads(f.read())


with st.form("할 일 추가하기"):
    col1, col2, col3 = st.columns([6, 1, 1])

    with col1:
        task = st.text_input(
            '새로운 To-Do 항목 추가',
            placeholder='새로운 To-Do 항목 추가',
            label_visibility='collapsed'
        )

    with col2:
        if st.form_submit_button('추가'):
            if task:
                todo_item = {"task": task, "done": False}
                if todo_item not in database["todo_list"]:
                    # database['todo_list'] 에 todo_item을 넣어주세요

    with col3:
        if st.form_submit_button('초기화'):
            database['todo_list'] = []

item = database['todo_list']
database['todo_list'] = sorted(item, key=lambda x: x['done'])

st.write('### 할 일 목록:')

for idx, item in enumerate(database['todo_list']):
    st.divider()
    v = st.checkbox(# 이 안에 item의 'task'와 'done'을 순서대로 넣어주세요.)
    database['todo_list'][idx]["done"] = v

st.divider()

if st.button("현재 목록 저장하기"):
    with open('save.json', 'w') as f:
        json.dump(database['todo_list'], f, indent=4)
