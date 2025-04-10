# LLM-Based Mental Health Chatbot with Mobile App Integration

This project integrates a **mental health chatbot** powered by a **Large Language Model (LLM)** from Hugging Face and a **mobile app** to provide users with a conversational experience. The chatbot is designed to respond empathetically to user input, providing mental health support in a conversational format.

The mobile app allows users to interact with the chatbot on their smartphones, making it accessible and easy to use anywhere.

## Features

- **Mental Health Chatbot**: The chatbot provides supportive, empathetic, and brief responses to mental health-related inquiries.
- **Mobile App Integration**: The chatbot is integrated with a mobile app, allowing users to chat directly from their phones.
- **User-Friendly Interface**: A simple interface on the mobile app for smooth and seamless interaction.
- **Privacy-First**: User interactions are not stored or used for any other purposes, ensuring privacy and confidentiality.

## How It Works

The backend API (built with **Flask**) handles user requests and forwards them to the Hugging Face API for response generation. The steps for the backend and mobile app work together as follows:

### Backend (Flask API)

1. **User Input**: The mobile app sends a user’s message (e.g., "I feel anxious") to the backend API.
2. **Request to Hugging Face**: The Flask app formats the input into a prompt and sends it to the Hugging Face model API (e.g., `mistralai/Mistral-7B-Instruct-v0.1`).
3. **Response Generation**: The model generates a response based on the user’s input. The response is intended to be brief, empathetic, and helpful.
4. **Return Response**: The Flask app receives the generated response from Hugging Face and sends it back to the mobile app.
5. **Display on Mobile App**: The mobile app receives the response and displays it on the screen.

### Mobile App

1. **User Interaction**: The user opens the mobile app, which features a simple chat interface.
2. **Sending Message**: The user types a message (e.g., "I am feeling stressed") and presses send.
3. **API Call**: The app makes a `POST` request to the backend API, passing the user’s message.
4. **Displaying Response**: Upon receiving the chatbot's response from the backend, the app displays the generated response in the chat interface.

## Prerequisites

To run this project, ensure you have the following:

- **Python 3.6+** for backend setup
- **pip** for installing Python dependencies
- **Mobile Development Environment** (React Native, Flutter, etc.) for the app
- **Hugging Face API Token**: You’ll need a Hugging Face API token to interact with the model.

## Setup and Installation

### Backend Setup (Flask API)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Vansh-1007/Cloud-Computing-Project.git
   cd mental-health-chatbot

