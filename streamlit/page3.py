import streamlit as st
import streamlit.components.v1 as components

def app():
    components.iframe("https://projector.tensorflow.org/", scrolling=False, width=1200, height=800)
