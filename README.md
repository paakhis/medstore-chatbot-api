# Backend Chatbot API using Flask

A backend-focused chatbot system built using **Flask**, demonstrating **REST API design**, **intent-based request handling**, and **structured backend logic** for handling user queries in an eCommerce-style environment.

---

## Key Features

- RESTful API endpoint for handling user queries
- Intent-based routing for predictable responses
- Modular backend structure (separation of logic and routing)
- Fallback NLP integration using ChatterBot
- Clean request → processing → response flow

---

## Tech Stack

- Python
- Flask (Backend API)
- ChatterBot (NLP integration)
- HTML/CSS (basic interface)

---

## How It Works

The system processes user requests through a structured backend flow:
### 1. API Layer
- Handles incoming HTTP requests
- Extracts user input

### 2. Intent-Based Routing
- Identifies user intent using keyword-based logic
- Routes request to appropriate handler

### 3. Response Generation
- Returns domain-specific responses (products, orders, etc.)
- Falls back to NLP model for general queries

