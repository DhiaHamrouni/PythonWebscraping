from bs4 import BeautifulSoup
import requests

import time


def findjob():
    i=0
    b=False
    print('put some skills you are unfamiliar with :')
    unfamiliar_skill= input('>')
    print(unfamiliar_skill)
    print(f'Filtering out {unfamiliar_skill}')
    l=list(unfamiliar_skill.split(','))
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&pDate=I&sequence=1&startPage=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    Data=dict()
    for job in jobs:
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            comapny_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skill=job.find('span',class_='srp-skills').text.replace(' ','')
            listation=list(skill.split(','))
            more_info=job.header.h2.a['href']
            while i<len(l):
                if b==False:
                    break
                else:
                    if l[i] in listation:
                        b=False
                        break
                    else:
                        i+=1
            if b==True:
                Data[comapny_name]=skill
                print(f"Company Name = {comapny_name.strip()}") 
                print(f" Required Skills = {skill.strip()}")
                print(f" More Info : {more_info}")
                print(f'')
            else:
                print("Job requires skills you're unfamiliar with !")


if __name__=='__main__':
    while True:
        findjob()
        time_wait=10
        print(f'waiting {time_wait} minutes.....')
        time.sleep(time_wait*60)
