class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29882470
    API_HASH = "be2335c254b85387696867938821620d"

    CASH_API_KEY = "6MR9E57AAMWQ38ZN"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zyafrqwu:DQwT2n-JTx-yhkkNmWscr9sG4aIOGcFf@kesavan.db.elephantsql.com/zyafrqwu"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002127712120)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://xemajes377:ciyelupa22"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6932885176:AAF2JPFe92EsH3JJxFONzO0ADt4m_94zjms"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "SODT1YDCHWJZ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6501438384  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
