# This is Day 54 project : Mini Chatbot

import re
import random
import datetime
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 0.9)

def speak(text):
    """Convert chatbot response into speech."""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print("(TTS unavailable)")

user_name = None

greeting_responses = [
    "Hi there! 👋 How can I help you today?",
    "Hello! 😊 It's nice to chat with you!",
    "Hey! 🤖 What can I do for you?",
    "Hi! 👋 Ask me anything!"
]

positive_responses = [
    "That's wonderful to hear! 😊",
    "I'm glad you're feeling good! 🌟",
    "That's great! Keep that positive energy going! 😄",
    "Awesome! 🎉 I'm happy for you!"
]

negative_responses = [
    "I'm sorry you're feeling this way. ❤️",
    "That sounds difficult. I'm here to listen. 🤗",
    "I'm sorry you're going through that. Things can get better. 🌱",
    "It sounds like you're having a tough time. Take a deep breath. 💙"
]

neutral_responses = [
    "I understand. 🤔",
    "Thanks for sharing that with me.",
    "I see! Tell me more. 😊"
]

positive_words = {"happy", "great", "good", "awesome", "excellent", "amazing", "wonderful", "love", "like", "excited", "fantastic", "best", "enjoy"}
negative_words = {"sad", "bad", "angry", "hate", "terrible", "awful", "worried", "stress", "stressed", "depressed", "upset", "lonely", "frustrated", "frustrating", "disappointed", "tired", "hurt", "problem"}

def analyze_sentiment(text):
    """ Simple keyword-based sentiment analysis. 
    
    Returns: positive, negative, neutral"""

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    
    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    return "neutral"

def calculate_expression(expression):
    """ Safely calculate simple arithmetic expressions.

    Supports:
        +
        -
        *
        /
        %
    """

    expression = expression.replace(" ", "")
    if not re.fullmatch(r"[0-9+\-*/%.()]+", expression):
        return None

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception:
        return None

def get_response(user_input):
    global user_name
    text = user_input.strip()
    text_lower = text.lower()

    if re.search(r"\b(exit|quit|goodbye|bye|see you)\b", text_lower):
        return "Goodbye! 👋 Have a wonderful day! 😊"

    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text_lower):
        if user_name:
            return random.choice([
                f"Hello, {user_name}! 👋 How can I help you?",
                f"Hey {user_name}! 😊 What would you like to talk about?",
                f"Hi {user_name}! 🤖 Nice to see you again!"
            ])
        return random.choice(greeting_responses)

    name_match = re.search(r"(?:my name is|i am|i'm|call me)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+)*)", text_lower)
    if name_match:
        user_name = name_match.group(1).title()
        return (f"Nice to meet you, {user_name}! 😊 "
            f"I'll remember your name during this conversation.")

    if re.search(r"\b(what is my name|what's my name|do you know my name)\b", text_lower):
        if user_name:
            return f"Your name is {user_name}! 😊"
        return "I don't know your name yet. You can tell me by saying 'My name is ...'."

    if re.search(r"\b(your name|who are you|what are you)\b", text_lower):
        return ("I'm Mini Chatbot 🤖, a Python-based virtual assistant with regex matching, sentiment analysis and text-to-speech!")

    if re.search(r"\b(how are you|how're you|how are you doing|are you okay)\b", text_lower):
        return random.choice([
            "I'm doing great! 🤖 Thanks for asking! 😊",
            "I'm feeling fantastic and ready to help! 🚀",
            "I'm doing well! How are you feeling today? 😊"
        ])

    if re.search(r"\b(help|what can you do|commands|features)\b", text_lower):
        return ("I can help with several things! 🤖\n"
            "• Greetings 👋\n"
            "• Remember your name 🧠\n"
            "• Date and time 📅\n"
            "• Basic calculations 🧮\n"
            "• Sentiment-aware conversations ❤️\n"
            "• General questions 💬\n"
            "• Text-to-speech 🔊")

    if re.search(r"\b(what time is it|current time|tell me the time|time now)\b", text_lower):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. ⏰"

    if re.search(r"\b(what date is it|today's date|todays date|current date|what day is it)\b", text_lower):
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {current_date}. 📅"

    if re.search(r"\b(thank you|thanks|thank u|thx)\b", text_lower):
        return random.choice([
            "You're very welcome! 😊",
            "No problem! 🤝",
            "Anytime! 😄",
            "Happy to help! 🌟"
        ])

    if re.search(r"\b(joke|make me laugh|tell me something funny)\b", text_lower):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why was the Python programmer confused? Because they couldn't find the right indentation! 🐍😂",
            "There are only 10 kinds of people: those who understand binary and those who don't. 😄"
        ]
        return random.choice(jokes)

    math_match = re.search(r"(?:calculate|what is|solve)\s+([0-9+\-*/%.() ]+)", text_lower)
    if math_match:
        expression = math_match.group(1)
        result = calculate_expression(expression)

        if result is not None:
            return f"The answer is {result}. 🧮"
        return "I couldn't calculate that expression. 🤔"

    sentiment = analyze_sentiment(text_lower)
    if sentiment == "positive":
        return random.choice(positive_responses)

    if sentiment == "negative":
        return random.choice(negative_responses)

    if re.search(r"^(what|why|when|where|who|how|can|could|would|is|are|do|does)\b", text_lower):
        return ("That's an interesting question! 🤔 "
            "I'm still a simple chatbot, so I may not know the answer to every question. Try asking me about my features!")

    return random.choice([
        "I'm not completely sure how to respond to that. 🤔",
        "Interesting! Tell me a little more. 😊",
        "I understand. Could you explain that differently? 💬",
        "I'm still learning! 🤖 Try asking me something else.",
        "Hmm... that's something I'll need to think about. 🧠"
    ])

def chatbot():
    print("=" * 55)
    print("              🤖 MINI CHATBOT")
    print("=" * 55)

    print("\nHello! 👋 I'm your Python Mini Chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'exit' to end the conversation.")
    print("-" * 55)

    speak("Hello! I'm your Python Mini Chatbot. How can I help you?")

    while True:
        user_input = input("\nYou : ").strip()
        if not user_input:
            print("Chatbot : Please say something! 😊")
            continue

        response = get_response(user_input)
        print(f"Chatbot : {response}")
        speak(response)

        if re.search(r"\b(exit|quit|goodbye|bye|see you)\b", user_input.lower()):
            break
        
if __name__ == "__main__":
    chatbot()
    
# Done