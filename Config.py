import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7616035506:AAEEbOmbWJ99THkK8lJ1JT6ejCmt33J6KzA")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Kayto_Official")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://oaykvtmj:bsIGPV7wmId1x1CNH9eqxQVX5t25cHI3@manny.db.elephantsql.com/oaykvtmj")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 28928028)
  API_HASH = os.environ.get("API_HASH", "b097202e877124392f4851d215fa8f3a")
  # Sudo users( goto @missrose_Bot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "7678359785").split()))
  SUDO_USERS.append(7678359785)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.__",
      ]
      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
