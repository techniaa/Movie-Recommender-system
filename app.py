import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    api_key = '88c1e9943b82102e046127739e2dede6' 
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Image"

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


st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)


    num_cols = 5
    for row in range(0, len(names), num_cols):
        cols = st.columns(num_cols)
        for col, name, poster in zip(cols, names[row:row+num_cols], posters[row:row+num_cols]):
            with col:
                st.image(poster, use_container_width=True)
                st.caption(name)
