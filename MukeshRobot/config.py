class Config(object):
    LOGGER = True
    API_ID = "27201175" 
    API_HASH = "f9fcd5bc0af204efdb06219b5c668fc1"
    TOKEN = "6392016724:AAGVd5l1161SSymqZQLTckUfMOpEGLh67Y8"  
    OWNER_ID= "6079943111"
    
    SUPPORT_CHAT = "AloneXBots" 
    START_IMG = "https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg"
    EVENT_LOGS = "-1001603822916"
    MONGO_DB_URI= "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority"
   
    DATABASE_URL = "postgres://qgwplioy:2qae3-yMNBvZUBFujjozU-dU7l1H8NsM@trumpet.db.elephantsql.com/qgwplioy"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "LQ58UKEV7CH8YCW5"
    )
    TIME_API_KEY = "LXDWL7BZN03W"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./!"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
