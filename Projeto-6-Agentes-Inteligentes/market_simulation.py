import autogen
import random

class PlayerAgent(autogen.Agent):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance
        self.items = 0

    def decide(self, price):
        if price < 12 and self.balance >= price:
            if random.random() < 0.7:
                return 'buy'
        if price > 13 and self.items > 0:
            if random.random() < 0.7:
                return 'sell'
        if self.balance >= price and random.random() < 0.1:
            return 'buy'
        if self.items > 0 and random.random() < 0.1:
            return 'sell'
        return 'wait'

class MarketAgent(autogen.Agent):
    def __init__(self, initial_price):
        super().__init__("Market")
        self.price = initial_price

    def adjust_price(self, buys, sells):
        if buys > sells:
            self.price += 1
        elif sells > buys:
            self.price -= 1
        self.price = max(1, self.price)

if __name__ == "__main__":
    market = MarketAgent(initial_price=8)
    players = [PlayerAgent(f'Player{i}', balance=100) for i in range(3)]

    for round in range(20):
        buys = sells = 0
        print(f"\n--- Round {round+1} ---")
        for player in players:
            action = player.decide(market.price)
            if action == 'buy':
                player.balance -= market.price
                player.items += 1
                buys += 1
            elif action == 'sell':
                player.balance += market.price
                player.items -= 1
                sells += 1
            print(f"{player.name}: ação = {action}, saldo = {player.balance}, itens = {player.items}")
        market.adjust_price(buys, sells)
        print(f"Compras: {buys}, Vendas: {sells}")
        print(f"Preço do mercado: {market.price}")
