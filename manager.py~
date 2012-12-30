def get_most_watch_movie_id(file_name,delimeter):
    file=open(file_name)
    movies_count={}
    for line in file:
        token=line.split(delimeter)
        movie_id=token[1]
        if movie_id in movies_count:
            movies_count[movie_id] = movies_count[movie_id] + 1
        else:
             movies_count[movie_id] = 1
    
    min_value=0
    most_watch_movie_id=0
    for key, value in movies_count.items():
        if value>min_value:
            min_value=value
            most_watch_movie_id=key
    return most_watch_movie_id
    
def get_most_watch_movie(movie_id,movie_data):
    for key, value in movie_data.items():
        if key==movie_id:
            return value
    
    
def get_movie_data(file_name,delimeter):
    file=open(file_name)
    movies_db={}
    for line in file:
        token=line.split(delimeter)
        movies_db[token[0]]=token
    return movies_db
        
            




