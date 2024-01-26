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
        description = task_data['taskDescription']

        plain = st.checkbox('Show as plain text', key='description')
        if plain:
            st.text(description)
        else:
            st.markdown(description, unsafe_allow_html=True)

    with st.expander(':green[**Steps**]'):
        steps = task_data['steps']

        plain = st.checkbox('Show as plain text', key='steps')
        if plain:
            st.text(steps)
        else:
            st.markdown(steps)

    with st.expander(':blue[**Prompt**]'):
        prompt = task_data['prompt']

        plain = st.checkbox('Show as plain text', key='prompt')
        if plain:
            st.text(prompt)
        else:
            st.markdown(prompt, unsafe_allow_html=True)


if __name__ == '__main__':
    main()