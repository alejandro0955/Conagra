from flask import Flask, render_template, jsonify
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
        api_key="",
        api_key="",
    )
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=2000,
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
    
file = pd.read_excel('test.xlsx', engine='openpyxl')
file = file.to_dict(orient="index")
    
    
file = pd.read_excel('test.xlsx', engine='openpyxl')
file = file.to_dict(orient="index")
    
    


suggestions = {
'suggestion1': '',
'suggestion2': '',
'suggestion3': '',
'suggestion4': '',
'suggestion5': ''
'suggestion1': '',
'suggestion2': '',
'suggestion3': '',
'suggestion4': '',
'suggestion5': ''
}






product_line = ["beef jerky", "hot pockets", "Beef power bowls", "simply steamers", "cookie mix", "cake mix", "Ultimate Plant-Based Chick’n Tenders", "turky roast", "wings", "sugared donuts bites", "Berry Smoothie Bowl", "Marie Callender's frozen meals", "Slim Jim meat snacks", "Hunt's canned tomatoes and sauces", "Chef Boyardee canned pastas and meals", "Orville Redenbacher's popcorn products", "Duncan Hines baking mixes and frostings", "Healthy Choice frozen meals and soups", "Banquet frozen meals and desserts", "Hebrew National hot dogs", "Birds Eye frozen vegetables", "Van Camp's canned beans", "Reddi-wip whipped topping", "Frontera frozen meals and sauces", "Gardein plant-based meat alternatives (acquired by Conagra)", "Angie's Boomchickapop popcor", "Earth Balance plant-based butter and spreads", "Udi's Gluten Free bread and baked goods (acquired by Conagra)", "Blake's All Natural Foods frozen meals (acquired by Conagra)", "Duke's and Bigs meat snacks", "Frontera salsas and sauces", "Peter Pan peanut butter", "Snack Pack pudding cups", "Rosarita canned beans and Mexican food products", "La Choy Asian-style canned foods", "Swiss Miss hot cocoa mixes", "Vlasic pickles", "Bertolli frozen meals and pasta sauces (licensed brand)", "Angie's kettle corn", "Slim Jim jerky"]
# str(product_line[random.randrange(0,len(product_line))])
# str(product_line[random.randrange(0,len(product_line))])
# time.sleep(60)

    

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('/index.html', product_line=product_line)

@app.route('/ask')
def askTrends():
    trends = ask("List the 5 most trending ingredients in this dataframe by name and number "+str(file))[0].text
    for i in range(5):
        random.shuffle(product_line)
        s = ask("How  can ingredient number " + str(i+1) +" of these trends:" + str(trends)+" be incorporated into one specific product from this list: "+str(product_line) + " in less than 15 words. please do not refer to me and please refer to the ingredient by its name and not its number")[0].text
        clean_suggestion = s.replace('\n-','')
        clean_suggestion = clean_suggestion.replace('\n','')
        suggestions['suggestion'+str(i+1)] = clean_suggestion
    
    result = {
        'suggestion1': suggestions['suggestion1'],
        'suggestion2': suggestions['suggestion2'],
        'suggestion3': suggestions['suggestion3'],
        'suggestion4': suggestions['suggestion4'],
        'suggestion5': suggestions['suggestion5']
    }
    print(result)
    time.sleep(60)
    return jsonify(result=result)

@app.route('/Analytics')
def Analytics():
    graphs = file
    return render_template('/Analytics.html', graphs= graphs)


if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()