class Config(object):
    LOGGER = True

    # Get this value from my.telegram.osrg/apps
    API_ID = 27138045
    API_HASH = "d4274d9aa7ef93dad8a26b830153c0ba"

    CASH_API_KEY = "1NMJ984LL5RIX7EV"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zgsfhwbp:5N06vnsqCbsXj94zHMrv_RaSqYCh7Gyl@bubble.db.elephantsql.com/zgsfhwbp"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002127712120)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://autofilter:autofilter@cluster0.gzork9r.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/929db6105613abc7e2d46.jpg"

    SUPPORT_CHAT = "nongsdisni"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6685879044:AAFbTpu3h5hO_nyyjbDSHu8FN2k7siv060Q"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "SXB4XEFZEXRV"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6392715492  # User id of your telegram account (Must be integer)

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
