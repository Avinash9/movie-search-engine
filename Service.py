import manager

def main():
    movie_data=manager.get_movie_data("movie.data","|")
    most_watch_movie_id=manager.get_most_watch_movie_id("ratings.data","\t")
    most_watch_movie=manager.get_most_watch_movie(most_watch_movie_id,movie_data)
    print "most watch movie is"
    print most_watch_movie
   # print movie_data
			

if __name__=="__main__":
	main()
