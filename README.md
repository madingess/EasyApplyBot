# LinkedIn Easy Apply Bot
Automatically apply to LinkedIn Easy Apply jobs. This bot answers the application questions as well!

This is for educational purposes only. I am not responsible if your LinkedIn account gets suspended or for anything else.

This bot is written in Python using Selenium.

## Fork Notes

Adopted from Mike's repo at https://github.com/madingess/EasyApplyBot/. 
Added new skills, questions, and logging of application date/time to monitor bot's performance (e.g. using PowerBI).

## How to video?
https://youtu.be/-eZJH5EdQr0

## Setup & Startup

To run the bot, open the command line in the cloned repository directory. Activate the virtual environment and start the bot using these commands:
```bash
source venv/bin/activate
python3 main.py
```
_Note that if you plan to use an IDE like PyCharm, a virtual environment might cause conflicts. If you are new to Python and prefer to use an IDE, a simple solution could be to delete the 'venv' folder once you have downloaded the bot files, and let the IDE handle the 'venv' part accordingly._

Next, you need to fill out the config.yaml file. Most of this is self-explanatory but if you need explanations please see the end of this README.

## Support and help
'config.yaml' is all a user needs to configure. Don't change the formatting or add spaces. Comments provide an explanation of each input required. If you think there is an issue with the code, please raise it in Issues. For general questions, post comments under the video above.
