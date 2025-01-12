# Spor Istanbul Appointment Notifier

This project is a Python-based Selenium automation script designed to check session availability on Spor Istanbul's website and notify users via SMS when an available session is found. The script can run on various platforms including Linux, Windows, and macOS, and can be executed manually or scheduled to run automatically.

## Features

- Automated login to Spor Istanbul website.
- Dynamic session availability checking.
- SMS notification for available sessions via Twilio.
- Handles website bugs with retry mechanisms.
- Supports multiple users.

## Prerequisites

- Python 3.8 or higher
- Firefox browser and Geckodriver
- A Twilio account for SMS notifications

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/efeaslansoyler/spor-istanbul-appointment-notifier.git
   cd spor-istanbul-appointment-notifier
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv  # For Windows use: python -m venv venv
   source venv/bin/activate  # For Windows use: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure users:

   - Copy `users_template.json` to `users.json`.
   - Edit `users.json` to add your username, password, and phone number for SMS notifications.

## Example `users.json`

```json
[
  {
    "username": "your_username",
    "password": "your_password",
    "phone_number": "+1234567890"
  }
]
```

**Important:** You must rename `users_template.json` to `users.json` and fill in the required information for the script to work.

## Running the Script

### Manually

Activate your virtual environment and execute:

```bash
python main.py
```

### Automatically

#### On Linux (Cron Job)

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script every 12 hours:
   ```bash
   0 */12 * * * /path/to/venv/bin/python /path/to/your_project/main.py >> /path/to/your_project/logs/cron.log 2>&1
   ```

3. Save and exit.

#### On Windows (Task Scheduler)

1. Open Task Scheduler and create a new task.
2. Set the action to run `python.exe` with arguments pointing to `main.py`.
3. Schedule the task to run every 12 hours.

#### On macOS (Launchd)

1. Create a `.plist` file in `~/Library/LaunchAgents/`.
2. Add scheduling instructions to execute the script every 12 hours.
3. Load the plist file using:
   ```bash
   launchctl load ~/Library/LaunchAgents/your_script.plist
   ```

## Alternative Hosting Options

- **Local Execution**: Run the script manually on your personal computer.
- **Cloud Services**: Deploy to cloud platforms like AWS, Google Cloud, or Heroku.
- **Raspberry Pi**: Set up the script on a Raspberry Pi for continuous local execution.

## Notes

- Ensure the `geckodriver` is in your system's `PATH`.
- Monitor logs for script output and errors.
