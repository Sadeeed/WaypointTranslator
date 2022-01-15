# Waypoint Translator

![GitHub contributors](https://img.shields.io/github/contributors/Sadeeed/WaypointTranslator?style=flat)

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)
+ [Contributing](#contributing)

## About <a name = "about"></a>
A Django based webapp to convert between various Minecraft minimap waypoints

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.10
Django 4
```

### Run

Clone this repo

```
git clone https://github.com/Sadeeed/WaypointTranslator.git
```

Setup a virtual environment inside the project folder and activate it

```
python -m venv venv
```

```
source venv/bin/activate
```

Install the requirements

```
pip install -r requirements.txt
```

Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

Run the server with Django

```
python manage.py runserver
```

You should now be able to acess the webapp through `localhost:8000` or `127.0.0.1:8000/`

## Screenshots

![Screenshot](https://i.imgur.com/k4h5CQH.png)

## Contributing

All kinds of contributions are welcome, if you would like to improve the code make a pull request
