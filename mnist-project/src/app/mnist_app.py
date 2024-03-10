import streamlit as st

st.title('MNIST Application')
st.image("https://projects-static.raspberrypi.org/projects/teach-a-computer-to-read/f6d49720608e5be2d20ea1f5847e5651269d1857/en/images/banner.png")

st.file_uploader("Enter your Image:")

result = st.button(label='Predict')


if result:
    st.success(f'Result: {7}')
    