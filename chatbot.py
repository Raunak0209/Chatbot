import nltk
from nltk.chat.util import Chat, reflections

# Extended conversation patterns
pairs = [
    # Greeting and basic responses
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there! How can I assist you today?", "Hi! How's it going?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Raunak. You can call me Chatbot!"]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you! How about you?"]
    ],
    [
        r"fine",
        ["Great to hear that! Do you have any other questions?"]
    ],

    # Apology
    [
        r"sorry (.*)",
        ["No worries! It's all good.", "Apologies accepted!"]
    ],

    # User's current state
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to know that you're feeling %1!"]
    ],

    # Age question
    [
        r"(.*) age?",
        ["I am just a program, so I don't have an age, but I can help you with other things!"]
    ],

    # General query
    [
        r"what (.*) want?",
        ["I want to help you with your queries and make your day better!"]
    ],

    # Creation of the chatbot
    [
        r"(.*) created?",
        ["I was created by Raunak using Python's NLTK library. Cool, right?"]
    ],

    # Location or city
    [
        r"Who are you?",
        ["I am a chatbot created by Raunak"]
    ],

    # Weather-related queries
    [
        r"how is the weather?",
        ["I don't have access to live weather data, but you can check it online or on your phone by searching live weather!"]
    ],

    # Farewell
    [
        r"quit",
        ["Bye! Take care, see you soon! Have a great day!"]
    ],

    # Asking for help
    [
        r"can you help me?",
        ["Of course! I'm here to help. What do you need assistance with?"]
    ],

    # Answering about hobbies or interests
    [
        r"what are your hobbies?",
        ["I don't have personal hobbies, but I'm happy to talk about yours! What do you enjoy doing?"]
    ],

    # Question about programming
    [
        r"tell me about programming",
        ["Programming is a fun and creative way to solve problems using code. What language are you learning?"]
    ],

    # Simple math queries
    [
        r"(.*) add (.*)",
        ["You want me to add? Sure! What numbers should I add for you?"]
    ],
    [
        r"(.*) multiply (.*)",
        ["You want multiplication? I can do that! Just give me the numbers."]
    ],

    # Information about AI
    [
        r"what is AI?",
        [
            "AI (Artificial Intelligence) is the simulation of human intelligence in machines that are programmed to think and learn."]
    ],

    # Asking for chatbot’s capabilities
    [
        r"what can you do?",
        ["I can answer your questions, chat with you, and help you learn. What would you like to know or do?"]
    ],

    # Other generic responses for unmatched queries
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?", "Could you clarify what you mean?",
         "Hmm... I'm not sure how to respond to that."]
    ]
]

# Reflections: this will help to reverse some user input patterns (like "I am" to "you are")
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}


# Function to start the chatbot
def chatbot():
    print("Hi, I'm the chatbot created by Raunak. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()
