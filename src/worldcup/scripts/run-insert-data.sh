# Thanks to django extensions now we can use runscripts instead of shell
# http://django-extensions.readthedocs.org/en/latest/runscript.html

# By convention scripts folder under project_root folder
# and place __init__.py and any script inside scripts folder
# permission denied? chmod u+x the script

python3 manage.py runscript insert-country
python3 manage.py runscript insert-player
python3 manage.py runscript insert-match