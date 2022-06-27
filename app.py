import streamlit as st
import pickle
import pandas as pd
import requests

#fetch the movie poster from api
def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=da970bb2bfca4ac03442245799c3ce76&language=en-US'.format(movie_id))
     details = response.json()
     return "https://image.tmdb.org/t/p/w500/"+details['poster_path']

# recommendition of movies
def recommend_movie(movie):
    movie_index = movie_list[movie_list['title']==movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:16]
    movie_recommendtion = []
    movie_poster = []
    for i in movies:
        movie_id = movie_list.iloc[i[0]].id
        movie_recommendtion.append((movie_list.iloc[i[0]].title))
        movie_poster.append(fetch_poster(movie_id))
    return movie_recommendtion,movie_poster

movie_list = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("MOVIE RECOMMENDER SYSTEM")
option = st.selectbox(
     'Choose a movie:',
     movie_list['title'].values)
if(st.button("RECOMMEND")):
     recommentions,poster = recommend_movie(option)
     # movie columns 5*3
     col1,col2,col3,col4,col5 = st.columns(5)
     col6, col7, col8, col9, col10 = st.columns(5)
     col11,col12,col13,col14,col15 = st.columns(5)
     with col1:
         st.text(recommentions[0])
         st.image(poster[0])
     with col2:
         st.text(recommentions[1])
         st.image(poster[1])
     with col3:
         st.text(recommentions[2])
         st.image(poster[2])
     with col4:
         st.text(recommentions[3])
         st.image(poster[3])
     with col5:
         st.text(recommentions[4])
         st.image(poster[4])
     with col6:
         st.text(recommentions[5])
         st.image(poster[5])
     with col7:
         st.text(recommentions[6])
         st.image(poster[6])
     with col8:
         st.text(recommentions[7])
         st.image(poster[7])
     with col9:
         st.text(recommentions[8])
         st.image(poster[8])
     with col10:
         st.text(recommentions[9])
         st.image(poster[9])
     with col11:
         st.text(recommentions[10])
         st.image(poster[10])
     with col12:
         st.text(recommentions[11])
         st.image(poster[11])
     with col13:
         st.text(recommentions[12])
         st.image(poster[12])
     with col14:
         st.text(recommentions[13])
         st.image(poster[13])
     with col15:
         st.text(recommentions[14])
         st.image(poster[14])