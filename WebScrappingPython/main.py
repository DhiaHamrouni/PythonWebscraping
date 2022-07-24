from bs4 import BeautifulSoup
import requests

import time


def findjob():
    print('put some skill you are unfamiliar with :')
    unfamiliar_skill= input('>')
    print(f'Filtering out {unfamiliar_skill}')
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&pDate=I&sequence=1&startPage=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    Data=dict()
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            comapny_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skill=job.find('span',class_='srp-skills').text.replace(' ','')
            listation=list(skill.split(','))
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name = {comapny_name.strip()}\n") 
                    f.write(f"Required Skills = {skill.strip()}\n")
                    f.write(f"More Info : {more_info}\n")
        print(f'File saved : {index}')

if __name__=='__main__':
    while True:
        findjob()
        time_wait=10
        print(f'waiting {time_wait} minutes.....')
        time.sleep(time_wait*60)
