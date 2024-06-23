from flask import Flask, render_template
import pandas as pd
import anthropic
import time
import random
from bs4 import BeautifulSoup
import requests
from gnews import GNews
import webbrowser

    
def ask(input):
    client = anthropic.Anthropic(
        api_key="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",
    )
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=100,
        temperature=1,
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
# google_news = GNews()
# news = google_news.get_news('Current and emerging food trends')
# random.shuffle(news)
# for i in range(5):
#     url = news[i]['url']
#     soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#     articles.append(soup.text)
    
    
# trends = ask("List 5 very healthy common food ingredients trends. Make sure that each food ingredient trend is not the same as the other and make sure that you list 5 trends")[0].text


suggestions = {
    'suggestion1': '',
    'suggestion2': '',
    'suggestion3': '',
    'suggestion4': '',
    'suggestion5': ''
}
product_line = ["beef jerky", "hot pockets", "Beef power bowls", "simply steamers", "cookie mix", "cake mix", "Ultimate Plant-Based Chick’n Tenders", "turky roast", "wings", "sugared donuts bites", "Berry Smoothie Bowl", "Marie Callender's frozen meals", "Slim Jim meat snacks", "Hunt's canned tomatoes and sauces", "Chef Boyardee canned pastas and meals", "Orville Redenbacher's popcorn products", "Duncan Hines baking mixes and frostings", "Healthy Choice frozen meals and soups", "Banquet frozen meals and desserts", "Hebrew National hot dogs", "Birds Eye frozen vegetables", "Van Camp's canned beans", "Reddi-wip whipped topping", "Frontera frozen meals and sauces", "Gardein plant-based meat alternatives (acquired by Conagra)", "Angie's Boomchickapop popcor", "Earth Balance plant-based butter and spreads", "Udi's Gluten Free bread and baked goods (acquired by Conagra)", "Blake's All Natural Foods frozen meals (acquired by Conagra)", "Duke's and Bigs meat snacks", "Frontera salsas and sauces", "Peter Pan peanut butter", "Snack Pack pudding cups", "Rosarita canned beans and Mexican food products", "La Choy Asian-style canned foods", "Swiss Miss hot cocoa mixes", "Vlasic pickles", "Bertolli frozen meals and pasta sauces (licensed brand)", "Angie's kettle corn", "Slim Jim jerky"]

# time.sleep(60)
# for i in range(5):
    # random.shuffle(product_line)
    # s = ask("How  can trend number " + str(i) +" of these trends:" + str(trends)+" be incorporated to this product "+str(product_line[random.randrange(0,len(product_line))]) + " in less than 15 words. please do not refer to me")[0].text
    # clean_suggestion = s.replace('\n-','')
    # clean_suggestion = clean_suggestion.replace('\n','')
    # suggestions['suggestion'+str(i)] = clean_suggestion
    

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'suggestion1': suggestions['suggestion1'],
        'suggestion2': suggestions['suggestion2'],
        'suggestion3': suggestions['suggestion3'],
        'suggestion4': suggestions['suggestion4'],
        'suggestion5': suggestions['suggestion5']
    }
    return render_template('/index.html', data = data, product_line=product_line)









if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()