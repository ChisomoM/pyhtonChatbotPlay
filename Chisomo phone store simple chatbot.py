import random

# Define the chat bot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! Welcome to Chisomo's Phone World."],
    "bye": ["Goodbye!", "See you later!", "Thank you for visiting Chisomo's Phone World!"],
    "userName": ["Nice choice! Please provide us with your name", "Nice choice! Please give us your name"],
    "iphone": ["Sure, we have iPhone 12, iPhone 13 and iPhone 14 in stock. Which one are you interested in buying?", "We have iPhone 12, iPhone 13 and iPhone 14 in stock. Which one would you like?"],
    "samsung": ["Sure, we have Samsung S20, Samsung S21 and Samsung S22 in stock. Which one are you interested in buying?", "We have Samsung S20, Samsung S21 and Samsung S22 in stock. Which model would you like?"],
    "googlePixel": ["Sorry, Google Pixel phones are not available.", "Sorry, Google Pixel phones are currently out of stock."],
    "location": ["Thanks, Please provide us with your address so we can arrange delivery.", "Thanks, We'll need your address for the delivery."],
    "phoneNumber": ["Thank you! Lastly, please provide your phone number so we can contact you.", "Thank you for providing your address. Can you also give us your phone number for contact purposes?"],
    "default": ["I'm sorry, I couldn't quite catch that. Can you please rephrase?", "I'm not sure I understand. Could you provide more details?", "I'm here to assist you with phones. Can you tell me more about what you're looking for?"]
}

# Function to get a response based on user input
def getResponse(userInput):
    userInput = userInput.lower()
    
    for pattern, responseList in responses.items():
        if pattern in userInput:
            return random.choice(responseList)
    
    return random.choice(responses["default"])

# Main function for the chat bot
def main():
    print("ChatBot: Hello! Welcome to Chisomo's Phone World, your source for the latest smartphones.")
    print("ChatBot: How can I assist you today? You can ask about iPhones, Samsung phones, or Google Pixel.")
    
    while True:
        userInput = input("You: ")
        if userInput.lower() == "exit":
            print("ChatBot: Thank you for visiting Chisomo's Phone World. Have a great day!")
            break

        response = getResponse(userInput)
        print("ChatBot:", response)
        
        if "iphone" in userInput or "samsung" in userInput:
            print("ChatBot:", random.choice(responses["userName"]))
            userName = input("You: ")
            print("ChatBot:", random.choice(responses["location"]))
            address = input("You: ")
            print("ChatBot:", random.choice(responses["phoneNumber"]))
            phoneNumber = input("You: ")
            
            # Create a text file with the order details
            orderDetails = f"Order Details:\nPhone Model: {userInput}\nName: {userName} \nAddress: {address}\nPhone Number: {phoneNumber}\n"
            with open(f"{userName} order.txt", "w") as file:
                file.write(orderDetails)
            
            print(f"ChatBot: Thank you! Your order has been placed and order details have been saved to '{userName} order.txt'. We will contact you shortly for confirmation.")

# Run the chat bot
if __name__ == "__main__":
    main()