def most_watch_genre():
    file=open("movie.data")
    genre={}
    for line in file:
         token=line.split('|')
         for genre_id in range(5,23):
            if token[genre_id]=="1":
                if genre_id in genre:
                    genre[genre_id]=genre[genre_id]+1
                else:
                    genre[genre_id]=1
    min_value=0
    most_watch_genre_id=0
    for key,value in genre.items():
        if value>min_value:
            min_value=value
            most_watch_genre_id=key
    print("most watch genre id")
    print(most_watch_genre_id)
            
     
     
     
    
         

         
         
