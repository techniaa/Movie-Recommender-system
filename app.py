import streamlit as st
import pickle
import pandas as pd
import requests

import os

def download_file_from_google_drive(url, filename):
    if not os.path.exists(filename):
        import gdown
        gdown.download(url, filename, quiet=False)

MOVIE_DICT_URL = "https://drive.google.com/uc?export=download&id=1chZNqV_a3DDdneWeOmwBmsyU53rsACco"
SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=1WsaY9S2Q8vZHmEzUgLqbD6cLMDCP6eMZ"

download_file_from_google_drive(MOVIE_DICT_URL, "movie_dict.pkl")
download_file_from_google_drive(SIMILARITY_URL, "similarity.pkl")

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Fetch poster function
def fetch_poster(movie_id):
    api_key = '88c1e9943b82102e046127739e2dede6'
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Image"

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# 💫 Dark Mode Gen-Z CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #E5E5E5;
        background-color: #0D0D0D;
    }
    .stApp {
        background: radial-gradient(circle at top left, #1A1A1A, #000);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 3em !important;
        font-weight: 800;
        letter-spacing: 1px;
        background: linear-gradient(90deg, #00FFFF, #FF00FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 0, 255, 0.4);
    }
    .stSelectbox label {
        color: #E5E5E5 !important;
        font-size: 1.1em;
        font-weight: 500;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #111;
        color: white;
        border: 1px solid #444;
        border-radius: 12px;
    }
    button[kind="primary"] {
        background: linear-gradient(90deg, #FF00FF, #00FFFF);
        color: black;
        border-radius: 25px;
        font-weight: bold;
        padding: 0.6em 1.5em;
        border: none;
        transition: 0.3s;
        box-shadow: 0 0 10px rgba(255, 0, 255, 0.6);
    }
    button[kind="primary"]:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.9);
    }
    img {
        border-radius: 18px;
        box-shadow: 0 4px 25px rgba(0, 255, 255, 0.2);
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.03);
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.4);
    }
    .stCaption {
        font-weight: 600;
        color: #B8F3FF;
    }
    </style>
""", unsafe_allow_html=True)


# UI
st.title("⚡ Movie Recommender System")

selected_movie_name = st.selectbox("🎥 Pick a movie:", movies['title'].values)

if st.button("💫 Recommend Movies 💫"):
    names, posters = recommend(selected_movie_name)

    num_cols = 5
    for row in range(0, len(names), num_cols):
        cols = st.columns(num_cols)
        for col, name, poster in zip(cols, names[row:row+num_cols], posters[row:row+num_cols]):
            with col:
                st.image(poster, use_container_width=True)
                st.caption(f"🎬 {name}")
