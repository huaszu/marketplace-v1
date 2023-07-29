# Marketplace

## Description

An online marketplace where people can buy and sell items. 

## Table of Contents

- [Tech Stack](#tech-stack)
- [Features for Users](#features-for-users)
- [Installation](#installation)
- [Upcoming Features](#upcoming-features)
- [License](#license)

## Tech Stack

- Python
- Django
- HTML
- CSS
- Tailwind
- Python Imaging Library

## Features for App Users

- Create account
- Log in
- View items in marketplace and details of each item
- Access user dashboard for each user to see and manage items they have put in marketplace
- Add, edit, and remove items for sale in marketplace

## Installation

#### Requirements:

- Python 3.10.5
- Django 4.2.3

To have this app running on your local computer, please follow the below steps:

Clone or fork this repository.
```
$ git clone https://github.com/huaszu/marketplace-v1.git
```

Create a virtual environment inside your marketplace-v1 directory.
```
$ virtualenv env
```

Activate the virtual environment.
```
$ source env/bin/activate
```

Source from `secrets.sh` to your environment.
```
$ source secrets.sh
```

Install dependencies.
```
$ pip3 install -r requirements.txt
```

Run the Django app from the command line.
```
$ python3 manage.py runserver
```

**You can now navigate to `localhost:8000` to access the marketplace.  Have fun!**

## Upcoming Features

- Enable search
- Create ability for users to communicate with each other

## License

[CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/): This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator.
![CC](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png)