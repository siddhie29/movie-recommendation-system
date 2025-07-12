import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("tmdb_5000_movies.csv")

# Fill any missing values
for feature in ['genres', 'keywords', 'overview']:
    movies[feature] = movies[feature].fillna('')

# Combine selected features
movies['combined'] = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['overview']

# Convert text to vectors
cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(movies['combined'])

# Calculate similarity
similarity = cosine_similarity(count_matrix)

# Recommendation function
def recommend(title):
    if title not in movies['title'].values:
        print("Movie not found!")
        return
    index = movies[movies['title'] == title].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    print(f"\nTop 5 movies similar to '{title}':\n")
    for i in sorted_movies:
        print(movies.iloc[i[0]].title)

# Ask user for input
movie_input = input("Enter a movie title: ")
recommend(movie_input)
