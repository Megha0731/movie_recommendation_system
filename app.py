from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load saved files
df = pd.read_pickle('df.pkl')
indices = pickle.load(open('indices.pkl', 'rb'))
# recommend = pickle.load(open('tfidf.pkl', 'rb'))

# Recommendation function
def get_recommendations(title):
    title = title.lower()
    
    if title not in indices:
        return ["Movie not found!"]
    
    idx = indices[title]
    scores = list(enumerate(recommend[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    
    movie_indices = [i[0] for i in scores]
    
    return df['title'].iloc[movie_indices].tolist()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    data = request.json
    movie = data['movie']
    
    results = get_recommendations(movie)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)