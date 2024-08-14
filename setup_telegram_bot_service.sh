#!/bin/bash

# Check if TELEGRAM_TOKEN is provided
if [ -z "$1" ]; then
  echo "Usage: $0 TELEGRAM_TOKEN"
  exit 1
fi

TELEGRAM_TOKEN=$1  # The Telegram bot token provided as an argument

# Variables (change these to match your setup)
SERVICE_NAME="telegram-bot"
SERVICE_DESCRIPTION="Telegram Bot for NGO 'Investors of Residential Complex Holosiivska Dolyna'"
USER_NAME=$(whoami)  # The current user
WORKING_DIR="$(pwd)/bot"  # The directory where app.py is located
PYTHON_PATH="$(which python3)"  # Path to the Python interpreter
APP_PATH="$WORKING_DIR/app.py"  # Full path to app.py

# Create the systemd service file
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

echo "Creating systemd service file at $SERVICE_FILE..."

sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=$SERVICE_DESCRIPTION
After=network.target

[Service]
User=$USER_NAME
WorkingDirectory=$WORKING_DIR
ExecStart=$PYTHON_PATH $APP_PATH
Restart=always
Environment="TELEGRAM_TOKEN=$TELEGRAM_TOKEN"

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd to recognize the new service
echo "Reloading systemd..."
sudo systemctl daemon-reload

# Enable the service to start on boot
echo "Enabling the $SERVICE_NAME service to start on boot..."
sudo systemctl enable $SERVICE_NAME

# Start the service
echo "Starting the $SERVICE_NAME service..."
sudo systemctl start $SERVICE_NAME

# Check the status of the service
echo "Checking the status of the $SERVICE_NAME service..."
sudo systemctl status $SERVICE_NAME