from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "22032175"))
API_HASH = getenv("API_HASH", "54c21046170f78a2e099d10b8e791df6")
BOT_TOKEN = getenv("BOT_TOKEN", “5624242543:AAGdys0RkGgSmCNWIS3XOPu_91RL09Liia4")
BOT_NAME = getenv("BOT_NAME","I love you")
BOT_USERNAME = getenv("BOT_USERNAME", "Iloveyou_999bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "B.g.m short status")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Anime_flix14")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "Ak_Back_up_channel")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cb2763a4fd9af49b26cb0.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1864894033").split()))
