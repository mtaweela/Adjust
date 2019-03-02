# Adjust End Point

Simple API end point.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To install the project, you need to get [Django](https://www.djangoproject.com/), [python](https://www.python.org/) 2.7, [pip](https://pypi.org/project/pip/) and [MYSQL](https://www.mysql.com/) runing on your machine.

### Installing
Once you have the previous mentioned tools, you could download the source code and go to the directory containing the source code and run the following to install the needed libraries.

```
pip install -r requirements.txt
```

After installing, you could either use the configuration file called production_env.py inside the folder /Adjust/Adjust inside the project or change the configurations in the file for more security.

Then, you need to create a database in MYSQL to be used by the project. In MYSQL console you could run:
```
create database datarestdb;
```

Then you need to run the migration by:

```
python manage.py makemigrations
python manage.py migrate
```

After that, you could run the server simply by:
```
python manage.py runserver
```

## Test the endpoint
finally you could now test the endpoint using postman or curl or by simply typing the following url in the browser.

```
localhost:8000/api/performance_metric/?date_from=2017-05-17&date_to=2017-05-18&sort_by=revenue&sort_type=asc&group_by=revenue,spend&filter_by_channel=adcolony&filter_by_country=US&filter_by_OS=android
```
The query string is the main used part where it controls the filters, grouping and sorting.

date_from --> used to filter by date equal or larger than its value.

date_to --> used to filter by date equal or less than its value.

sort_by --> takes the name of the field to sort by. 

sort_type --> takes the sorting criteria (asc for ascending order and des or any other word for descending order)

group_by --> takes comma separated fields names.

filter_by_channel, filter_by_country, filter_by_OS --> are used for filtering by channel, countery,, operating system.


## Additional info
inside the scripts folder you could find a script called upload_data.py that is used to upload the data in the dataset.csv file to the database.

## Built With

* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Express](https://expressjs.com/)
* [MYSQL](https://www.mysql.com/)

## Authors

* **Mohamed Taweela** - *Initial work* - [mtaweela](https://github.com/mtaweela)