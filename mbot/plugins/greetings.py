"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from mbot import LOG_GROUP, OWNER_ID, SUDO_USERS, Mbot,AUTH_CHATS
from os import execvp,sys

@Mbot.on_message(filters.command("start"))
async def start(client,message):
    reply_markup = [[
        InlineKeyboardButton(
            text="🥀𝐂𝐡𝐚𝐧𝐧𝐞𝐥🍁", url="https://t.me/Ur_rishu_143"),       InlineKeyboardButton(text="🌹𝐇𝐞𝐥𝐩🪅",callback_data="helphome")
        ],
        [
            InlineKeyboardButton(text="➕𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐆𝐫𝐨𝐮𝐩➕",
            url="https://t.me/"+bot.name+"?startgroup=true"),
        ]]
    if LOG_GROUP:

        invite_link = await client.create_chat_invite_link(chat_id=(int(LOG_GROUP) if str(LOG_GROUP).startswith("-100") else LOG_GROUP))
        reply_markup.append([InlineKeyboardButton("💮𝐋𝐨𝐠 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🌺", url=invite_link.invite_link)])
    return await message.reply_text 
(f"👋 𝐇𝐢! {message.from_user.first_name},𝐈 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮 𝐟𝐢𝐧𝐝 𝐦𝐮𝐬𝐢𝐜 🎶 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐬𝐨𝐦𝐞 𝐨𝐟 𝐭𝐡𝐢𝐬⭐️🎵𝐒𝐨𝐧𝐠 𝐭𝐢𝐭𝐥𝐞 𝐨𝐫 𝐚𝐫𝐭𝐢𝐬𝐭⭐️🔤 𝐋𝐲𝐫𝐢𝐜𝐬 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐬𝐨𝐧𝐠✍️🎙 𝐕𝐨𝐢𝐜𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐰𝐢𝐭𝐡 𝐦𝐮𝐬𝐢𝐜🧡📹 𝐕𝐢𝐝𝐞𝐨 𝐰𝐢𝐭𝐡 𝐦𝐮𝐬𝐢𝐜⭐️🔊 𝐀𝐮𝐝𝐢𝐨 𝐫𝐞𝐜𝐨𝐫𝐝𝐢𝐧𝐠🎁🎥 𝐕𝐢𝐝𝐞𝐨 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐰𝐢𝐭𝐡 𝐦𝐮𝐬𝐢𝐜⭐️🔗 𝐋𝐢𝐧𝐤 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨 𝐭𝐨 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦🌐, 𝐓𝐢𝐤-𝐓𝐨𝐤🌐, 𝐘𝐨𝐮𝐓𝐮𝐛𝐞▶️ 𝐚𝐧𝐝 𝐨𝐭𝐡𝐞𝐫 𝐬𝐢𝐭𝐞𝐬⭐️ 
𝐃𝐞𝐯𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 🚩@Rishu1286✅️🕺 𝐄𝐧𝐣𝐨𝐲🥀",
                    reply_markup=InlineKeyboardMarkup(reply_markup))

@Mbot.on_message(filters.command("restart") & filters.chat(OWNER_ID) & filters.private)
async def restart(_,message):
    await message.delete()
    execvp(sys.executable,[sys.executable,"-m","mbot"])

@Mbot.on_message(filters.command("log") & filters.chat(SUDO_USERS))
async def send_log(_,message):
    await message.reply_document("bot.log")

@Mbot.on_message(filters.command("ping"))
async def ping(client,message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ms = (datetime.now() - start).microseconds / 1000
    await message.reply_text(f"**Pong!**\nResponse time: `{ms} ms`")

HELP = {
    "Youtube": "Send **Youtube** Link in Chat to Download Song.",
    "Spotify": "Send **Spotify** Track/Playlist/Album/Show/Episode's Link. I'll Download It For You.",
    "Deezer": "Send Deezer Playlist/Album/Track Link. I'll Download It For You.",
    "Jiosaavn": "Not Implemented yet",
    "SoundCloud": "Not Implemented yet",
    "Group": "Will add later."
}


@Mbot.on_message(filters.command("help"))
async def help(_,message):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await message.reply_text(f"Hello **{message.from_user.first_name}**, I'm bot of **@Ur_rishu_143**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))

@Mbot.on_callback_query(filters.regex(r"backdome"))
async def backdo(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await query.message.edit(f"Hello **{query.message.from_user.first_name}**, I'm bot of **@Ur_rishu_143**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))     
    
@Mbot.on_callback_query(filters.regex(r"help_(.*?)"))
async def helpbtn(_,query):
    i = query.data.replace("help_","")
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Back",callback_data="helphome")]])
    text = f"Help for **{i}**\n\n{HELP[i]}"
    await query.message.edit(text = text,reply_markup=button)

@Mbot.on_callback_query(filters.regex(r"helphome"))
async def help_home(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    await query.message.edit(f"Hello **{query.from_user.first_name}**, I'm bot of **@Ur_rishu_143**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))
