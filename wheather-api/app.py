#/usr/bin/python3.8


import requests
from datetime import date
import socket
from config import (aqi, location, key)
import os 

'''Checking the functionality of different wheather apis'''

# To get hostname of this pc
hostname = socket.gethostname()

# To get the ip adress of this pc
ip_address = socket.gethostbyname(hostname)

# To retrieve data from current.json method
def current_wheather():
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi={aqi}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from forecast.json method
def forecast_wheather():
    url = f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days=1&aqi={aqi}&alerts=yes'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from search.json method
def search_wheather():
    url = f'http://api.weatherapi.com/v1/search.json?key={key}&q={location}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)


# To retrieve data from history.json method
def history_wheather():

    #Upto last 7 Days
    todays_date = date.today()
    url = f'http://api.weatherapi.com/v1/history.json?key={key}&q={location}&dt={todays_date}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from astronomy.json method
def astronomy_wheather():
    todays_date = date.today()
    url = f'http://api.weatherapi.com/v1/astronomy.json?key={key}&q={location}&dt={todays_date}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from timezone.json method
def timezone_wheather():
    url = f'http://api.weatherapi.com/v1/timezone.json?key={key}&q={location}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from sports.json method
def sports_wheather():
    url = f'http://api.weatherapi.com/v1/sports.json?key={key}&q={location}'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

# To retrieve data from iplookup.json method
def iplookup_wheather():
    url = f'http://api.weatherapi.com/v1/ip.json?key={key}&q=192.168.0.104'
    response = requests.get(url)
    status = response.status_code
    headers = response.headers
    content = response.json()
    return (status, headers, content)

