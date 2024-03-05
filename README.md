# SickBot

This program, `sickbot.py`, is a Python script designed to automate the process of sending an email notification to inform about absence due to sickness. The program selects a random excuse from a predefined list and crafts an email accordingly. It also includes a scheduler to send the email at a specified time.

## How to Use

1. **Configure SMTP Settings**: Before using this program, make sure to configure the SMTP settings including the SMTP server, port, username, and password.

2. **Email Recipient**: Update the `to_email` variable to specify the recipient's email address.

3. **Run the Script**: Execute the script either by running it locally or deploying it to a server.

4. **Scheduled Email**: The script is set to send the email at a specific time (defined by `target_hour` and `target_minute` variables). You have 20 minutes to close the program after it prompts you.

## Program Explanation

- The program randomly selects an excuse from a list of predefined excuses.
- It crafts an email template with the selected excuse and sends it to the specified recipient.
- The script uses SMTP (Simple Mail Transfer Protocol) for sending emails.
- It utilizes the `smtplib` library for SMTP functionality.
- The script includes an infinite loop that constantly checks the current time. When the specified time (`target_hour` and `target_minute`) is reached, it prompts the user to close the program within 20 minutes to prevent sending the email.

## Customizing Excuses and Letter

To customize the excuses and the absence letter, follow these steps:

1. **Excuses:**
    - Open the Python script (`email_send.py`) in a text editor.
    - Locate the `random_excuse` variable assignment.
    - Modify the list of excuses according to your preference.
    - Save the changes.

2. **Letter:**
    - Open the Python script (`email_send.py`) in a text editor.
    - Locate the `letter` variable assignment.
    - Modify the content of the absence letter as needed.
    - Save the changes.

Remember to keep the structure of the code intact while making modifications. Ensure that the email content is appropriate and professional.

## Important Note

- **Security**: Be cautious with the usage of this script, especially regarding sensitive information such as SMTP credentials.
- **Customization**: Feel free to customize the email template, excuses, and scheduling parameters to fit your specific requirements.
- **Error Handling**: Ensure proper error handling mechanisms are in place, especially for SMTP operations to handle network errors or authentication failures.
### Setting Up SMTP Server

To use the `sickbot.py` script effectively, you'll need to set up an SMTP server. Below is a step-by-step guide on how to set up an SMTP server using Gmail as an example.

#### Video Tutorial: Setting Up SMTP Server with Gmail

Here's a video tutorial that demonstrates how to set up an SMTP server using Gmail:

[![Setting Up SMTP Server with Gmail](https://img.youtube.com/vi/kTcmbZqNiGw/0.jpg)](https://www.youtube.com/watch?v=kTcmbZqNiGw&t=235s)


You can follow along with this video to configure your SMTP server with Gmail. Once set up, make sure to update the `smtp_server`, `smtp_port`, `smtp_username`, and `smtp_password` variables in the `sickbot.py` script accordingly.

### Additional Resources

- [Gmail SMTP settings and configuration](https://support.google.com/mail/answer/7126229)
- [Setting up SMTP server with other email providers](https://www.google.com/search?q=setting+up+smtp+server)

By following these instructions and the video tutorial, you'll be able to set up an SMTP server effectively for use with the `sickbot.py` script. If you encounter any difficulties, feel free to consult the documentation of your email provider or seek further assistance online.

