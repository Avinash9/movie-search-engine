def get_most_watch_movie():
    file=open("ratings.data")
    movies_count = {}
    for line in file:
        token=line.split("\t")
        movie_id = token[1]
        if movie_id in movies_count:
            movies_count[movie_id] = movies_count[movie_id] + 1
        else:
            movies_count[movie_id] = 1
    min_value=0
    most_watch_movie_id=0
    for key, value in movies_count.items():
        if value>min_value :
            min_value=value
            most_watch_movie_id=key
    file=open("movie.data")
    for line in file:
        token=line.split('|')
        if token[0]==most_watch_movie_id:
            most_watch_movie_name=token[3]
    return most_watch_movie_name
    
    
def get_most_active_user():
    file=open("ratings.data")
    movies_count = {}
    for line in file:
        token=line.split("\t")
        user_id = token[0]
        if user_id in movies_count:
            movies_count[user_id] = movies_count[user_id] + 1
        else:
            movies_count[user_id] = 1
    min_value=0
    most_active_user_id=0
    for key, value in movies_count.items():
        if(value>min_value):
            min_value=value
            most_active_user_id=key
    file=open("user.data")
    for line in file:
        token=line.split('|')
        if(token[0]==most_active_user_id):
            most_active_user=token
    return most_active_user
