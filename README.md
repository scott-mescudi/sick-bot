# SickBot - Automatic Absence Notification System

SickBot is a Python program that automates the process of sending absence notifications to a predefined recipient via email at a specified time. It can be utilized for various purposes such as notifying teachers or employers about unexpected absences.

## Installation and Setup

1. **Python Installation**: Ensure you have Python installed on your system. This program is compatible with Python 3.x.

2. **Dependencies Installation**: Install the required dependencies using pip. You can install them via the following command:
    ```bash
    pip install pygame colorama
    ```

3. **Configuration Setup**: Edit the `config.json` file to configure your SMTP server details and email credentials. The configuration file includes the following parameters:
   - `smtp_server`: SMTP server address.
   - `smtp_port`: Port number of the SMTP server.
   - `smtp_username`: Username for SMTP authentication.
   - `smtp_password`: Password for SMTP authentication.
   - `from_email`: Sender's email address.
   - `to_email`: Recipient's email address.
   - `audio_file_path`: Path to the audio file to be played as an alarm.

## Usage

1. **Run the Program**: Execute the program by running the Python script `sickbot.py`.

2. **Set Alarm Time**: Enter the desired hour and minute when you want the alarm/notification to trigger. The program will wait until the specified time to execute further actions.

3. **Notification Process**: At the specified time, the program will play an alarm sound and prompt you to take action:
   - You have a set duration (randomly generated between 2 to 120 minutes) to close the program to cancel the email notification.
   - If no action is taken within the specified duration, an email will be automatically sent to the recipient with a predefined absence notification message.

4. **Cancel Notification**: To cancel the email notification, simply close the program using `Ctrl + C` before the countdown timer ends.

## Important Notes

- Ensure that your SMTP server allows access from less secure apps or provides an application-specific password if required.
- Customize the absence notification message (`letter` variable in the script) according to your requirements.
- Test the program with caution, especially when dealing with real email addresses and SMTP credentials.

#### Video Tutorial: Setting Up SMTP Server with Gmail

Here's a video tutorial that demonstrates how to set up an SMTP server using Gmail:

[![Setting Up SMTP Server with Gmail](https://img.youtube.com/vi/kTcmbZqNiGw/0.jpg)](https://www.youtube.com/watch?v=kTcmbZqNiGw&t=235s)

You can follow along with this video to configure your SMTP server with Gmail. Once set up, make sure to update the `smtp_server`, `smtp_port`, `smtp_username`, and `smtp_password` variables in the `sickbot.py` script accordingly.

### Additional Resources

- [Gmail SMTP settings and configuration](https://support.google.com/mail/answer/7126229)
- [Setting up SMTP server with other email providers](https://www.google.com/search?q=setting+up+smtp+server)

By following these instructions and the video tutorial, you'll be able to set up an SMTP server effectively for use with the `sickbot.py` script. If you encounter any difficulties, feel free to consult the documentation of your email provider or seek further assistance online.

