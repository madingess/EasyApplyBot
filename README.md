# LinkedIn Easy Apply Bot

Automate your LinkedIn job applications using Easy Apply feature with ease using this Python and Selenium-based bot.
Tested successfully on over 20,000+ job applications!

## Disclaimer

**Use this bot at your own risk.** This bot comes with no warranties or guarantees. I am not liable for any
consequences, including potential account restrictions or suspensions by LinkedIn. Consider it an educational and
exploratory project!

## Credits & Enhancements

This repository is a fork from the original developer [Nathan Duma](https://github.com/NathanDuma), with significant
code updates contributed by [Micheal Dingess](https://github.com/madingess/). Since their last commits, I've diligently
maintained and improved this fork, addressing bugs, introducing new features, and enhancing the user experience.
Notably, I've added the option to log application submission dates and times for performance tracking.

## 🎥 How-to Video

For your convenience, I've created a comprehensive video tutorial to guide you through the setup and usage of the bot.
Check it out on [YouTube](https://youtu.be/IXflenwJzhQ).

## 🛠️ Setup & Launch

If you are new to Python, please watch this [video first](https://youtu.be/IXflenwJzhQ).

1. Start by configuring the `config.yaml` file. This is a one-time setup and contains the necessary inputs for running
   the bot. Necessary help is documented within the `config.yaml`.
2. Please maintain the formatting and avoid adding unnecessary spaces in the file.
3. After configuring the file, install the dependencies listed in `requirements.txt`.

   Now, you're ready to launch the bot using your preferred method:

    - If you're using an IDE like PyCharm Community Edition, execute `main.py` from your IDE.
    - If you prefer the command line or terminal, activate the virtual environment with `source venv/bin/activate`, then
      run `python3 main.py`.

In case you encounter any "dependencies not found" errors, ensure that the required dependencies are installed. You can
verify this using your IDE or, if you're using the command line/terminal, run `pip install -r requirements.txt` before
executing `python3 main.py` to initiate the bot.

### 🐞🔧 Known Issues & Resolutions

1. ~~Sometimes, the bot may get stuck in an endless loop of opening external links. This occurs when two specific
   conditions are met: First, the bot encounters a page with text like "no matching jobs found for(...)," and second,
   LinkedIn suggests "Jobs you may be interested in..." along with links to external websites. To resolve this, either
   click on the next Easy Apply job from the suggestions or modify the search keywords while the bot is active. If all
   else fails, restarting the bot is an option.~~

2. ~~Random "stale element" errors have been fixed.~~

3. ~~Resolved issue with remote filter change in URL.~~

4. In some cases, integrated development environments (IDEs) such as PyCharm might conflict with the included virtual
   environment (venv) in this project. To address this, you can delete the `venv` folder and configure the Python
   interpreter to use the "local" option. Furthermore, installing the dependencies from `requirements.txt` ensures a
   successful run of `main.py`.

5. The bot occasionally struggles with providing accurate or complete responses to questions in non-English job posts,
   leading to potential infinite loops. The solution is to close such a job, allowing the bot to progress to the next
   item in the queue.

## 🆘❓Need Further Assistance?

If you're new to Python, I recommend watching the [YouTube](https://youtu.be/IXflenwJzhQ) video for a comprehensive
overview. If you encounter any genuine issues with the code or the bot's functionality, please raise them in the "
Issues" section of this repository. However, please refrain from using issues for personal technical support.

For general inquiries and support, feel free to post a comment describing your problem under
the [YouTube](https://youtu.be/IXflenwJzhQ) video.

## Support This Project

If you find this project valuable, consider showing your support by buying me a coffee through
[PayPal](https://paypal.me/voidbydefault). Your support is greatly appreciated!