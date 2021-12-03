import pandas as pd
import streamlit as st
import pickle
from heatmap import heatmap

st.markdown('<style>h3{color: #000}</style>', unsafe_allow_html=True)
st.markdown('<style>h1{color: #4056A1}</style>', unsafe_allow_html=True)
st.markdown('<style>.css-1hox65q{color: #FFFFFF}</style>',
            unsafe_allow_html=True)


def get_pic(player_name):
    temporary_df = pd.read_csv('csv/player_pic_club_and_flag.csv'
    )
    list_of_names = list(temporary_df["long_name"])
    if player_name in list_of_names:
        df_0 = temporary_df[temporary_df["long_name"] == player_name]
        url_pic = list(df_0["player_face_url"])[0]
        url_club = list(df_0["club_logo_url"])[0]
        nation_flag_url = list(df_0["nation_flag_url"])[0]
        club_name = list(df_0["club_name"])[0]
        return url_pic, url_club, nation_flag_url, club_name
    else:
        url_pic = 'https://cdn.sofifa.net/players/notfound_0_120.png'
        return url_pic


def player():
    data = pd.read_csv('csv/player2vec_final_df.csv')
    df = data.copy()
    data1 = pd.read_csv('csv/player.csv')
    df1 = data1.copy()

    st.sidebar.write('### Check the stats and similar players of this player')

    player = st.sidebar.selectbox('Select a player',
                                  df1['player_name'].sort_values())
    #index=df['player_name'].iloc[3271]
    number_of_player = len(df1['player_name'])
    st.sidebar.write(f'There are {number_of_player} players available.')

    id = []
    for n in range(len(df['player_name'])):
        if player in df['player_name'].iloc[n]:
            id = df['Unnamed: 0'].iloc[n]
    st.sidebar.write('### Check the number of similar players of this player')
    st.sidebar.write('Select a number of player')
    num_of_similar = st.sidebar.slider(' ', 3, 10)
    file = open('pickle/doc2vec.pickle', 'rb')
    loaded_model = pickle.load(file)
    result = loaded_model.dv.most_similar(loaded_model[id], topn=100)
    lst = [x for x in df1['player_name']]

    dict_similar = []
    for n in result[1:]:
        if df.iloc[n[0]]['player_name'] in lst:
            dict_similar.append(df.iloc[n[0]]['player_name'])
    f'''
        ## {player}
    '''
    st.write(f"### {player}")

    ###Informations about the player
    st.write('#### Informations')
    col1, col2 = st.columns(2)
    player_photo = get_pic(player)
    team = df.iloc[id]['team']
    position = df.iloc[id]['position']
    foot = df.iloc[id]['foot']
    goals = df.iloc[id]['goals']
    with col2:
        if player_photo == 4:
            st.write('Team : ', player_photo[3])
        else:
            st.write('Team : ', team)
        st.write('Position : ', position)
        st.write('Foot : ', foot)
        st.write('Goal per match : ', goals)
    with col1:
        if len(player_photo) == 4:
            st.image(player_photo[0])
            st.image(player_photo[2])
        else:
            st.image(player_photo)

    st.write(f'''
    ### Here are the {num_of_similar} players that are the most similar to {player}
    ''')
    c1 = st.container()
    i = 0
    for pl in dict_similar:
        if i < num_of_similar:
            c1.write(f"{i+1}. {pl}")
        i += 1
    st.write(f"### {player}'s heatmap over recorded seasons")

    type_name = st.selectbox(
        'Please Choose one of the three possible actions?',
        ('Pass', 'Dribble', 'Shot'))

    figure = heatmap(type_name, player)

    st.plotly_chart(figure, use_container_width=False)


def app():
    player()
