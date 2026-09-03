# 🤖 Day 54 - Mini Chatbot

Welcome to **Day 54** of my **100 Days, 100 Python Projects** challenge!

This project is a **Mini Chatbot** built using **Python, Regular Expressions, Random, DateTime, and Text-to-Speech**.

The chatbot can hold a simple interactive conversation with the user, recognize common commands and questions, remember the user's name during the conversation, perform basic calculations, detect simple sentiment from text, provide the current date and time, tell jokes, and respond using **text-to-speech**.

The main purpose of this project is to gain practical experience with **Python automation, string processing, regular expressions, conditional logic, sentiment analysis basics, and text-to-speech functionality**.

---

## 📌 Project Overview

Chatbots are software applications that interact with users through natural language.

This project implements a simple **rule-based chatbot** that analyzes the user's input and selects an appropriate response based on predefined patterns and keywords.

The chatbot uses **Regular Expressions (Regex)** to identify different types of user input and provides different responses depending on what the user says.

Users can:

* 👋 Start a conversation
* 🧠 Tell the chatbot their name
* 💬 Ask about the chatbot
* ❤️ Have sentiment-aware conversations
* ⏰ Ask for the current time
* 📅 Ask for today's date
* 🧮 Perform basic calculations
* 😂 Ask for jokes
* ❓ Ask for help and available features
* 🔊 Hear chatbot responses using text-to-speech
* 👋 End the conversation using commands such as `exit` or `bye`

---

## ✨ Features

* 🤖 Interactive command-line chatbot
* 👋 Greeting recognition
* 🧠 Remembers user's name during the conversation
* 🔍 Regex-based input matching
* ❤️ Simple keyword-based sentiment analysis
* 😊 Positive sentiment responses
* 😔 Negative sentiment responses
* 😐 Neutral sentiment responses
* ⏰ Current time detection
* 📅 Current date detection
* 🧮 Basic arithmetic calculations
* ➕ Addition support
* ➖ Subtraction support
* ✖️ Multiplication support
* ➗ Division support
* `%` Modulo support
* 🧮 Parentheses support in calculations
* 😂 Random programming jokes
* ❓ Help and feature detection
* 💬 General question handling
* 🎲 Randomized chatbot responses
* 🔊 Text-to-speech functionality
* ⚠️ Input validation
* 🛡️ Safe arithmetic expression validation
* 🚪 Exit commands
* 💻 Simple command-line interface

---

## 🖥️ Application Interface

The chatbot runs directly in the **terminal / command prompt**.

When the application starts, it displays a welcome message and provides instructions for interacting with the chatbot.

Example:

```text
=======================================================
              🤖 MINI CHATBOT
=======================================================

Hello! 👋 I'm your Python Mini Chatbot.
Type 'help' to see what I can do.
Type 'exit' to end the conversation.
-------------------------------------------------------
```

The user can then enter messages interactively:

```text
You : Hello
Chatbot : Hi there! 👋 How can I help you today?

You : My name is Abhijit
Chatbot : Nice to meet you, Abhijit! 😊

You : What is my name?
Chatbot : Your name is Abhijit! 😊
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re`)**
* **Random (`random`)**
* **DateTime (`datetime`)**
* **pyttsx3**

### Python

Python is used to develop the complete chatbot logic, including:

* User input handling
* Pattern matching
* Response generation
* Sentiment analysis
* Calculations
* Date and time processing
* Conversation management

### Regular Expressions

The `re` module is used extensively for recognizing patterns in user input.

For example, the chatbot can recognize different greeting variations:

```python
re.search(
    r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
    text_lower
)
```

Regex is also used to:

* Detect exit commands
* Detect questions
* Extract the user's name
* Detect mathematical expressions
* Identify keywords

### Random

The `random` module is used to select different responses from predefined response lists.

For example:

```python
random.choice(greeting_responses)
```

This prevents the chatbot from giving exactly the same response every time.

### DateTime

The `datetime` module is used to provide the current date and time.

Example:

```python
datetime.datetime.now().strftime("%I:%M %p")
```

### pyttsx3

`pyttsx3` is used to convert chatbot responses from text into speech.

The project configures the speech engine using:

```python
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 0.9)
```

---

## 📂 Project Structure

```text
DAY_54/
│
├── main54.py
├── requirements.txt
└── README.md
```

### File Description

| File               | Purpose                  |
| ------------------ | ------------------------ |
| `main54.py`        | Main chatbot application |
| `requirements.txt` | Python dependency list   |
| `README.md`        | Project documentation    |

---

## 📦 requirements.txt

The project requires the following external Python library:

```text
pyttsx3
```

Install the dependency using:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install pyttsx3
```

The following modules are part of Python's standard library and do not require separate installation:

```text
re
random
datetime
```

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

### 2. Open the project folder

Open a terminal inside the `DAY_54` folder.

### 3. Install the required dependency

```bash
pip install -r requirements.txt
```

### 4. Run the chatbot

```bash
python main54.py
```

The chatbot will start in the terminal.

---

## 💬 How to Use

After launching the program, enter messages in the terminal.

The chatbot will process your input and provide a response.

### 👋 Greetings

You can use:

```text
Hello
Hi
Hey
Good morning
Good afternoon
Good evening
```

Example:

```text
You : Hello
Chatbot : Hey! 🤖 What can I do for you?
```

The chatbot randomly selects a greeting response.

---

## 🧠 Remembering Your Name

The chatbot can remember your name during the current conversation.

You can introduce yourself using phrases such as:

```text
My name is Abhijit
I am Abhijit
I'm Abhijit
Call me Abhijit
```

Example:

```text
You : My name is Abhijit

Chatbot : Nice to meet you, Abhijit! 😊
I'll remember your name during this conversation.
```

You can then ask:

```text
You : What is my name?

Chatbot : Your name is Abhijit! 😊
```

The name is stored in the variable:

```python
user_name = None
```

and updated when the chatbot detects a name introduction.

---

## 🤖 Asking About the Chatbot

The chatbot can respond to questions such as:

```text
What is your name?
Who are you?
What are you?
```

Example:

```text
You : Who are you?

Chatbot : I'm Mini Chatbot 🤖, a Python-based virtual assistant
with regex matching, sentiment analysis and text-to-speech!
```

---

## ❓ Help Command

The user can type:

```text
help
```

or:

```text
What can you do?
commands
features
```

The chatbot displays its available capabilities.

Example:

```text
You : help

Chatbot : I can help with several things! 🤖
• Greetings 👋
• Remember your name 🧠
• Date and time 📅
• Basic calculations 🧮
• Sentiment-aware conversations ❤️
• General questions 💬
• Text-to-speech 🔊
```

---

## ❤️ Sentiment Analysis

The chatbot includes a simple **keyword-based sentiment analysis system**.

It maintains two sets of words:

### Positive Words

```python
positive_words = {
    "happy", "great", "good", "awesome",
    "excellent", "amazing", "wonderful",
    "love", "like", "excited",
    "fantastic", "best", "enjoy"
}
```

### Negative Words

```python
negative_words = {
    "sad", "bad", "angry", "hate",
    "terrible", "awful", "worried",
    "stress", "stressed", "depressed",
    "upset", "lonely", "frustrated",
    "frustrating", "disappointed",
    "tired", "hurt", "problem"
}
```

The chatbot extracts words from the user's message using:

```python
re.findall(r"\b[a-zA-Z]+\b", text.lower())
```

It then calculates positive and negative scores.

If:

```text
Positive Score > Negative Score
```

the chatbot identifies the message as:

```text
positive
```

If:

```text
Negative Score > Positive Score
```

it identifies the message as:

```text
negative
```

Otherwise:

```text
neutral
```

---

## 😊 Positive Responses

When positive sentiment is detected, the chatbot randomly selects a response.

Example:

```text
You : I am feeling amazing today!

Chatbot : That's wonderful to hear! 😊
```

Possible responses include:

```text
That's wonderful to hear! 😊
I'm glad you're feeling good! 🌟
That's great! Keep that positive energy going! 😄
Awesome! 🎉 I'm happy for you!
```

---

## 😔 Negative Responses

When negative sentiment is detected, the chatbot provides an empathetic response.

Example:

```text
You : I am feeling stressed.

Chatbot : That sounds difficult. I'm here to listen. 🤗
```

Possible responses include:

```text
I'm sorry you're feeling this way. ❤️
That sounds difficult. I'm here to listen. 🤗
I'm sorry you're going through that. Things can get better. 🌱
It sounds like you're having a tough time. Take a deep breath. 💙
```

---

## 😐 Neutral Responses

If the chatbot cannot identify a strong positive or negative sentiment, it provides a neutral response.

Example:

```text
You : I went to college today.

Chatbot : Thanks for sharing that with me.
```

---

## 🧮 Basic Calculator

The chatbot can perform simple arithmetic calculations.

Supported operators include:

```text
+
-
*
/
%
()
```

Examples:

```text
calculate 10 + 5
```

```text
what is 25 * 4
```

```text
solve 100 / 5
```

Example conversation:

```text
You : calculate 25 * 4

Chatbot : The answer is 100.0. 🧮
```

Another example:

```text
You : what is (10 + 5) * 2

Chatbot : The answer is 30. 🧮
```

---

## 🛡️ Safe Expression Validation

Before evaluating a mathematical expression, the chatbot validates the input using a regular expression.

```python
if not re.fullmatch(r"[0-9+\-*/%.()]+", expression):
    return None
```

This ensures that only supported mathematical characters are accepted.

The calculation is then performed using:

```python
eval(expression, {"__builtins__": None}, {})
```

The use of restricted built-ins prevents access to normal Python built-in functions through the expression evaluator.

Invalid calculations are handled gracefully:

```text
Chatbot : I couldn't calculate that expression. 🤔
```

---

## ⏰ Date and Time

The chatbot can provide the current time.

Users can ask:

```text
What time is it?
Current time
Tell me the time
Time now
```

Example:

```text
You : What time is it?

Chatbot : The current time is 08:30 PM. ⏰
```

The time is generated dynamically using:

```python
datetime.datetime.now()
```

---

## 📅 Current Date

The chatbot can also provide the current date.

Users can ask:

```text
What is today's date?
What date is it?
Current date
What day is it?
```

Example:

```text
You : What date is it?

Chatbot : Today is Thursday, 03 September 2026. 📅
```

The date is formatted using:

```python
strftime("%A, %d %B %Y")
```

---

## 😂 Joke Feature

The chatbot includes a collection of programming jokes.

Users can type:

```text
Tell me a joke
Make me laugh
Tell me something funny
```

Example:

```text
You : Tell me a joke

Chatbot : Why do programmers prefer dark mode?
Because light attracts bugs! 🐛😂
```

The chatbot randomly selects a joke using:

```python
random.choice(jokes)
```

---

## 🔊 Text-to-Speech

One of the main features of this project is **Text-to-Speech (TTS)**.

After generating a response, the chatbot calls:

```python
speak(response)
```

The `speak()` function uses `pyttsx3` to convert text into speech.

```python
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print("(TTS unavailable)")
```

This allows the chatbot to both:

* 🖥️ Display the response in the terminal
* 🔊 Speak the response aloud

The speech rate is configured to:

```text
165 words per minute
```

and the volume is configured to:

```text
0.9
```

If text-to-speech is unavailable, the program catches the exception and continues running.

---

## 🚪 Exit Commands

The conversation can be ended using commands such as:

```text
exit
quit
goodbye
bye
see you
```

Example:

```text
You : bye

Chatbot : Goodbye! 👋 Have a wonderful day! 😊
```

The chatbot then exits the conversation loop.

---

## 🔍 Regular Expression Patterns Practiced

This project provides practical experience with Python Regex.

### Greeting Detection

```python
r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b"
```

### Exit Detection

```python
r"\b(exit|quit|goodbye|bye|see you)\b"
```

### Name Extraction

```python
r"(?:my name is|i am|i'm|call me)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+)*)"
```

### Mathematical Expression Detection

```python
r"(?:calculate|what is|solve)\s+([0-9+\-*/%.() ]+)"
```

### Question Detection

```python
r"^(what|why|when|where|who|how|can|could|would|is|are|do|does)\b"
```

Regex allows the chatbot to recognize different forms of user input without requiring exact string matches.

---

## 🔄 Chatbot Processing Flow

The chatbot follows a simple rule-based processing pipeline:

```text
User Input
     │
     ▼
Clean Input
     │
     ▼
Convert to Lowercase
     │
     ▼
Check Exit Command
     │
     ▼
Check Greeting
     │
     ▼
Check Name
     │
     ▼
Check Identity Questions
     │
     ▼
Check Help Command
     │
     ▼
Check Date / Time
     │
     ▼
Check Joke Request
     │
     ▼
Check Mathematical Expression
     │
     ▼
Analyze Sentiment
     │
     ▼
Check General Question
     │
     ▼
Generate Response
     │
     ▼
Display Response
     │
     ▼
Text-to-Speech
```

---

## 🧩 Main Functions

| Function                 | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| `speak()`                | Converts chatbot response into speech                |
| `analyze_sentiment()`    | Detects positive, negative, or neutral sentiment     |
| `calculate_expression()` | Safely evaluates supported arithmetic expressions    |
| `get_response()`         | Processes user input and generates chatbot responses |
| `chatbot()`              | Runs the main interactive conversation loop          |

---

## 🖥️ Python Concepts Practiced

This project uses several important Python concepts.

### Variables

Used for storing:

* User name
* Chatbot state
* Scores
* Expressions
* Responses

### Lists

Used to store:

* Greetings
* Positive responses
* Negative responses
* Neutral responses
* Jokes

### Sets

Used to store sentiment keywords:

```python
positive_words = {...}
negative_words = {...}
```

### Functions

The project is divided into multiple reusable functions.

### Conditional Statements

Used to determine which response should be generated.

### Loops

The main chatbot conversation uses:

```python
while True:
```

to continuously receive user input.

### Exception Handling

`try-except` blocks prevent the program from crashing when:

* Text-to-speech fails
* An invalid calculation is entered

### Regular Expressions

Used for flexible natural-language pattern recognition.

### String Processing

The project makes extensive use of:

```python
strip()
lower()
replace()
split()
```

and regular-expression processing.

---

## 📚 Concepts Practiced

* Python Programming
* Functions
* Lists
* Sets
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* String Manipulation
* Regular Expressions
* Pattern Matching
* Keyword Matching
* Rule-Based Chatbots
* Basic Sentiment Analysis
* Text-to-Speech
* Date and Time Handling
* Randomized Responses
* Arithmetic Expression Processing
* User Input Handling
* Command-Line Applications

---

## 🎯 Learning Outcome

This project helped me understand:

* How to build a simple rule-based chatbot
* How to process natural-language-like user input
* How Regular Expressions can be used for pattern matching
* How to extract information from text
* How to implement keyword-based sentiment analysis
* How to generate different responses using random selection
* How to use Python's `datetime` module
* How to perform basic arithmetic calculations programmatically
* How to validate mathematical expressions
* How to use exception handling for safer applications
* How to integrate text-to-speech into a Python project
* How to maintain simple conversation state
* How to structure a Python application using reusable functions
* How rule-based chatbots differ from modern AI/LLM-based chatbots

---

## ⚠️ Limitations

This project is intentionally designed as a **simple rule-based chatbot**.

It does not use:

* Large Language Models
* Machine Learning models
* Neural Networks
* External AI APIs
* Internet-based knowledge retrieval

Therefore, the chatbot cannot understand arbitrary questions like a modern AI assistant.

Its responses are based on:

```text
Regex Patterns
+
Keywords
+
Predefined Responses
```

The user's name is also remembered only **during the current program execution** and is not stored permanently.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* 🧠 Add machine-learning-based intent classification
* 🤖 Integrate an LLM API
* 💾 Store conversation history
* 🗃️ Save user preferences
* 🧠 Add persistent user memory
* 🌐 Convert the chatbot into a web application
* 🎨 Create a graphical chatbot interface using Tkinter
* 💬 Add more conversation intents
* 🌍 Support multiple languages
* 🎙️ Add speech-to-text input
* 🔊 Add selectable voices
* ⚙️ Add configurable speech rate and volume
* 📚 Connect the chatbot to external knowledge sources
* 🧮 Add advanced mathematical calculations
* 📊 Add conversation analytics
* 🧪 Add automated chatbot tests
* 🔐 Improve expression evaluation further
* 📝 Add conversation logging
* 🌐 Build a Flask-based chatbot API
* 💻 Create a desktop GUI chatbot

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, learn new technologies, and maintain consistency through daily coding.

**Day 54** focuses on **Chatbot Development fundamentals**, combining **Regular Expressions for pattern recognition**, **keyword-based sentiment analysis**, **Python logic for conversation handling**, and **pyttsx3 for text-to-speech** to create a simple interactive virtual assistant.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🤖
