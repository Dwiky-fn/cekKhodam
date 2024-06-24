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
        background-image: url('https://static.promediateknologi.id/crop/0x0:0x0/0x0/webp/photo/p2/01/2024/06/22/IMG_4326-4177611336.jpg');
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
