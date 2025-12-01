animes = [
    {"name": "Attack on Titan", "genre": "Action", "score": 9.1, "episodes": 75},
    {"name": "Sakamoto Days", "genre": "Adventure", "score": 8.3, "episodes": 22},
    {"name": "Chainsaw Man", "genre": "Action", "score": 8.7, "episodes": 12},
    {"name": "Death Note", "genre": "Thriller", "score": 9.0, "episodes": 37},
    {"name": "Your Name", "genre": "Romance", "score": 8.9, "episodes": 1}
]
top_animes = list(filter(lambda a: a ["score"] >= 9,animes))
print (top_animes)

anime_scores = list(map(lambda a: (a["name"], a["score"]), animes))
print (anime_scores)

sorted_by_score = sorted(animes, key=lambda a: a["score"], reverse=True)
print(sorted_by_score)


def genre_filter_builder(target_genre):
    tg = target_genre.lower()
    return lambda a: a["genre"].lower() == tg

action_filter = genre_filter_builder("Action")
action_animes = list(filter(action_filter, animes))
print (action_animes)

def apply_processor (data, processor):
        return list(processor(data))

result = apply_processor(animes, lambda items: map(lambda a: a["name"].upper(), items))
print(result)
