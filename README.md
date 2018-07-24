# Project-Euler-Scrape
A complete web-scrape of every Project Euler programming challenge problem including information about the problem, the problems themselves, and all files/images.

### What information was scraped?
# FIX BELOW
![Example of scraped information](https://github.com/zachstence/Project-Euler-Scrape/raw/master/example.png)
# FIX ABOVE

I extracted as much information as I could find that was useful, including:
* Problem number (purple)
* Problem title (blue)
* Problem information (green)
  * Publish date/time
  * Number of solvers
  * Difficulty rating
* Problem description (orange)
  * Raw HTML from the page
  * Plain text
* Any images in the problem description (red)
* Any files in the problem description (yellow)

Most of the data I scraped is in the file [`1_631.json`](https://github.com/zachstence/Project-Euler-Scrape/raw/master/1_631.json). The structure of the data is:
```
{
  "<problem number>": {
    "number": 1,
    "url": "<Project Euler problem URL>",
    "title": "<title of problem>",
    "info": {
      "difficulty": <problem difficulty level in %>,
      "published": "<publish date/time>",
      "solved": <number of solvers>
    },
    "content": {
      "images": <list of images>,
      "html": <raw HTML text>,
      "files": <list of files>
    }
  },

  ...
}
```
The images and files from the problems are found in the [`images/`](https://github.com/zachstence/Project-Euler-Scrape/blob/master/images/) and [`files/`](https://github.com/zachstence/Project-Euler-Scrape/blob/master/files/) directories respectively.

### How was information scraped?
In previous commits I used a program called [ParseHub]() to do the scraping as I was fairly new to the concept and didn't think about doing it in a programming language. However, recently I redid everything in Python using [`requests`](http://docs.python-requests.org/en/master/) to get the webpages and [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) to parse the HTML and scrape the information I wanted with regular expressions. All of the code is in [`pe_scrape.py`](https://github.com/zachstence/Project-Euler-Scrape/blob/master/pe_scrape.py)

### Why?
I am in the process of making a [portfolio](https://cs.txstate.edu/~zms22/portfolio/) of all of the programming projects I have done. Naturally, I have solved a couple of the Project Euler problems and wanted to include their descriptions, title, etc in my website without manually entering it all. So I decided to have the webpages dynamically filled with PHP using a json file containing all the necessary information, hence this project!

Feel free to use the data I scraped, or modify my code to suit your needs!