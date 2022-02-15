import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
UNSCREEN_API = os.environ.get("UNSCREEN_API", "")

Bot = Client(
    "Remove Background Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=os.environ.get("API_ID"),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """ʜᴇʟʟᴏ...🙄 {},
ɪ ᴀᴍ ᴀ ᴍᴇᴅɪᴀ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ʙᴏᴛ. sᴇɴᴅ ᴍᴇ ᴀ ᴘʜᴏᴛᴏ ɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴡɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ💖: @santhu_music_bot"""
HELP_TEXT = """**ᴍᴏʀᴇ ʜᴇʟᴘ**

- ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀ ᴘʜᴏᴛᴏ
- ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ɪᴛ
- ɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴡɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ

ᴘᴏᴡᴇʀᴇᴅ ʙʏ💖: @santhu_music_bot"""
ABOUT_TEXT = """**About Me**

- **Bot :** `Backround Remover Bot`
- **Creator :** [sᴀɴᴛʜᴜ](https://t.me/santhu_music_bot)
- **Channel :** [sᴀɴᴛʜᴜ ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ](https://telegram.me/santhuvc)
- **Language :** [Python3](https://telugu.org)
- **Library :** [Pyrogram](https://english.org)"""
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('💘ɴᴇᴛᴡᴏʀᴋ💘', url='https://telegram.me/santhubotupadates'),
            InlineKeyboardButton('💛ʟᴇᴀᴠᴇ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ❤', url='https://telegram.me/santhu_music_bot')
        ],
        [
            InlineKeyboardButton('🔰help🔰', callback_data='help'),
            InlineKeyboardButton('💙ᴀʙᴏᴜᴛ💙', callback_data='about'),
            InlineKeyboardButton('😇ᴄʟᴏsᴇ🧐', callback_data='close')
        ]
    ]
)
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('◁', callback_data='home'),
            InlineKeyboardButton('🙄ᴀʙᴏᴜᴛ🙄', callback_data='about'),
            InlineKeyboardButton('😊ᴄʟᴏsᴇ🧐', callback_data='close')
        ]
    ]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('◁', callback_data='home'),
            InlineKeyboardButton('🔰ʜᴇʟᴘ🔰', callback_data='help'),
            InlineKeyboardButton('😇ᴄʟᴏsᴇ🧐', callback_data='close')
        ]
    ]
)
ERROR_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🔰ʜᴇʟᴘ🔰', callback_data='help'),
            InlineKeyboardButton('😇ᴄʟᴏsᴇ🧐', callback_data='close')
        ]
    ]
)
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ', url='https://telegram.me/santhubotupadates')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update, cb=False):
    text=START_TEXT.format(update.from_user.mention)
    if cb:
        await update.message.edit_text(
            text=text,
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & (filters.photo | filters.video | filters.document))
async def remove_background(bot, update):
    if not REMOVEBG_API:
        await update.reply_text(
            text="Error :- Remove BG Api is error",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action("typing")
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    try:
        new_file_name = f"./{str(update.from_user.id)}"
        if update.photo or (
            update.document and "image" in update.document.mime_type
        ):
            new_file_name += ".png"
            file = await update.download()
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_image(file)
        elif update.video or (
            update.document and "video" in update.document.mime_type
        ):
            new_file_name += ".webm"
            file = await update.download()
            await message.edit_text(
                text="Video downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_video(file)
        else:
            await message.edit_text(
                text="Media not supported",
                disable_web_page_preview=True,
                reply_markup=ERROR_BUTTONS
            )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True
        )
    try:
        with open(new_file_name, "wb") as file:
            file.write(new_document.content)
        await update.reply_chat_action("upload_document")
    except Exception as error:
        await message.edit_text(
           text=error,
           reply_markup=ERROR_BUTTONS
        )
        return
    try:
        await update.reply_document(
            document=new_file_name,
            quote=True
        )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=f"Error:- `{error}`",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )


Bot.run()
