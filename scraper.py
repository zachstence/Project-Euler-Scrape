import requests
import re
import json
from bs4 import BeautifulSoup


def get_title(soup):
  return soup.h2.text


def get_info(soup):
  # get raw info section
  raw_info = soup.find('span', {'style' : 'left:-400px;width:450px;font-size:80%;'})
  
  # get published, solved, and difficulty information using regex
  m = re.search(r'Published on (.+); Solved by (\d+);<br/>Difficulty rating: (\d+)%', str(raw_info))
  published = m.group(1)
  solved = m.group(2)
  difficulty = m.group(3)
  
  return {'published' : published, 'solved' : solved, 'difficulty' : difficulty}


def get_images(soup):
  return []


def get_files(soup):
  return []


def get_content(soup):
  # get raw problem content
  raw_content = soup.find('div', {'class' : 'problem_content'})
  
  # somehow unwrapping the <div> tag would be better, can't get it to work though
  # so I'll just use regex to get stuff inside the tag
  html = re.search(r'<div class="problem_content" role="problem">(.*)<\/div>', str(raw_content), re.S).group(1)
  
  # replace <br> with \n and get text
  text = raw_content.get_text()

  return {'text' : text, 'html' : html, 'images' : get_images(soup), 'files' : get_files(soup)}


##########################################################################################################


# choose problem number, setup url, and get html from website
problem = 107
url = 'https://projecteuler.net/problem={}'.format(problem)
r = requests.get(url)
raw_html = r.text

# create a soup object from webpage html
soup = BeautifulSoup(raw_html, 'html.parser')



output = {
  'number' : problem,
  'url' : url,
  'title' : get_title(soup),
  'info' : get_info(soup),
  'content' : get_content(soup)
}

print(json.dumps(output, indent=2))