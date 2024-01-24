import pandas as pd
import streamlit as st


def main():
    data_path = st.file_uploader("Data path:", type='csv')
    if not data_path:
        st.stop()

    data = pd.read_csv(data_path)

    task_id = st.selectbox(
        'Task:',
        options=data['taskId'],
        format_func=lambda value: f'{value} -- {data.loc[data["taskId"] == value, "taskName"].squeeze()}',
    )

    task_data = data[data['taskId'] == task_id].squeeze()

    with st.expander(':red[**Task description**]'):
        st.markdown(task_data['taskDescription'], unsafe_allow_html=True)

    with st.expander(':green[**Steps**]'):
        st.markdown(task_data['steps'], unsafe_allow_html=True)

    with st.expander(':blue[**Prompt**]'):
        st.markdown(task_data['prompt'], unsafe_allow_html=True)


if __name__ == '__main__':
    main()