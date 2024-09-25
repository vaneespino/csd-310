# Import mysql
import mysql.connector as sql

def show_films(cursor, title):
	# execute an inner join on all tables
	cursor.execute('''select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id''')
	# get results from cursor
	films = cursor.fetchall()
	print("\n -- {} --".format(title))
	
	#iterate film data and display
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
		film[0], film[1], film[3]))
		
# main method
def main():
	
	#create connection to database
	connection = sql.connect(
	host="localhost",
	user="movie_user",
	password="popcorn",
	database="films"
	
	)
	# create cursor
	cursor = connection.cursor()
	
	# display existing records in database
	show_films(cursor, "DISPLAYING FILMS")
	 
	 # insert new movie
	 insertQuery = " INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Hunger Games', '2012', '222', 'Gary Ross', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), (SELECT genre-id FROM genre WHERE genre_name = 'SciFi') );"
	 connection.commit()
	 cursor.execute(insertQuery)
	 show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
	 
	 # update Alien movie
	 updateQuery = " update film set genre_id = (select genre-id from genre where genre_name = 'Horror') where film_name = 'Alien';"
	 connection.commit()
	 cursor.execute(updateQuery)
	 show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")
	 
	 # delete Gladiator movie from table
	 deleteQuery = " delete from file where film_name = 'Gladiator';"
	 connection.commit()
	 cursor.execute(deleteQuery)
	 show_films(cursor, "DISPLAYING FILMS AFTER Delete")
	 
	 main()
