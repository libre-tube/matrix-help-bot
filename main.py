import simplematrixbotlib as botlib
import os 
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("matrix_username")
password = os.getenv("matrix_password")

data = {"hls": """Hey, I am the LibreTube Helpbot. 
If videos don't play for you, check your app for updates (settings -> scroll to bottom -> press"Check for new updates")
If this didn't help, make sure that HLS is enabled ("!enablehls" for more instructions!)
If it's still not working, send another message so we know, that your problems still exist""",
     
     "dash": """Hey, I am the LibeTube Helpbot. 
If your videos aren't rendering, check your app for updates (settings -> scroll to bottom -> press "Check for new updates")
If this didn't help, make sure that HLS is enabled("!enablehls" for more instructions) 
If it's still not working, send another message so we know, that your problems still exist.""",
     
     "enablehls": """Press the "settings"-button -> "audio and video" -> enable "Use HLS".""",
     
     "github": "You can find the GitHub Repository at ![https://github.com/libre-tube/LibreTube](https://github.com/libre-tube/LibreTube)",
     
     "offtopic": "Offtopic! Please continue writing in #pfo:matrix.org",
     
     "issue": "Issues are tracked on Github (!github)",
     
     "help": """Hello I am your Opensource Bot for the LibreTube chatroom. I'll explain my functions:
     "!hls" and "!dash" Instruction
     "!enablehls" Instruction for enabeling HLS.
     "!github" shows you the official Github Repository.
     "!offtopic" can be used for Offtopic talks.
     "!issue" can be used if someone posts an issue in the LibreTube chat."""}
     
     
config = botlib.Config()
# config.encryption_enabled = True  # Automatically enabled by installing encryption support
config.emoji_verify = True
config.ignore_unverified_devices = True

creds = botlib.Creds("https://matrix.org", username, password)
bot = botlib.Bot(creds, config)
PREFIX = '!'


@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    
    if not match.is_not_from_this_bot():
        return 
    if not match.prefix():
        return
    message = data.get(match.command())
    if message: 
        await bot.api.send_markdown_message(room.room_id, message)
bot.run()
