# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommender System** built using Python. It suggests 5 similar movies based on an input title using genres, keywords, and overview. It's a beginner-friendly project ideal for learning text feature extraction and cosine similarity.

---

## 📁 Dataset

This project uses a simplified version of the **TMDB 5000 Movies Dataset**, containing:
- Movie titles
- Genres
- Keywords
- Overview

File used: `tmdb_5000_movies.csv` (10 movies)

---

## 🚀 How It Works

1. *Data Preprocessing: Combines `genres`, `keywords`, and `overview` into a single text column.
2. Vectorization: Converts the combined text into numeric vectors using `CountVectorizer`.
3. Similarity Calculation: Uses `cosine_similarity` from `scikit-learn` to measure similarity between movies.
4. Recommendation: Based on user input, the system recommends the top 5 similar movies.

---

## 💻 Technologies Used

- Python  
- Pandas  
- scikit-learn (CountVectorizer & Cosine Similarity)

---

## 📦 How to Run

1. Clone the repository or download the files.

2. Install required libraries:
```bash
pip install pandas scikit-learn
python project2.py
Enter a movie title: Inception
Top 5 movies similar to 'Inception':

The Dark Knight  
Interstellar  
The Avengers  
The Matrix  
Avatar
