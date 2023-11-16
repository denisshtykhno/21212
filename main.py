import sqlite3
import requests
from bs4 import BeautifulSoup

def create_database():

    conn = sqlite3.connect('movies_weather_database.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            genre TEXT,
            release_year INTEGER,
            director_id INTEGER,
            FOREIGN KEY (director_id) REFERENCES directors(id)
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
    ''')

    cursor.executemany('''
        INSERT INTO directors (first_name, last_name) VALUES (?, ?)
    ''', [
        ('Steven', 'Spielberg'),
        ('Christopher', 'Nolan'),
        ('Quentin', 'Tarantino'),
        ('Martin', 'Scorsese'),
        ('Hayao', 'Miyazaki')
    ])


    cursor.executemany('''
        INSERT INTO movies (title, genre, release_year, director_id) VALUES (?, ?, ?, ?)
    ''', [
        ('Jurassic Park', 'Adventure', 1993, 1),
        ('Inception', 'Sci-Fi', 2010, 2),
        ('Pulp Fiction', 'Crime', 1994, 3),
        ('The Irishman', 'Crime', 2019, 4),
        ('Spirited Away', 'Animation', 2001, 5)
    ])


    conn.commit()
    conn.close()

def get_weather():

    url = "https://weather.com/weather/tenday/l/your_location_code"  # Замініть "your_location_code" на код вашого місця


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    forecast_container = soup.find('div', class_='DailyForecast--DisclosureList')

    if forecast_container:

        forecast_items = forecast_container.find_all('div', class_='DailyContent--dailyContent--3obym')


