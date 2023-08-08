from config import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            userid = message.from_user.id 
            user_name = message.from_user.first_name
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"'🚧 ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ ʙᴏᴛ ᴄʜᴀɴɴᴇʟ ⚠️\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\n⌯︙W⃟ᴇʟᴄᴏᴍᴇ :[{message.from_user.first_name}](tg://user?id={message.from_user.id})\n⌯︙🏝️ **ʙᴏᴛ ᴄʜᴀɴɴᴇʟ :** ||[S⃟ᴏʟᴏ ᴛʀᴇᴇ]({link})||\n┉───┈┈╌╍╌┄┈───┉┉───┈┈╌\nᴛᴏ ᴜsᴇ ᴍᴇ. Aғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ Jᴏɪɴ ᴄʜᴀɴɴᴇʟ  ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
