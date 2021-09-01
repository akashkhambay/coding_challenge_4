# coding_challenge_4

## Purpose of the App:

Welcome to a webapp created by Polina, James and Akash. This is a one page website which allows for the sole purpose of shorterning a URL. Please enjoy the app.

## Technologies:

- Python
- Flask
- sqlite3
- Bootstrap
- HTML and CSS

## Installation and Usage:

### Installation -

- First clone down this repo
- Then navigate to the directory where the repo is cloned.
- Open the directory with a text editor of your choice.
- Create a virtual environment using `pipenv shell`
- Install all the dependencies required using `pipenv install`
- You have to run `python init_db.py` to intialise the database.

### Usage-

- To be able to run this web app with it's intended functionality, please in the main directory run the command `flask run`.
- This will run the webapp on your localhost with the respective port defined in the url specified in the terminal.
- Please visit the respective URL and then you can utilise the website, copy and paste any url starting with HTTPS and you can shorten this url using the specified buttons on the page.

## Challenges:

- sqlite3 did not like the integer data type being passed into it, so we had to use formatted strings on the integer 'id' so it would work.
- Bootstrap styling had some hiccups with it not working, and not actually adding the styling to the page, we had to use the `!important` code line to overwrite some stuff.
- sqlite3 requires us to constantly run `python init_db.py` to at the start before trialling the code.
- The code would sometimes get typos and we would get mixed up, hence leading to some errors, but this was easily fixed through paired programming.

## Wins:

- Got the app to function with it's intended functionality
- Copy to clipboard button
- Bootstrap styling really helped bring our vision of what we wanted the website to look like to life.
- Working together was really helpful, we found a good workflow, and having 3 minds come together on this project made debugging, troubleshooting online, finding useful tips and resources much easier.
