from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    crypto_data = None
    error = None
    
    if request.method == 'POST':
        coin = request.form.get('coin').lower().strip()
        # Fetching data from CoinGecko
        url = f"https://api.coingecko.com/api/v3/coins/{coin}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            crypto_data = {
                "name": data['name'],
                "price": data['market_data']['current_price']['usd'],
                "change": data['market_data']['price_change_percentage_24h'],
                "image": data['image']['small']
            }
        else:
            error = "Coin not found! Try 'bitcoin' or 'ethereum'."

    return render_template('index.html', crypto=crypto_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)