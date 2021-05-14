from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nThis is a Telegram YouTube Download Bot!\n\n<b>Please send me any YouTube Link, I can upload to telegram as File/Video</b>\n\n/help for More info"
    raise StopPropagation
