import pickle
import streamlit as st
import streamlit as st

import requests
import pandas


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


st.header('Aekansh\'s Movie Recommend')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie ",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    st.text(recommended_movie_names[0])
    st.image(recommended_movie_posters[0], width=200)
    st.text(recommended_movie_names[1])
    st.image(recommended_movie_posters[1], width=200)
    st.text(recommended_movie_names[2])
    st.image(recommended_movie_posters[2], width=200)
    st.text(recommended_movie_names[3])
    st.image(recommended_movie_posters[3], width=200)
    st.text(recommended_movie_names[4])
    st.image(recommended_movie_posters[4], width=200)
