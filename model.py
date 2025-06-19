import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/items.csv")

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["features"])
cosine_sim = cosine_similarity(tfidf_matrix)

def get_recommendations(item_id, top_n=3):
    idx = df.index[df['id'] == item_id][0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in scores[1:top_n+1]]
    return df.iloc[recommended_indices][["id", "title", "category"]].to_dict(orient="records")
