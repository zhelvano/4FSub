from datetime import datetime, timedelta
from pyrogram import filters
from pyrogram.types import Message
from bot import Bot
from config import OWNER_ID
from database.database import present_admin, add_admin, full_adminbase, del_admin

def convert_time(duration_seconds: int) -> str:
    periods = [
        ('year', 60 * 60 * 24 * 365),
        ('month', 60 * 60 * 24 * 30),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1)
    ]

    parts = []
    for period_name, period_seconds in periods:
        if duration_seconds >= period_seconds:
            num_periods = duration_seconds // period_seconds
            duration_seconds %= period_seconds
            parts.append(f"{num_periods} {period_name}{'s' if num_periods > 1 else ''}")

    if len(parts) == 0:
        return "0 seconds"
    elif len(parts) == 1:
        return parts[0]
    else:
        return ', '.join(parts[:-1]) + ' and ' + parts[-1]


@Bot.on_message(filters.command("add_admin"))
async def add_admin_command(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("madherchod tere baap ne tujhe owner banaya mera!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>You're using the wrong format. Please use it like this:</b> /add_admin {user_id}")
        return

    try:
        admin_id_add = int(message.command[1])
        user_info = await client.get_users(admin_id_add)  # Fetch user details
    except ValueError:
        await message.reply_text("Invalid user ID. Please check again!")
        return

    # Extract first and last name
    first_name = user_info.first_name
    last_name = user_info.last_name if user_info.last_name else ""  # Last name could be None
    full_name = f"{first_name} {last_name}".strip()

    # Add the user to the admin list in the database
    added = await add_admin(admin_id_add)
    if added:
        await message.reply_text(f"<b>{first_name} - {admin_id_add} is already an admin.</b>")
    else:
        await message.reply_text(f"<b>{first_name} - {admin_id_add} is now an admin.</b>")


@Bot.on_message(filters.command('del_admin'))
async def remove_admin_command(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("madherchod tere baap ne tujhe owner banaya mera!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>You're using the wrong format. Please use it like this:</b> /del_admin {user_id}")
        return

    try:
        admin_id_remove = int(message.command[1])
        user_info = await client.get_users(admin_id_remove)  # Fetch user details
    except ValueError:
        await message.reply_text("Invalid user ID. Please check again...!")
        return

    # Extract first and last name
    first_name = user_info.first_name
    last_name = user_info.last_name if user_info.last_name else ""  # Last name could be None
    full_name = f"{first_name} {last_name}".strip()

    # Remove the user from the admin list in the database
    removed = await del_admin(admin_id_remove)
    if removed:
        await message.reply_text(f"<b>{first_name} - {admin_id_remove} was neither an admin nor found in the admin list.</b>")
    else:
        await message.reply_text(f"<b>{first_name} - {admin_id_remove} has been removed from the admin list.</b>")


@Bot.on_message(filters.command('admins'))
async def admin_list_command(client: Bot, message: Message):
    user_id = message.from_user.id
    is_user_admin = await present_admin(user_id)
    if user_id != OWNER_ID:
        await message.reply_text("madherchod tere baap ne tujhe owner banaya mera!")
        return

    our_admin_ids = await full_adminbase()  
    formatted_admins = []

    for admin_id in our_admin_ids:
        user = await client.get_users(admin_id)
        if user:
            full_name = user.first_name + (" " + user.last_name if user.last_name else "")
            admin_info = f"{full_name} - {admin_id}"
            formatted_admins.append(admin_info)

    if formatted_admins:
        admins_text = "\n".join(formatted_admins)
        text = f"<b>radhwo ki list:</b>\n\n{admins_text}"
    else:
        text = "<b>Admin list is empty</b>"

    await message.reply_text(text, disable_web_page_preview=True)
