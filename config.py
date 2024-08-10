import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7391520101:AAF0pA1SByHcJV2tDEMSQtA4RMJOkDyOBS")
      API_ID = int(os.environ.get("APP_ID", "23416992"))
      API_HASH = os.environ.get("API_HASH", "bebe7b8b7bc74aeaa08f658e8aa799fe")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "TG_SUPP0RT")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", "7030346964" )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://botss:botss@cluster0.txf7e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
