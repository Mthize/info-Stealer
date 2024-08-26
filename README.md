# # System Information Collector & HTTP Server

This repository contains two Python scripts designed to work together for collecting and storing system information over HTTP.

## Overview
1. **Client Script** (`client.py`):
   - Gathers system information using the `systeminfo` command (for Windows environments).
   - Sends the collected information as a JSON payload to a specified HTTP server.
   - Implements a retry mechanism with a delay, ensuring resilience in case of network or server issues.
   - Configured to send data to `http://localhost:3000` by default.

2. **Server Script** (`server.py`):
   - A simple Flask-based HTTP server listening on port 3000.
   - Receives the JSON payload from the client, extracts the system information, and writes it to a file named `target_information.txt`.
   - Sends an "OK" response upon successful data handling.

## Features
- **Automatic Data Collection**: The client script automatically gathers and sends system information without requiring user input.
- **Resilient Communication**: The client retries sending data until it successfully connects to the server.
- **Simple Data Handling**: The server saves the received system information in a plain text file for easy access and further analysis.
- **Modular Design**: The client and server scripts can be easily customized to work in different environments or use different data sources and destinations.

## Use Cases
- **System Monitoring**: Collect basic system information from remote machines.
- **Penetration Testing**: Simulate data exfiltration during security assessments.
- **Learning & Experimentation**: A simple example of using Flask and `requests` for HTTP communication in Python.

## Requirements
- Python 3.x
- Flask: `pip install flask`
- Requests: `pip install requests`

## Usage

### Running the Server
1. Install the required dependencies:
   ```
    pip install flask




-Run the server script:
`python server.py`
-The server will start listening on http://localhost:3000.

-Running the Client
  
`Install the required dependencies:`


 `pip install requests`
 `Run the client script:`
 
 `python client.py`
- The client will collect system information and attempt to send it to the server.

- Notes
- Retry Mechanism: If the client script fails to connect to the server, it will retry every 3 seconds until successful.
- Storage: The system information is saved in target_information.txt in the same directory as the server script.
