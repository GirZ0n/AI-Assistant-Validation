import pandas as pd
import streamlit as st


def main():
    number_of_tables = st.number_input('Number of tables:', min_value=2)

    tables = {}
    for i in range(number_of_tables):
        left, right = st.columns(2)
        with left:
            table_name = st.text_input('Table name:', key=f'table_name_{i}')

        with right:
            table_path = st.file_uploader('Table path:', type='xlsx', key=f'table_path_{i}')

        if table_path:
            tables[table_name] = pd.read_excel(table_path).set_index('taskId')

    try:
        table = next(iter(tables.values()))
    except StopIteration:
        st.stop()

    left, right = st.columns(2)

    with left:
        task_id = st.selectbox('Task ID:', options=table.index)

    columns = table.columns.tolist()
    columns.remove('taskName')
    columns.remove('taskDescription')
    columns.remove('prompt')
    columns.remove('steps')

    with right:
        column = st.selectbox('Column:', options=columns, format_func=lambda value: value[: value.find(':')])

    for name, table in tables.items():
        st.header(name)
        st.write(table.at[task_id, column])


if __name__ == '__main__':
    main()
