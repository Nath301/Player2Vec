import streamlit as st
import umap.umap_ as umap
import pickle

st.markdown('<style>h5{color: #659DBD}</style>', unsafe_allow_html=True)
def info2():
    st.write(
        '''### On this page you can see the graphical representations provided by our most optimized model:
        the players' posts are well recognized and the clusters are more accurate.'''
    )


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
    info2()
    plot_player()
    plot_3d()
