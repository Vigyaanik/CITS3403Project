# CITS3403Project
@authors: Divyanshu Siwach (22912646), Ron Zatuchny (22984076), Bao Long Hoang (22667153), Oliver Winter (22987923)

A Memory-based game teaching us about how memory works with the help of demonstrations. The demonstrations used in this project is a fun and interesting game with multiple assignments. The user sees a few cards and have to flip two of them, one after the other. Each card has a face behind it, if the faces matches, it's a match and that means that you have found a pair. If it's not a pair, the cards flip back soon. The purpose of the game is to find all the pairs in the least number of trials.

Dependencies:
pip3 install Flask
flask
bcrypt
sqlite3
import os
sqlalchemy
selenium
unittest

To run the project, go to the command line and enter: flask run
It will run a local server host: http://localhost:5000/

When the project runs, the first page is a login page, if you haven't already registered, just go to register and make an account. You can use same login details to login later. The Username and email for registration has to be unique. The password will be stored as hash so that if anyone ever gets access to the database can not get those passwords. The database also stores date and time of registration, this can be used to add future features for the website.
When you login, your password and user name must match, otherwise you will receive an error. On entering the website, you will receive a welcome message. These messages disappear after a couple of seconds on their own.

Successful login takes you to the home page. Here you can read about the website and more about the game. This is the only page that someone can reach without logging in. This is so that they can read more about the game before registering. You can use the navigation bar to shift between the tabs on website.

The Content page has both content and assignments for the game. Here you can play the game. The top player records are stored on the website using a databse for everyone to see. The Feedback page gives you a feedback on your score. The Statistics page has statistics for the game using a plot.

The Unit tests for this project currently include a login tester to check whether a user can successfully log in or not. Checks whether the password is working or not by comparing the hashes. To run the unit test you will need to install selenium in your working directory. Use the command python -m test.unit to run the tests. You must have a matching version for chrome and chrome driver to run the tests and the chrome driver should be present in the same directory as your testdb.py file.

This project also uses downloaded jquery. 
