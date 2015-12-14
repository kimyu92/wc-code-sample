# Ubuntu configuration
* adduser newuser
* sudo visudo
* mod newuser privilege
```bash
# User privilege specification
root        ALL=(ALL:ALL) ALL
newuser    ALL=(ALL:ALL) ALL
```
* install these dependencies
```bash
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx 
sudo apt-get install python3-dev super gunicorn
```

# DB admin console
## login
* sudo su - postgres
* psql

## useful postgres command
* \connect database_name
* \list 					# list all databases
* \dt  						# list all tables in the current database
* \d tablename 				#list the schema of the table
* \dropdb database_name		# drop database (outside of psql)
* \q              # exit psql session

## Example of SQL on postgres in psql
```SQL
* psql [optional flag -u user_name] databasename
* select * from "Country";
* select Count(*) from "Player";
* select * from "Match";
```
* p.s: require to end with a semilcolon and put a quotation on table name

## Example of database creation
```SQL
CREATE DATABASE whatever_db_name_on_env;

CREATE USER myUserName WITH PASSWORD 'whateverPasswordYouSetOnEnvironment';
ALTER ROLE myUserName SET client_encoding TO 'utf8';
ALTER ROLE myUserName SET default_transaction_isolation TO 'read committed';
ALTER ROLE myUserName SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE whatever_db_name_on_env TO myUserName;
```

### Build/Migrate and test database, django >= 1.8
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser

### Single-line
```bash
python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser
```

### Migration Useful Commands
* python manage.py showmigrations --list
* python manage.py migrate --fake app_name
* python manage.py makemigrations app
* python manage.py sqlmigrate app 0001
