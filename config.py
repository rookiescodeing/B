import os



class Config((object)):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5008141817:AAF7hrx6DwYAdEVhx2YM4mREcJD7QZE_la4")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 7363654))
    API_HASH = os.environ.get("API_HASH","68e518c106f816dc7eebded6bfaf33a6")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = {int(x) for x in os.environ.get("AUTH_USERS", "").split()}
    # Banned Unwanted Members..
    BANNED_USERS = {int(x) for x in os.environ.get("BANNED_USERS", "").split()}
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "postgres://xgaguiml:zQEGDj7O0o6DgReyTO-wzJS7WPJhn4bR@tiny.db.elephantsql.com/xgaguiml")
    # dict to hold Google Drive SignIns
    G_DRIVE_AUTH_DRQ = {}
    # g_drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", True)
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", True)
    INDEX_URL = os.environ.get("INDEX_URL", "")
