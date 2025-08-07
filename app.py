from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load model files
vectorizer = joblib.load('vectorizer.pkl')
vectors = joblib.load('vectors.pkl')
df = pd.read_csv('IMDb_All_Genres_etf_clean1.csv')

app = Flask(__name__)

# Get all unique genres from the 'main_genre' and 'side_genre' columns
all_genres = set()
for genre_str in df['main_genre'].dropna():
    all_genres.add(genre_str.strip().lower())

for genre_str in df['side_genre'].dropna():
    if isinstance(genre_str, str):
        genres = [g.strip().lower() for g in genre_str.split(',')]
        all_genres.update(genres)

all_genres = sorted(list(all_genres))  # Convert to sorted list

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    selected_genre = ""
    
    if request.method == 'POST':
        selected_genre = request.form.get('genre', '')
        if selected_genre:
            # Create user input vector
            user_input = selected_genre
            user_vector = vectorizer.transform([user_input])
            
            # Calculate similarity scores
            scores = cosine_similarity(user_vector, vectors)
            top_indices = scores[0].argsort()[::-1][:10]
            
            # Get recommendations with more details
            recommendations = df.iloc[top_indices][['Movie_Title', 'main_genre', 'side_genre', 'Rating', 'Year']].values.tolist()
    
    return render_template('index.html', recommendations=recommendations, genres=all_genres, selected_genre=selected_genre)

if __name__ == '__main__':
    app.run(debug=True)
