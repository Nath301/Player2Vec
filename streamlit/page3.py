import streamlit as st
import streamlit.components.v1 as components

def info3():
    st.write(
        '''#### Finally, on this page using the link, you can see our model training in real time. We used the Projector TensorFlow tool provided by TensorFlow.
        ''')
    st.write('''
        Approach:
        - Click on the link
        - Go to TSN-E
        - Pause directly
        - Click on Sphereize data in the top box, learning rate of 10.
        - Stop the training after 150 iterations
        - You can put the labels and see the clusters

        Bonus:
        If you go to the right sidebar after the training you can search for a player and see which players are the most similar to him.

        Enjoy''')


def app():
    info3()
    visualisation = 'https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/Yanka13/ab939e88821f32da1ad5fc32149b6261/raw/0c5f257bbeb035a4d7708b49cab447044dd7911b/player2vec_config.txt'
    st.write(f"check out this [link]({visualisation})")

    components.iframe("https://projector.tensorflow.org/", scrolling=False, width=1200, height=800)
