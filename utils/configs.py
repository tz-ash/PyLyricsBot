import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # ID of users that can't use the bot commands
    BANNED_USERS = set(
        int(x) for x in os.environ.get(
            "BANNED_USERS", "").split())

    # To record start time of bot
    BOT_START_TIME = time.time()

    # Genius Api From Here : https://genius.com/api-clients
    API = os.environ.get("GENIUS_API", None)

    # buttons
    PAGENUM = int(os.environ.get("PAGENUM", 20))


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @miztyrobot !

MizLyrics Is A Bot That Can Help You Get Song Lyrics
"""

    ABOUT_TEXT = """🤖 **My Name:** [Miz Lyrics](t.me/miztyrobot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Heroku](heroku.com)

👨‍💻 **Developer:** [This Kid](t.me/kidhub)

💡 **Mush World:** [Magical](https://t.me/magiclmush)

👥 **Support Group:** [Kid Support](https://t.me/tzkid)

📢 **Updates Channel:** [Kid Updates](https://t.me/kidbots)


❤ [Kid](https://t.me/kidhub) (Hub)
"""

    HELP_TEXT = """💡 Just Send Me The Name Of The Song.  That's it

❤ [Kid](https://t.me/kidhub) (Hub)
"""

    ERR_TEXT = "⚠️ Genius API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons.",

    NORES = "💬 No Results"

    SEARCHING = "🔍 Searching For :"

    WAIT = "💬 Please Wait !!"

    ARTIST = "🗣 Artist :"

    SONG = "🎵 Song :"
