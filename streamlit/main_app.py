import streamlit as st
import page1, page2, page3

st.markdown('<style>h1{color: #4056A1}</style>', unsafe_allow_html=True)
st.markdown('<style>.css-12oz5g7{padding: 0}</style>', unsafe_allow_html=True)

c = st.container()
c.write('''
# PLayer2Vec
''')
c.write('''
#### Using NLP to Profile Football Players
#### Football speaks its own language. We translate it for you to find player similarities.
''')


PAGES = {"Data Visualisation": page2, "Project Tensorflow":page3, "Player2Vec": page1}
st.sidebar.write('### Navigation')

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
