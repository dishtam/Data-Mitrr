import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape blog details from each article
def scrape_blog_details(article):
    blog = {}
    blog['Image URL'] = article.select_one('div.img a')['href']
    blog['Title'] = article.select_one('div.content h6 a').text.strip()
    blog['Date'] = article.select_one('div.blog-detail').find_all('span')[0].text.strip()
    blog['Likes Count'] = article.select_one('a.zilla-likes span').text.strip()
    return blog

# Function to scrape all pages of the blog
def scrape_all_pages(url):
    all_blog_details = []
    page = 1
    while True:
        page_url = f"{url}/page/{page}/"
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')  # Use 'lxml' parser here
            articles = soup.find_all('article', class_='blog-item')
            if not articles:
                break  # Break the loop if no more articles are found
            for article in articles:
                blog_details = scrape_blog_details(article)
                all_blog_details.append(blog_details)
            page += 1
        else:
            break
    
    return all_blog_details

# Main code to scrape the blog website
blog_url = "https://rategain.com/blog"
all_blogs = scrape_all_pages(blog_url)

# Convert scraped data to DataFrame
df = pd.DataFrame(all_blogs)

# Save scraped data to an Excel file
excel_file_name = 'blog_details.xlsx'
df.to_excel(excel_file_name, index=False)

print(f"Scraped blog details saved to {excel_file_name}")
