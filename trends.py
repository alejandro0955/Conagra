import anthropic
from gnews import GNews
import requests
from bs4 import BeautifulSoup
import time
import random


def ask(input):
    client = anthropic.Anthropic(
        api_key="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",
    )
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        temperature=0.5,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": input
                    }
                ]
            }
        ]
    )
    return message.content
    

articles = []
google_news = GNews()
news = google_news.get_news('Current and emerging food trends')
random.shuffle(news)
for i in range(5):
    url = news[i]['url']
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    articles.append(soup.text)
    
    
trends = ask(str(articles) + " analyze these articles and idenitfy 5 emerging or current food ingredient trends")


suggestions = {
    'suggestion1': '',
    'suggestion2': '',
    'suggestion3': '',
    'suggestion4': '',
    'suggestion5': ''
}
product_line = [
    "Frozen pizza",
    "Microwaveable burrito",
    "Instant ramen noodles",
    "Hot pockets",
    "Frozen chicken tenders",
    "Microwaveable macaroni and cheese",
    "Frozen lasagna",
    "Microwaveable popcorn",
    "Microwaveable breakfast sandwich",
    "Frozen taquitos",
    "Microwaveable chicken nuggets",
    "Instant oatmeal cups",
    "Microwaveable rice bowls",
    "Frozen mini tacos",
    "Microwaveable soup cups"
]

time.sleep(60)
for i in range(5):
    time.sleep(10)
    s = ask("How would you adapt one of these random trends:"+str(trends)+" to one random product in this product line:"+str(product_line) + " in less than 15 words")[0].text
    clean_suggestion = s.replace('\n-','')
    clean_suggestion = clean_suggestion.replace('\n','')
    suggestions['suggestion'+str(i)] = clean_suggestion
    


    
    


