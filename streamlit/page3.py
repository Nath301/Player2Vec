import streamlit as st
import streamlit.components.v1 as components

def app():
    visualisation = 'https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/Yanka13/ab939e88821f32da1ad5fc32149b6261/raw/0c5f257bbeb035a4d7708b49cab447044dd7911b/player2vec_config.txt'
    components.iframe("https://projector.tensorflow.org/", scrolling=False, width=1200, height=800)
    st.write(
        f"check out this [link]({visualisation})"
    )
