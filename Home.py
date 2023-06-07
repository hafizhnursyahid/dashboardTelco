from lib import *

st.set_page_config(page_title='Overview', page_icon=':smiley:')
file = "./data.xlsx"
df = pd.read_excel(file)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
df = df.dropna()



st.title("Dataset Costumer Telco")
st.markdown("Overview the **behavior** of costumer")

st.write(df)

st.title("Overview:")

st.write("* Number of rows:", len(df))
st.write("- Number of columns:",len(df.columns), unsafe_allow_html=True)
st.write("- Column name and type:")
right, left = st.columns(2)
with left:
    for column in df.columns[10:]:
        st.write(f"{column}: {df[column].dtype}")
with right:
    for column in df.columns[:10]:
        st.write(f"{column}: {df[column].dtype}")


keterangan = pd.read_excel("./desc.xlsx")

st.title("Keterangan Setiap Atribut Kolom")
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.table(keterangan)