import json
import os
from pprint import pprint
from IPython import embed

from app.models import *

# Path
current_folder_path = os.path.dirname(os.path.abspath(__file__))
absolute_json_path = os.path.abspath(current_folder_path + '/../../db_data/json')


# Debugging purpose
DEBUG_SWITCH = False

# driver
def run(*args):
	player_basic()
	player_bio()
	player_twitter()


# Insert basic information associate with player
def player_basic():
	player_dict = {}
	 
	data_path = absolute_json_path + '/Players-basic.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		player_dict = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(player_dict)

		for key in player_dict:
			q = 0
			p = Country.objects.get(country_name = player_dict[key][1])
			q = Player.objects.create(country=p, sur_name=player_dict[key][0], full_name=key, clubname=player_dict[key][2], position=player_dict[key][3], shirt_number=player_dict[key][5], birth_date=player_dict[key][4], player_image=player_dict[key][6], international_caps=player_dict[key][7] , first_international_appearance=player_dict[key][8], goals=player_dict[key][9], height=player_dict[key][10], biography=player_dict[key][11])
			q.save()


# Update biography associate with player
def player_bio():
	player_list = []
	 
	data_path = absolute_json_path + '/Players-bio.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		player_list = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(player_list)

		for play_dict in player_list:
			for key in play_dict.keys():
				try:
					q = Player.objects.get(full_name = key.title())
					q.biography = play_dict[key]
					q.save()
				except Player.DoesNotExist:
					raise "Player not found"


# Insert twitter account associate with player
def player_twitter():
	player_dict = {}
	 
	data_path = absolute_json_path + '/Players-twitter.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		player_dict = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(player_dict)

		for key in player_dict:
			q = Player.objects.get(full_name = key)
			q.twitter_name = player_dict[key]
			q.save()