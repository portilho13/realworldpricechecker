# REAL WORLD PRICE CHECKER
#### Video Demo:  <https://youtu.be/CSevfBgUrIE>
#### Description:
Hello world, for my project in python I thought of doing something that applies to the real world and that one day later I can use for a professional portfolio so
I chose to do a "REAL WORLD PRICE CHECKER" where the user chooses a link of a product from the website "www.fnac.pt" and a range of time and the program will obtain the price of the product and in the
space of the selected interval it will compare it with the most recent one notifying the user via telegram if there is a price change or not along with the product URL.

#### Explanation:

The program is divided in 6 functions:

- main: Is where all the basic content is and the most important, it calls all the other functions

- check_interval: It checks if the interval provided by the user is or isn´t valid if it as letters for example

- validate_url: it uses a library called "validators" to check if the url provided by the user is or isn´t valid.

- get_price: It uses a library named "requests" to get a GET Request from the URL provided by the user and then uses the "BS4" library to parse the html response obtaining the current item price.

- compare_price: It compares the price between to previous check and the current one.

- send_message: Sends the message to the telegram bot.

#### Testing

To test the program we need to create a file called test_project.py where we run pytest to check if the output of each function is what we expected and if it is it will pass all tests.

#### Librarys

In this project I used:

- requests

- telebot

- sys

- bs4

- validators

- time


#### Thoughts and things learned with this project

With this project I gained experience with web requests and handling/parsing real world values and deal with them, I expect to focus more on this part of python in the future to amplify my knowledge:
