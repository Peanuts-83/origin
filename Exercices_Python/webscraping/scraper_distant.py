#!/usr/bin/env python3
# coding: utf8
import os
os.chdir('webscraping')
import time
from bs4 import BeautifulSoup
import requests

unfamilliar = input("Enter skill your not familliar with :")
print("Unfamilliar skill processed.")

def find_jobs():
    html_text = requests.get('https://candidat.pole-emploi.fr/offres/recherche?lieux=83140&motsCles=python&offresPartenaires=true&rayon=60&tri=0').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_= 'result')
    for num, job in enumerate(jobs):
        age_of_job = job.find('p', class_= 'date').text.replace('\n', '')
        selection = ["hier", "aujourd'hui", " 1 ", " 2 ", " 3 "]
        if any(x in age_of_job for x in selection):
            job_name = job.find('h2', class_= 't4 media-heading').text.replace('\n', '')
            company = (job.find('p', class_= 'subtext').text.replace('\n', '')).split('-')[0]
            place = '-'.join((job.find('p', class_= 'subtext').text.replace('\n', '')).split('-')[1:])
            contract = job.find('p', class_= 'contrat').text.replace('\n', '')
            skills = job.find('p', class_= 'description').text
            more_info = job.a['href']
            if unfamilliar not in skills:
                with open(f'jobs/job{num}.txt', 'w', encoding='utf-8') as f:
                    f.write(f"\
                    Job name = {job_name} \n\
                    Company name = {company} \n\
                    Place = {place} \n\
                    Contract = {contract} \n\
                    Age of job = {age_of_job} \n\
                    More info = {'https://candidat.pole-emploi.fr' + more_info} \n\
                    ")

                print(f"""
                Job name = {job_name}
                Company name = {company}
                Place = {place}
                Contract = {contract}
                Age of job = {age_of_job}
                More info = {'https://candidat.pole-emploi.fr' + more_info}
                """)

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes.')
        time.sleep(time_wait * 60)