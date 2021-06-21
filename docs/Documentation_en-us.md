# Documentation

## Problem

Candlestick charting is extremely relevant in Bitcoin and cryptocurrency trading as a whole. By learning how candlestick patterns work, you can get ahead of the trend by acting on these leading indicators before the rest of the traders pile on.

As candlesticks utilize raw price data and updates as soon as a period is completed, candlestick patterns are said to be “leading” indicators and not “lagging.” This makes candlestick pattern recognition a must-have if you plan on trading cryptocurrencies.

A candlestick consists of four values, open, high, low and close. The open value refers to the first value of the range and the close value to the last value, whereas the high and low values represent the highest and lowest value in the range respectively. This project fetches real-time values from a public API and saves them in memory. Periodically, saved data is aggregated into 1, 5 or 15 minute candlesticks and saved in a local database. The application runs continuously, saving the candlesticks as soon as the period is complete. 


## Project decisions

### Docker

Two services were created using docker-compose, one uses a standard MariaDB image and the other uses an image built using the python 3.8.5 image, but the Poetry dependency manager and project dependencies are installed via the dockerfile. In the docker-compose file a network that both services use is also created, this is useful because then containers can communicate through hostnames that are always the same and don't need to use IP addresses that are dynamic. 

### Poetry

Poetry was used to manage the project dependencies because I had used it in other projects and I find it practical.

### Database

For the database, I chose to use MariaDB as it is a version of MySQL, but open-source. All commands are identical and the python libraries made for mysql work with MariaDB without problems.

As this is a public project, I chose to use the mysql option which allows the database's root password to be empty for ease. In private versions if someone creates a fork of this project and puts it into production in a real database I suggest that you change this option in the docker-compose file. 

### Parallel programming

There are two aspects of the system that must run all the time, the data request that calls Poloniex's public api and the methods that create the candlesticks at the end of each period. I researched some ways to run code concurrently and ended up choosing to use the threading library because it is simpler to use and easier to create tests for, since I still didn't have much experience with parallel programming in python. Each of the methods that needs to run continuously calls itself via the threading.Timer() method. The methods that perform requests have a delay of 0.3 seconds each, since the maximum number of requests to the api is 6 per second, so each method performs a maximum of 3 requests per second. 

<!-- porque thread -->

## Possible improvements

~~One of the main points I intend to improve on the system is to make it more generic. Currently it is only possible to fetch the data and create Bitcoin and Monero candles. A way to improve this would be to get the currency codes using the api's 'returnCurrencies' command and give the user the option of which currency to use showing the codes and names on the screen, or passing the code of the pair in the class constructor.~~ _Improvement implemented._

I would also like to have done the integration tests, I don't have much experience with that and I preferred to focus on doing the unit tests.

~~Some methods got a little big, it would be good practice to break them down into smaller methods, I plan to do that in the future.~~ _Improvement implemented._

## Main difficulties

My main difficulty was finding a way to make requests in real time, I tried to do it with async but I couldn't do it the way I wanted so I ended up choosing to use the threading library. Another difficulty was finding a good way to decide when to close the candlesticks. I ended up deciding to use the _time_ library, closing the candles in the last second of each period, I don't know if there is a more elegant method but it worked well and consistently.

The testing part was also a point of difficulty as I didn't have much experience with it. I ended up choosing to only do unit tests but I intend to increase the test coverage by doing the integration tests with the bank.