# main class for the rule base bot
class Crypto_Buddy_Bot:
    def __init__(self):
        #crypto info
        self.crypto_data = {
            "bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "description": "Bitcoin is the pioneer cryptocurrency, known for its decentralized nature and store of value."
            },
            "ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "description": "Ethereum is a blockchain platform that enables smart contracts and decentralized applications (dApps)."
            },
            "cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "description": "Cardano is a proof-of-stake blockchain platform aiming for security, scalability, and sustainability."
            }
        }
        # General responses 
        self.general_phrases = {
            "hello": "Hello! I am Crypto Buddy. How can I assist you today?",
            "hi": "Hello! I am Crypto Buddy. How can I assist you today?",
            "thank you": "You're welcome! I am here to help you anytime with anything. Don't hesitate to reach out."
        }
        
        # quick access of the crypto data
        self.crypto_keywords = list(self.crypto_data.keys())

    def respond(self, message):
        message = message.lower().strip()
        for key, reply in self.general_phrases.items():
            if key in message:
                return reply

        # check for users asking about a specific crypto
        keywords = ["sustainable", "eco-friendly", "efficient", "long-term", "favourable", "good", "bad", "good", "best", "favourable", "recommend", "recommended"]

        if any(keyword in message for keyword in keywords):
            # filter to iterate to only crypto with high sustainability score
            sustainable_cryptos = []
            for name_key, data_value in self.crypto_data.items():
                if 'sustainability_score' in data_value:
                    sustainable_cryptos.append((name_key, data_value['sustainability_score']))

            if sustainable_cryptos:
                recommend_crypto_name = max(sustainable_cryptos, key=lambda x: x[1])[0]
                # Access the full data for the recommended crypto to give a better response
                recommend_data = self.crypto_data[recommend_crypto_name]

                return (f"For sustainability, I recommend {recommend_crypto_name}! 🌱 "
                        f"It has a sustainability score of {recommend_data['sustainability_score']:.0%} "
                        f"and its energy use is {recommend_data['energy_use']}. "
                        f"It's eco-friendly and has long-term potential!")
            else:
                return "Hmm. I am not sure what you asked. Try to ask more about a specific crypto."
            
        for crypto_name in self.crypto_keywords:
            if crypto_name in message:
                crypto_info = self.crypto_data[crypto_name]
                #response from the bot
                response = (f"Here's some information about {crypto_name.capitalize()}:\n"
                            f"- Price Trend: {crypto_info['price_trend'].capitalize()}\n"
                            f"- Market Cap: {crypto_info['market_cap'].capitalize()}\n"
                            f"- Energy Use: {crypto_info['energy_use'].capitalize()}\n"
                            f"- Sustainability Score: {crypto_info['sustainability_score']:.0%}\n"
                            f"- Description: {crypto_info['description']}")
                return response

        # Default response
        return "Sorry, I don't understand your request about cryptocurrency. I am still learning."

# Run the bot
if __name__ == "__main__":
    chatbot = Crypto_Buddy_Bot()
    print("Hey there! Let’s find you a green and growing crypto!\n")

    while True:
        user_input = input("User: ")
        if user_input.lower().strip() in ["quit", "exit", "goodbye"]:
            print("\nCrypto Buddy: Goodbye! Come back anytime.\n")
            break
        
        bot_response = chatbot.respond(user_input)
        print("Crypto Buddy:", bot_response)