import streamlit as st
import pandas as pd
import pickle

# Load the movie data and similarity matrix
movies = pd.read_csv("movies.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))

# Title and description
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get similar movie recommendations based on genres.")

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Recommendation function (copied from your notebook)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# When button is clicked
if st.button("Recommend 🎯"):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Similar Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
