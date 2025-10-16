# portfolio_tracker.py
import requests
import time

def get_crypto_prices(coins):
    """CoinGecko API'den verilen coin'lerin USD fiyatlarını çeker."""
    coin_ids = ",".join(coins)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_ids}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Fiyatlar alınamadı: {e}")
        return {}

def calculate_portfolio_value(portfolio, prices):
    """Portföyün toplam USD değerini hesaplar."""
    total_value = 0
    print("\nPortföy Durumu:")
    print("-" * 30)
    for coin, amount in portfolio.items():
        if coin in prices and "usd" in prices[coin]:
            value = amount * prices[coin]["usd"]
            total_value += value
            print(f"{coin.capitalize()}: {amount} adet = ${value:.2f}")
        else:
            print(f"{coin.capitalize()}: Fiyat bilgisi alınamadı")
    print("-" * 30)
    print(f"Toplam Portföy Değeri: ${total_value:.2f}")

def main():
    # Örnek portföy: Kullanıcı coin'lerini ve miktarlarını buraya girer
    portfolio = {
        "bitcoin": 0.5,    # 0.5 BTC
        "ethereum": 2.0,   # 2 ETH
        "solana": 10.0     # 10 SOL
    }
    coins = list(portfolio.keys())
    
    while True:
        prices = get_crypto_prices(coins)
        if prices:
            calculate_portfolio_value(portfolio, prices)
        else:
            print("Portföy değeri hesaplanamadı.")
        
        print("\nFiyatlar 60 saniyede bir güncelleniyor. Çıkmak için Ctrl+C.")
        time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı.")