import Parser
import getdata
def main():
	most_watch_movie_name=Parser.get_most_watch_movie()
	print("most watch movie")
	print(most_watch_movie_name)
	most_active_user=Parser.get_most_active_user()
	print("most active user")
	print(most_active_user)
	getdata.most_watch_genre()
			

if __name__=="__main__":
	main()
