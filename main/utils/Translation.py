# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 你好, {}**\n
<i>Telegram 文件直链机器人</i>\n
<i>Click On Help To Get More Information</i>"""

        HELP_TEXT = """ 使用方法
<i>发送文件以获得直链.</i>
"""

        ABOUT_TEXT = """OK"""

        stream_msg_text ="""
<u>**Successfully Generated Your Link !**</u>\n
<b>📂 文件名: </b> {}\n
<b>📦 文件大小: </b> {}\n
<b>📥 下载链接: </b> {}\n
<b>🖥 播放链接: </b> {}"""

        ban_text="__你已遭到封禁.__"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],        
        [InlineKeyboardButton("Updates Channel", url='https://google.com'),
        InlineKeyboardButton("Repo", url='https://google.com')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
