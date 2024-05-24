import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
LOG_LEVEL = "INFO"
SENTRY_DSN =  os.getenv('sentry_dsn')
LOLS_BOT_ENABLED = bool("True")
EMOJI_TIMEOUT_SECONDS = int("60")
GARBAGE_MESSAGE_TIMEOUT_SECONDS = int("30")
