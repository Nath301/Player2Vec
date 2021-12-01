import streamlit as st
import umap.umap_ as umap
import pickle

st.markdown('<style>h5{color: #659DBD}</style>', unsafe_allow_html=True)


def plot_action():
    st.write('##### Vizualisation Action2Vec')
    file = open('pickle/action2vec.pickle', 'rb')
    fig = pickle.load(file)
    fig.update_layout(
        plot_bgcolor='#C5C6C7',
        autosize=False,
        width=800,
        height=600,
    )
    st.plotly_chart(fig)

def plot_player():
    st.write('##### Vizualisation Player2Vec')
    file = open('pickle/umap_player_model.pickle', 'rb')
    fig = pickle.load(file)
    fig.update_layout(
        plot_bgcolor='#C5C6C7',
        autosize=False,
        width=800,
        height=600,
    )
    st.plotly_chart(fig)

def plot_3d():
    st.write('##### Vizualisation Player2Vec 3D')
    file = open('pickle/umap3d__player_model.pickle', 'rb')
    fig = pickle.load(file)
    fig.update_layout(
        autosize=False,
        width=800,
        height=600,
    )
    st.plotly_chart(fig)


def app():
    plot_player()
    plot_action()
    plot_3d()
