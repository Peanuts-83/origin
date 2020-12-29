#!/usr/bin/env python3
# coding: utf8
import os

from bs4 import BeautifulSoup
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/webscraping')

with open('Python_test.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    
    paragraf_tags = soup.find_all('h3')
    print(paragraf_tags)
    for paragraf in paragraf_tags:
        print(paragraf.text)

    links = soup.find_all('a')
    # print(links)
    for l in links:
        print(l.text)

with open('manomano.html', 'r', encoding='utf-8') as mano_file:
    content = mano_file.read()
    soup = BeautifulSoup(content, 'lxml')

    links = soup.find_all('span', class_='price-integer')
    for l in links:
        print(l.text)

