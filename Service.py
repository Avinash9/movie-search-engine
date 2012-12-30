import manager

def main():
    movie_data=manager.get_movie_data("movie.data","|")
    user_data=manager.get_user_data("user.data","|")
    most_watch_movie_id=manager.get_most_watch_movie_id("ratings.data","\t")
    most_watch_movie=manager.get_most_watch_movie(most_watch_movie_id,movie_data)
    print "most watch movie is"
    print most_watch_movie
    most_active_user_id=manager.get_most_active_user_id("ratings.data","\t")
    most_active_user=manager.get_most_active_user(most_active_user_id,user_data)
    print "most active user is"
    print most_active_user
   # print movie_data
			

if __name__=="__main__":
	main()
