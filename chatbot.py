from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
CB = ChatBot(
    'MedStoreBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I didn’t understand that. You can ask about products or orders.',
            'maximum_similarity_threshold': 0.65
        }
    ]
)

# Domain-specific training
conversation = [
    "hello",
    "Hi, welcome to MedStore Assistant!",

    "hi",
    "Hello! How can I assist you today?",

    "what products do you have",
    "We offer ECG machines, monitors, and diagnostic devices.",

    "do you have products",
    "Yes, we offer medical devices like ECG machines and monitors.",

    "where is my order",
    "Please provide your order ID to check status.",

    "order status",
    "Please provide your order ID to check status.",

    "thank you",
    "You're welcome!",

    "bye",
    "Goodbye! Have a great day."
]

trainer = ListTrainer(CB)
trainer.train(conversation)