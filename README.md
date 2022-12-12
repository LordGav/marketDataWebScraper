# Scraping and Storing Data in Real-time

The purpose of this project is to scrape and store data from various sources. The data includes ticker data from various streams, news articles from various sources, and data on derivative contracts from various sources. The data is stored in a PostgreSQL database and can be used for further analysis and processing.

- Scrapes news articles related to NIFTY Stocks (Reliance, HDFC, ...)
- Scrapes NIFTY and BANKNIFTY Option Chain Data
- Scrapes Stock Prices, Index Prices, Currency Rates, Commadity Prices, and Intrest Rates

Data is stored in TimescaleDB databse (TimescaleDB is a time-series SQL database)

## Screenshots:
- Console:
![image](https://user-images.githubusercontent.com/30123626/206867757-bd275456-f53b-43b5-acab-8ba3142077fc.png)

- Option Chain Data
![image](https://user-images.githubusercontent.com/30123626/206867863-5195e56d-2e37-4500-b1ad-41d62aa47662.png)

- News Data
![image](https://user-images.githubusercontent.com/30123626/206867986-72e75fc2-5499-4d34-9aa7-2a9d28eeeecb.png)

- Price Data
![image](https://user-images.githubusercontent.com/30123626/206868026-029381be-7259-41a5-9c9d-f30faa6c65e9.png)

## Installation
To install and set up this project, follow these steps:

- Clone the project repository from GitHub:

      git clone https://github.com/LordGav/marketDataWebScraper.git

- Install the required Python packages by running the following command in the project directory:

      pip install -r requirements.txt

- Install and set up a PostgreSQL database and create the tickerdata, newsdata, and derivativesdata tables. You can use the following code to create the tables.

      CREATE TABLE tickerdata (
          timestamp timestamptz,
          ticker VARCHAR(10),
          close VARCHAR(10)
      );

      CREATE TABLE newsdata (
          timestamp timestamptz,
          title VARCHAR(255),
          dateTimePublished VARCHAR(25),
          link VARCHAR(255),
          text TEXT,
          keywords TEXT,
          summary TEXT,
          author VARCHAR(100)
      );

      CREATE TABLE derivativesdata (
          timestamp timestamptz,
          underlying VARCHAR(10),
          expiryDate VARCHAR(10),
          optType VARCHAR(1),
          strikePrice VARCHAR(10),
          underlyingValue VARCHAR(10),
          openInterest VARCHAR(10),
          totalTradedVolume VARCHAR(10),
          impliedVolatility VARCHAR(10),
          lastPrice VARCHAR(10),
          bidprice VARCHAR(10),
          askPrice VARCHAR(10)
      );


- In the Scrapper class in the scrapper.py file, update the host, database, user, password, and port variables in the psycopg2.connect function with the appropriate values for your PostgreSQL database.

- You are now ready to use the Scrapper class to scrape and store data.

## Usage

To use the Scrapper class to scrape and store data, follow these steps:

- Ensure that you have installed the required Python packages and set up a PostgreSQL database with the tickerdata, newsdata, and derivativesdata tables.

- In the Scrapper class in the Scrapper.py file, update the host, database, user, password, and port variables in the psycopg2.connect function with the appropriate values for your PostgreSQL database.

- Run the Scrapper.py file to start scraping and storing data:

      python Scrapper.py

This will start the getAndStoreData method, which will continue to scrape and store data indefinitely. You can stop the scraping process at any time by pressing CTRL + C.

## Conclusion

To conclude, this project provides a Scrapper that can be used to scrape and store data from various sources. The Scrapper includes methods for scraping ticker data, news articles, and data on derivative contracts, as well as methods for inserting the scraped data into a PostgreSQL database. To use the Scrapper, you need to install the required Python packages, set up a PostgreSQL database, and update the Scrapper with the appropriate database connection information. Once you have done this, you can run the Scrapper.py file to start scraping and storing data.

I hope this README.md file provides helpful information on how to use the Scrapper class and how to set up and run the project. Let me know if you have any other questions or if you need any further clarification.
