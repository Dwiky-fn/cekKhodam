import streamlit as st
import random
import json
import time

file = 'data.json'

def read_json(file_path):
    '''Menggunakan file JSON'''
    with open(file_path, 'r') as file:
        data = json.load(file)
    products = data['Sheet1']
    data_random = random.choice(products)
    return data_random

khodam = read_json(file)
list(khodam)

def main():

    st.markdown( #membuat background
    """
    <style>
    .stApp {
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fid.carousell.com%2Fp%2Flukisan-harimau-putih-1244512754%2F&psig=AOvVaw2r8cX53PVbimV7JzrQ3BbW&ust=1719275736766000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCuu6H_8oYDFQAAAAAdAAAAABAh');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

# Membuat kolom
col1, col2, col3 = st.columns([1, 2, 1])

# Menempatkan judul di kolom tengah
with col2:
    st.title("Cek Khodam")
    nama = st.text_input('',placeholder='Masukkan nama')

with col2:
    st.markdown(
        """
        <div style="position: absolute; top: 5px; left: -72px; background: rgba(255, 255, 255, 0.7); padding: 250px; border-radius: 15px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    if nama:
        st.header('')
        bar_loading = st.empty()
        loading = bar_loading.progress(0)

        for i in range(101):
            
            loading.progress(i)
            time.sleep(0.001)

        bar_loading.empty()
        st.write(khodam)

if __name__ == "__main__":
    main()
