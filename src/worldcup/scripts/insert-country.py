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
	country_basic()
	country_stat()
	country_bio()


# Insert Basic information about a country
def country_basic():
	country_dict = {}
	 
	data_path = absolute_json_path + '/Countries-basic.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		country_dict = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(country_dict)

		for key in country_dict:
			q = 0
			q = Country(country_name=key, \
         				country_code=country_dict[key][0], \
         				rank=country_dict[key][1], \
         				flag=country_dict[key][2], \
         				symbol_flag=country_dict[key][3], \
         				map_url=country_dict[key][4], \
         				team_logo_url=country_dict[key][5], \
         				team_video_url=country_dict[key][6]).save()


# Insert stat for countries
def country_stat():
	country_dict = {}
	 
	data_path = absolute_json_path + '/Countries-stat.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		country_dict = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(country_dict)

		for key in country_dict:
			q = Country.objects.get(country_name=key)
			q.matches_played = country_dict[key][0]
			q.goals_scored = country_dict[key][1]
			q.attempts_on_target = country_dict[key][2]
			q.distance_covered = country_dict[key][3]
			q.one_g_freq_min = country_dict[key][4]
			q.one_g_freq_attempts = country_dict[key][5]
			q.scoring_method_total = country_dict[key][6]
			q.open_play_goals = country_dict[key][7]
			q.set_piece_goals = country_dict[key][8]
			q.att_attempts = country_dict[key][9]
			q.attempts_off_target = country_dict[key][10]
			q.att_shots_saved = country_dict[key][11]
			q.att_goals_scored = country_dict[key][12]
			q.att_shots_blocked = country_dict[key][13]
			q.tournament_average = country_dict[key][14]
			q.att_dribble_penalty_area = country_dict[key][15]
			q.att_dribble_penalty_area_ta = country_dict[key][16]
			q.att_deliveries_penalty_area = country_dict[key][17]
			q.att_deliveries_penalty_area_ta = country_dict[key][18]
			q.att_crosses = country_dict[key][19]
			q.att_crosses_ta = country_dict[key][20]
			q.att_crosses_completed = country_dict[key][21]
			q.att_crosses_completed_ta = country_dict[key][22]
			q.att_offsides = country_dict[key][23]
			q.att_offsides_ta = country_dict[key][24]
			q.def_total_defense = country_dict[key][25]
			q.def_tackles = country_dict[key][26]
			q.def_saves = country_dict[key][27]
			q.def_blocks = country_dict[key][28]
			q.def_saves = country_dict[key][29]
			q.def_saves_ta = country_dict[key][30]
			q.def_attempted_clearances = country_dict[key][31]
			q.def_attempted_clearances_ta = country_dict[key][32]
			q.def_completed_clearances = country_dict[key][33]
			q.def_completed_clearances_ta = country_dict[key][34]
			q.def_recovered_balls = country_dict[key][35]
			q.def_recovered_balls_ta = country_dict[key][36]
			q.def_tackles_tol = country_dict[key][37]
			q.def_tackles_tol_ta = country_dict[key][38]
			q.def_tackles_won = country_dict[key][39]
			q.def_tackles_won_ta = country_dict[key][40]
			q.def_tackles_lost = country_dict[key][41]
			q.def_tackles_lost_ta = country_dict[key][42]
			q.def_offsides_given = country_dict[key][43]
			q.def_offsides_given_ta = country_dict[key][44]
			q.pass_total = country_dict[key][45]
			q.pass_short_passes_complete = country_dict[key][46] 
			q.pass_medium_passes_complete = country_dict[key][47]
			q.pass_long_passes_complete = country_dict[key][48]
			q.pass_ta = country_dict[key][49]
			q.pass_crosses = country_dict[key][50]
			q.pass_crosses_ta = country_dict[key][51]
			q.pass_throw_ins = country_dict[key][52]
			q.pass_throw_ins_ta = country_dict[key][53]
			q.save()


# Insert Biography of countries
def country_bio():
	country_dict = {}
	 
	data_path = absolute_json_path + '/Countries-biography.json'

	with open(data_path) as data_file:
		data = json.load(data_file)
		country_dict = data

		if DEBUG_SWITCH:
			embed()

		if DEBUG_SWITCH:
			pprint(country_dict)

		for key in country_dict:
			q = Country.objects.get(country_name=key)
			q.article = country_dict[key][0]
			q.continent = country_dict[key][1]
			q.save()