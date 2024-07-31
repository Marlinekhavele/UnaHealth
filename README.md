### Glucose Record API 
Glucose API that stores users glucose values and perform basic CRUD functionalities

Built with:
```shell
Python version 3
Django
Djangorestframework
```
#### Setting up the project

- Clone the project using git clone from Github: ```https://github.com/Marlinekhavele/UnaHealth```
- Enter the project directory i.e ```cd app```
- create virtual environment
```shell
virtualenv env -p python3.11 - use your local python
```
*Activate the virtual env with the below command
```shell
source env/bin/activate
```

##### Install deps:
```shell
pip install -r requirements.txt
```
##### To check django admin you need to create a user using the below command
- `python manage.py createsuperuser` 
```shell
- username: unahealth
- password: password123
```
##### Ensure Database is on the same level
```
python manage.py makemigrations
python manage.py migrate
```
##### Run the project Locally with the below command 
```shell
python manage.py runserver
```


##### Running Tests Locally
```shell
python manage.py test

```
some environment variables you will use inside your `.env`file just copy this.
```shell
DB_USER=postgres
DB_HOST=localhost
DB_NAME=una_health_app
DB_PASSWORD=password
```
service has two DB services:
- `una_health_app_db` bound to port 5432 - a DB for local testing,
- `una_health_app_test_db` bound to port 5433 - a DB for running tests.

Load CSVs 
- Initialize database with the above credentials for the DB
- Run the script to `csv_loader` and provide the sample data path to load the data into the DB
- command for running the script `python csv_loader.py sample-data`  

