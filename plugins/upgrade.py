"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	
	
	𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 :- **@MaHi_458**
	
	After Payment Send Screenshots Of 
        Payment To Admin @MaHi_458"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  𝙼𝚊𝚑𝚎𝚜𝚑.𝚂  👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	
	
	𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 :- **@MaHi_458**
	
	After Payment Send Screenshots Of 
        Payment To Admin @MaHi_458"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  𝙼𝚊𝚑𝚎𝚜𝚑.𝚂  👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
