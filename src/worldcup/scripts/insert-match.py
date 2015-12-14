# One way of running script
# python3 manage.py runscript insert-match
# can support --script-args=whateverargs in future
# http://django-extensions.readthedocs.org/en/latest/runscript.html

import json
import os
from pprint import pprint
from IPython import embed

from app.models import *

# Path
current_folder_path = os.path.dirname(os.path.abspath(__file__))
absolute_json_path = os.path.abspath(current_folder_path + '/../../db_data/json')

# embed()

# Debugging purpose
DEBUG_SWITCH = False

def run(*args):
    match_dict = {}
    
    data_path = absolute_json_path + '/Matches.json'

    with open(data_path) as data_file:    
        data = json.load(data_file)
        match_dict = data
        
        if DEBUG_SWITCH:
            embed()

    if DEBUG_SWITCH:
        pprint(match_dict)

    # Insert basic country information
    for key in match_dict:
        score_cat = str(match_dict[key][2]) + "-" + str(match_dict[key][4])
        Match.objects.create(match_num = match_dict[key][0], country_A = Country.objects.get(country_name = match_dict[key][1]), country_B = Country.objects.get(country_name = match_dict[key][3]), winner = match_dict[key][5], score = score_cat, location = match_dict[key][6], match_date = match_dict[key][7], merge_flag = match_dict[key][8], map_location = match_dict[key][9], highlight_url= match_dict[key][10]).save()