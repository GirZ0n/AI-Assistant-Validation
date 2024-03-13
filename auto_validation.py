import pandas as pd
import streamlit as st
from diff_viewer import diff_viewer


def main():
    st.set_page_config(layout='wide')

    data_path = st.file_uploader("Data path:", type='csv')
    if not data_path:
        st.stop()

    data = pd.read_csv(data_path)

    left, right = st.columns(2)

    with left:
        task_id = st.selectbox(
            'Task:',
            options=data['taskId'].unique(),
            format_func=lambda value: f'{value} -- {data.loc[data["taskId"] == value, "taskName"].values[0]}',
        )

        task_data = data[data['taskId'] == task_id]

    with right:
        student = st.number_input('Student', min_value=1, max_value=len(task_data))
        row_data = task_data[task_data['user'] == student].squeeze()

    with st.expander(':red[**Task description**]'):
        description = row_data['taskDescription']

        plain = st.checkbox('Show as plain text', key='description')
        if plain:
            st.text(description)
        else:
            st.markdown(description)

    with st.expander(':green[**Steps**]'):
        steps = row_data['solutionSteps']

        plain = st.checkbox('Show as plain text', key='steps')
        if plain:
            st.text(steps)
        else:
            st.markdown(steps)

    with st.expander(':rainbow[**Hint**]', expanded=True):
        userCode = row_data['userCode']
        nextStep = row_data['nextStepCodeHint']
        hint = row_data['nextStepTextHint']

        st.write(hint)

        compare = st.checkbox('As code diff', key='compare', value=True)
        if compare:
            diff_viewer(userCode, nextStep, lang=None)
        else:
            left, right = st.columns(2)

            with left:
                st.write('Student')
                st.code(userCode, language='kotlin', line_numbers=True)

            with right:
                st.write('Assistant')
                st.code(nextStep, language='kotlin', line_numbers=True)


if __name__ == '__main__':
    main()
