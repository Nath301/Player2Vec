import matplotlib.pyplot as plt
from matplotlib import patches
import seaborn as sns
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
import pandas as pd


def get_player(heatmap, name):
    player_heatmap = heatmap[heatmap["player_name"] == name]
    try:
        player_heatmap = player_heatmap.replace("2018", "2018/2019")
    except:
        pass
    try:
        player_heatmap = player_heatmap.replace("2007", "2007/2008")
    except:
        pass
    return player_heatmap


def get_seasons_for_df(player_heatmap):
    ordered_list = []
    for element in player_heatmap.seasons:
        ordered_list.append(int(element[:4]))

    player_heatmap["ordered_season"] = ordered_list
    player_heatmap = player_heatmap.sort_values(by="ordered_season")
    return player_heatmap


def get_figure(heatmap, type_name, player_name):
    player_heatmap = get_seasons_for_df(get_player(heatmap, player_name))
    player_heatmap_1 = player_heatmap[player_heatmap["type_name"] == type_name]
    player_name = player_heatmap["player_name"].unique()[0]
    fig = px.density_heatmap(data_frame=player_heatmap_1,
                             x="X_loc",
                             y="Y_loc",
                             nbinsx=22,
                             nbinsy=22,
                             range_x=(-6, 130),
                             range_y=(86, -7),
                             animation_frame="seasons",
                             animation_group="type_name",
                             color_continuous_scale="reds",
                             title=f"Heatmap",
                             width=800,
                             height=650)

    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')

    bg = Image.open("png/pitch.png")
    fig.add_layout_image(
        dict(source=bg,
             x=-0.155,
             y=1.1545,
             sizex=1.153,
             sizey=1.327,
             sizing="fill",
             layer='above',
             opacity=0.5))

    return fig


def heatmap(type_name, player_name):
    heatmap = pd.read_csv(
        "csv/type_location_for_male_player.csv"
    )
    heatmap.drop(columns="Unnamed: 0", inplace=True)
    figure = get_figure(heatmap, type_name, player_name)
    return figure


if __name__ == "__main__":
    type_name = input("Choose between: Pass//Shot//Dribble: ")
    player_name = input("Choose a player: ")
    figure_ = heatmap(type_name, player_name)
    figure_.show()
