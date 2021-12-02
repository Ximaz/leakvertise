# Leakvertise
Leakvertise is a Python open-source project which aims to bypass these fucking annoying captchas and ads from linkvertise, easily. You can see in details how it works walking through the code. However, you might have see web browser extensions or tampermonkey scripts to do this automatically. This projects is more mass-using turned. You can automate the downlaod process so faster. You can see an example in ``tests.py``.

# Config
You don't have to config anything. But you must be aware of something. A cache will be stored in ``leakvertise/``'s folder because once a link is bypass, there is no need to make a new request to linkverise. It's just stored as sqlite format in a file. You can find, using a DB software, all the link that have been bypassed, and there destination. You can delete this file if it takes too much space, but it will be created straight after the newest bypass.

# Thanks
Please, don't forget to ⭐️. If you have any question or trouble, please open an issue. If you think you can make a cleaner code or else, feel free to open a pull request.
