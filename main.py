__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *
import os

bot = MsBot(port=int(os.environ['PORT']))
bot.add_process(bit_response)
bot.run()
