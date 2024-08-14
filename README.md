
# Telegram Bot for NGO "Investors of Residential Complex Holosiivska Dolyna"

This is a Telegram bot designed to provide information and assistance to the members of the NGO "Investors of Residential Complex Holosiivska Dolyna". The bot can provide general information, share important documents, guide new members on how to join the organization, and offer contact support through Telegram.

## Features

- **Information about the NGO:** Provides general information about the organization, its purpose, and its leadership.
- **Documents:** Shares links to important documents such as the charter and membership regulations.
- **How to Join:** Guides new members on how to join the NGO, including submitting necessary documents.
- **Support:** Offers contact support via Telegram.

## Installation and Setup

Follow these steps to set up the bot locally and deploy it:

### Prerequisites

- Python 3.9 or later
- Docker (optional, for containerized deployment)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/holosiivska-dolyna-bot.git
cd holosiivska-dolyna-bot
```

### 2. Set Up the Virtual Environment

```bash
make install
```

This will create a virtual environment and install all necessary dependencies.

### 3. Create a `.env` File

Create a `.env` file in the root directory of the project and add your Telegram bot token:

```
TELEGRAM_TOKEN=your_telegram_bot_token_here
```

### 4. Run the Bot

To start the bot, run:

```bash
make run
```

### 5. Running Tests

To run the tests using `pytest`, use:

```bash
make test
```

### 6. Build and Run with Docker (Optional)

If you want to containerize the bot, you can build and run the Docker image:

```bash
make docker-build
make docker-run
```

### 7. Install bot to Systemd

Run the Script with the TELEGRAM_TOKEN as an Argument:

```bash
make setup-service TELEGRAM_TOKEN=your_telegram_token
```

## Project Structure

- `lambda_function.py`: The entry point of the bot when running on AWS Lambda.
- `requirements.txt`: The list of Python dependencies.
- `.env`: Environment variables file (not included in the repo).
- `Dockerfile`: Docker configuration for containerizing the bot.
- `.dockerignore`: Specifies files and directories that should be ignored by Docker.
- `Makefile`: Automates setup, testing, and Docker tasks.
- `test_bot.py`: Contains unit tests for the bot.
- `setup_telegram_bot_service.sh`: Setup telegram bot as service

## License

This project is licensed under the MIT License.
