# Mock Interview Flask App with OpenAI Integration

![Mock Interview App](mock-interview.png)

## Overview

This Flask-based web application serves as a platform for conducting mock interviews, harnessing OpenAI's powerful text generation capabilities. The app generates tailored interview questions, evaluates code submissions, and provides an interactive environment for interview simulations.

### Features

- **Interview Setup:** Enter your name, select a company of interest, and provide your OpenAI API key to initiate the mock interview process.
- **Dynamic Question Generation:** OpenAI's GPT-3 model generates interview questions based on the chosen company, ensuring relevant and diverse scenarios.
- **Code Submission & Evaluation:** Users can submit code solutions to the generated questions for evaluation against predefined criteria.
- **Timer Functionality:** An integrated timer helps track the interview duration, ensuring a realistic simulation.

## Technologies Used

- **Flask:** Backend web framework facilitating HTTP request handling and routing.
- **OpenAI API:** Integration with OpenAI's text generation API for question generation and code evaluation.
- **HTML/CSS/JS:** Frontend interface for user interaction and presentation of interview questions.
- **Docker:** Dockerized deployment for streamlined setup and portability across environments.

## Getting Started

### Build and Run the Docker Image:

docker build -t mock-interview-app .
docker run -p 5000:5000 -d mock-interview-app

### Access the App:
Visit http://localhost:5000 in your web browser to start using the app.

### Usage

Setup:
Enter your name, choose a company of interest, and provide your OpenAI API key to initialize the interview.
Interview Simulation:
Receive dynamically generated interview questions based on the selected company.
Code Submission:
Submit code solutions for evaluation against the provided questions.
Timer Tracking:
Keep track of the interview duration to simulate real-time constraints.
