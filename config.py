#(©)CodeXBotz
#Recoded By @i_killed_my_clan



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7326140432:AAEZ2v_4qS4A89y0xQy09csQg_zqoIC4JDg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20718334"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002177334941"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5585016974"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://gohan:gohanxbot@cluster0.xoc5s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002072642438"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001930406310"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002033058072"))
FORCESUB_CHANNEL4 = int(os.environ.get("FORCESUB_CHANNEL4", "-1002177334941"))
                                       
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/oCO.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/opu.jpg")

HELP_TXT = "https://t.me/AHSS_HELP_ZONE"
ABOUT_TXT = "<b>» ᴏᴡɴᴇʀ: <a href=https://t.me/TeenGohan002>ɢᴏʜᴀɴ</a>\n» ᴍᴀᴛ ᴀɴɪᴍᴇ : <a href=https://t.me/Mikey_anime_team>ᴍᴀᴛ ᴀɴɪᴍᴇ</a>\n» ʜᴀɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+7Ext4kkaB9ZmZTRl>ʜᴀɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ</a>\n» ʙᴀᴄᴋ ᴜᴘ : <a href=https://t.me/+ufHLR0GHOSNkNjI1>ʙᴀᴄᴋ ᴜᴘ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Cosmic_Awaken>ᴏʙɪᴛᴏ</a></b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://t.me/Mikey_anime_team>ᴍᴀᴛ ᴀɴɪᴍᴇ</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5355745915 6911235730 5924136853 5585016974").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>"

ADMINS.append(7546728320)
ADMINS.append(5585016974)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
