import requests
import csv

def get_rating_from_id(player_id):
	if(player_id != 0):
		r = requests.get('http://rating.chgk.info/api/players/'+player_id+'/rating/last')
		d = r.json()
		if(len(d)==0):
			return 0
		else:
			return d["rating"]

path = "C:\\Users\\pavel.semenyuk\\Desktop\\python\\rating\\"

with open(path + "ids.txt") as f:
	f_ids = f.read()

ids = f_ids.split("\n")
final_ratings = dict()

for player_id in ids:
	final_ratings[player_id] = get_rating_from_id(player_id)
	print(final_ratings[player_id])
# with open(path + "rating.csv", 'w', newline='') as rating_file:
# 	fieldnames = ['ID', 'Rating']
# 	rating_writer = csv.DictWriter(rating_file, fieldnames = fieldnames, delimiter = ';')
# 	rating_writer.writerow({'ID': ' ID', 'Rating': 'Rating'})
# 	for k,v in final_ratings.items():
# 		rating_writer.writerow({'ID': k, 'Rating': v})