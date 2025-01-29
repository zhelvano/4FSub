import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, START_PIC, ABOUT_TXT, HELP_TXT, FORCE_PIC
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user
async def delete_after_delay(message: Message, delay):
    await asyncio.sleep(3600)
    await message.delete()

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...⚡")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                if msg and (msg.text or msg.photo or msg.document or msg.video or msg.audio or msg.sticker or msg.voice or msg.animation or msg.video_note or msg.contact or msg.location or msg.venue or msg.poll):
                    k = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
                    await asyncio.sleep(0.01)
                    if k is not None:
                        asyncio.create_task(delete_after_delay(k, 1800))
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        await message.reply_text(f"<b>‼️ Forward the Files to Saved Messages or somewhere else before Downloading it.\n\nIt will get Delete after 5 Minutes‼️</b>")
        await message.reply_text(f"<b>Join @AIO_Backup for More ⚡</b>")
        return
    else:
        reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("∆ Backup Channel ∆", url='https://t.me/AIO_Backup')],
                    [InlineKeyboardButton("∆ About Me ∆", callback_data='about'),
                     InlineKeyboardButton("∆ Developer ∆", url='https://t.me/straw_hat_yonko')],
                    [InlineKeyboardButton("∆ Share Us ∆", url='https://telegram.me/share/url?text=%2A%2ABest%20Adult%20Network%20in%20Telegram%2A%2A%0A%0Ahttps://t.me/AIO_Backup%0A%0A%2A%2AJoin%20Now%2A%2A')],
                ])
        await message.reply_photo(
            photo= START_PIC,
            caption= START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            
        )
        return
    

#=====================================================================================##

WAIT_MSG = "<b>Working....</b>"

REPLY_ERROR = "<code>Use this command as a reply to any telegram message without any spaces.</code>"

#=====================================================================================##

    
    
@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="• ⚡ᴄʜᴀɴɴᴇʟ 1⚡", url=client.invitelink2),
            InlineKeyboardButton(text="⚡ᴄʜᴀɴɴᴇʟ 2⚡ •", url=client.invitelink3),
        ],
        [
            InlineKeyboardButton(text="• ⚡ᴄʜᴀɴɴᴇʟ 3⚡", url=client.invitelink4),
            InlineKeyboardButton(text="⚡ᴄʜᴀɴɴᴇʟ 4⚡ •", url=client.invitelink),
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = '• ⚡ ɴᴏᴡ ᴄʟɪᴄᴋ ʜᴇʀᴇ ⚡ •',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply_photo(
    photo=FORCE_PIC, 
    caption=FORCE_MSG.format(
        first=message.from_user.first_name,
        last=message.from_user.last_name,
        username=None if not message.from_user.username else '@' + message.from_user.username,
        mention=message.from_user.mention,
        id=message.from_user.id
    ),
    reply_markup=InlineKeyboardMarkup(buttons)
)

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴘʀᴏᴄᴇꜱꜱɪɴɢ....</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>🚀 Broadcast Completed</u></b>

<b>😍 Total Users :</b> <code>{total}</code>
<b>😁 Successful :</b> <code>{successful}</code>
<b>😒 Blocked Users :</b> <code>{blocked}</code>
<b>😢 Deleted Accounts :</b> <code>{deleted}</code>
<b>😔 Unsuccessful :</b> <code>{unsuccessful}</code>"""
        
        return await pls_wait.edit(status)

    else:
        aqua = 21
