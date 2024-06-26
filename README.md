
# Salat

Salat is a chat interface built using Flask, a lightweight WSGI web application framework in Python.

## Features

- Simple chat interface
- Responsive web design

## Getting Started

### Prerequisites

- Docker installed on your machine

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/svXaverius/Salat.git
   cd Salat
   ```

### Running the Application

1. Build and run the Docker container:

   ```sh
   docker build -t salat-app .
   docker run -p 5000:5000 salat-app
   ```

2. Open your browser and navigate to `http://localhost:5000` to access the chat interface.

## Directory Structure

- `static/`: Static files (CSS, JavaScript, images)
- `templates/`: HTML templates
- `answergen.py`: Script for generating answers
- `app.py`: Main application file
- `index.html`: Main HTML file
- `requirements.txt`: Project dependencies

## License

This project is licensed under the MIT License.

## Acknowledgments

- Flask
- Docker
