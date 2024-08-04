# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27043578"))
API_HASH = getenv("API_HASH", "be06bb8e73532042d947bac9d6ee34c0")
BOT_TOKEN = getenv("BOT_TOKEN", "7292978806:AAG07VgutugTU2UAeAyWJx-Vd7UXSDQ_zDg ")
OWNER_ID = int(getenv("OWNER_ID", "1307312609"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://krishnasoni63888:P94txJtapNrxFNRz@cluster0.enblfk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "t.me/bhusoni"))
FORCESUB = getenv("FORCESUB", "bhusoni")
