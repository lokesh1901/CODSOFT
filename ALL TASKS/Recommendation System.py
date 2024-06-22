import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("C:/Users/HAPPY/Downloads/movies.csv")
data = data.fillna('')
data['features'] = data['Genre'] + ' ' + data['Lead Studio'] + ' ' + \
                   data['Audience score %'].astype(str) + ' ' + data['Profitability'].astype(str) + ' ' + \
                   data['Rotten Tomatoes %'].astype(str) + ' ' + data['Worldwide Gross'].astype(str) + ' ' + \
                   data['Year'].astype(str)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['features'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = data[data['Film'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return data['Film'].iloc[movie_indices]

user_preference = 'Comedy'
recommended_movies = data[data['Genre'].str.contains(user_preference, case=False)]['Film'].tolist()
print(f"Recommended movies in {user_preference} genre:")
for movie in recommended_movies:
    print(f"- {movie}")

movie_title = 'Twilight'
print(f"\nMovies similar to '{movie_title}':")
similar_movies = get_recommendations(movie_title)
for movie in similar_movies:
    print(f"- {movie}")
