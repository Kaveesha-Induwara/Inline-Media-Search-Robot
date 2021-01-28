import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi, I'm Media Search bot.

හායි 😌 මම ඉන්ලයින් ක්‍රමයට මීඩියා සර්ච් කරන බොට් කෙනෙක් ❤ **

Here you can search files in inline mode. Just press following buttons and start searching.

ඔයාලට ඔනේ දෙවල් ලබාගන්න පහත ඉන්ලයින් බටන් එක යුස් කරන්න ❤

එක ටච් කරාම මැසෙජ් ටයිප් කරන තැන එන සර්ච් ඔප්ශන් එක යුස් කරලා ඔයාට ඔනේ දෙ හොයා ගන්න 💪💪.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
