from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", "7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM")
API_ID = int(environ.get("API_ID", "24089031"))
API_HASH = environ.get("API_HASH", "0615e3afe13ddaaf8e9ddbd3977d35ff")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "5702598840 6584789596").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", "-1002100475470"))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", ""-1002100475470))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", "-1002100475470"))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", "300"))
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://Mongo1:586637515hshhwfftqu@cluster0.tvy79ai.mongodb.net/?retryWrites=true&w=majority")
ARQ_API_URL = environ.get("ARQ_API_URL", "https://thearq.tech")
ARQ_API_KEY = environ.get("ARQ_API_KEY", "HMXVLQ-NGJEQW-LGKBOW-XRUNUG-ARQ")
RSS_DELAY = int(environ.get("RSS_DELAY", "300"))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/Al3x-GitHub/KomiBot.git"
)
