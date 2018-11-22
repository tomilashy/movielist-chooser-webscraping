'''
Created on Nov. 14, 2018

@author: tomilashy
'''
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint
from warnings import warn
from requests import get
from datetime import date
from openpyxl import *
import pandas as pd

import re
class imdb():
    def __init__(self,paged,start,end,min_rating):
        names = []
        years = []
        imdb_ratings = []
        runtimes=[]
        '''
        ask user to input between what years, minimum rating to show
        remove series/movies lower than the said year
        should be able to chow in gui as pqytlist
        selected movies would be saved in a file so that they do not show up when the user wants to watch another movie
        user can allow program to chose for it
        the user can clear the list if he  wishes
        user can sort however he wishes
        
        '''
        
        # url = 'http://www.imdb.com/search/title?release_date='+str(2018)+'-01-01,'+str(2018)+'-12-31'+'&sort=num_votes,desc&&start='+ str(1)
        # headers = {"Accept-Language": "en-US, en;q=0.5"}
        
        # response = get(url, headers = headers)
        # html_soup = bs(response.text, 'html.parser')
        # # print(html_soup.prettify())
        # movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
        
        # if response.status_code != 200:
        #   warn(f'Status code: {response.status_code}')
        
        
        # print(type(movie_containers))
        # print(len(movie_containers))
        # print("\n\n")
        # # for first_movie in movie_containers:
        # first_movie = movie_containers[0]
        # print(first_movie.prettify())
        # # print(first_movie.find_all('a'))
        
        # first_name = first_movie.h3.a.text
        # first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
        # # first_mscore =int( first_movie.find('span', class_ = 'metascore favorable').text)
        # first_runtime = first_movie.find('span', class_ = 'runtime').text
        # first_mscore = float (first_movie.strong.text)
        # if first_mscore > 8:
        #   print(first_name,first_year,first_mscore,first_runtime  )
        
        
        
            # Lists to store the scraped data i
        for year_url in range(int (start),int (end)+1):
          count=1
          print(f"Loading: {year_url}")
          for page in range(1,int(paged)):
              
            sleep(randint(1,4))
            '''
          https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1%27
        
            https://www.imdb.com/search/title?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&start=51&ref_=adv_nxt
        '''
            url = 'http://www.imdb.com/search/title?release_date='+str(year_url)+'-01-01,'+str(year_url)+'-12-31'+'&sort=num_votes,desc&&start='+ str(count)
            headers = {"Accept-Language": "en-US, en;q=0.5"}
            
            response = get(url, headers = headers)
            html_soup = bs(response.text, 'html.parser')
            # print(html_soup.prettify())
            movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
            count+=len(movie_containers);
            if response.status_code != 200:
              warn(f'Status code: {response.status_code}')
        
        
            # print(type(movie_containers))
            # print(len(movie_containers))
            # print("\n\n")
            # for first_movie in movie_containers:
            #   # first_movie = movie_containers[0]
            #   # print(first_movie.prettify())
            #   # print(first_movie.find_all('a'))
        
            #   first_name = first_movie.h3.a.text
            #   first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
            #   # first_mscore =int( first_movie.find('span', class_ = 'metascore favorable').text)
            #   first_mscore = float (first_movie.strong.text)
            #   if first_mscore > 8:
            #     print(first_name,first_year,first_mscore )
        
        
        
            # Lists to store the scraped data in
            
        
            # Extract data from individual movie container
            for container in movie_containers:
        
                # If the movie has Metascore, then extract:
                if container.strong.text is not None and float(container.strong.text) >min_rating :
        
                    # The name
                    name = container.h3.a.text
                    names.append(name)
        
                    # The year
                    year = container.h3.find('span', class_ = 'lister-item-year').text
                    match = re.search(r'([1-3][0-9]{3})', year)
                    year=int(match.group(0))
                    years.append(year)
        
                    # The IMDB rating
                    imdb = float(container.strong.text)
                    imdb_ratings.append(imdb)
        
                    # The Metascore
                    # m_score = container.find('span', class_ = 'metascore').text
                    # metascores.append(int(m_score))
        
                    # Duration of the movie
                    runtime = container.find('span', class_ = 'runtime').text
                    runtimes.append(runtime)
        
                    # The number of votes
                    # vote = container.find('span', attrs = {'name':'nv'})['data-value']
                    # votes.append(int(vote))
        
                    # print(name,imdb,year)
        
        self.movie_ratings= pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'Duration': runtimes})
        # print(movie_ratings.info())
        
        # movie_ratings.sort_values('year', ascending=False)
        self.movie_ratings=self.movie_ratings.sort_values(['year', 'imdb'], ascending=[False, False])
        self.movie_ratings=self.movie_ratings.drop_duplicates(subset=['movie', 'year'], keep='first')#use false to completely drop all
        self.movie_ratings=self.movie_ratings.reset_index(drop=True)
        self.movie_ratings.index.name = 'S/N'
#         print("\n\n",movie_ratings)
        # movie_ratings['year'].head(3)
#         self.movie_ratings.to_csv('movie_ratings.csv')
#         self.movie_ratings.to_excel('movie_ratings.xlsx', sheet_name='Sheet1')
        
    def printdb(self):
        return self.movie_ratings
    
    
    
