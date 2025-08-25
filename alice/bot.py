import os
import discord
from discord.ext import commands
print("DISCORD_TOKEN:", os.getenv("DISCORD_TOKEN"))

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # 必須啟用語音事件
bot = commands.Bot(command_prefix="!", intents=intents)

# 指定要發訊息的文字頻道 ID
TARGET_CHANNEL_ID = 1010848964981051424  # 換成你的文字頻道ID

@bot.event
async def on_ready():
    print(f"登入成功：{bot.user}")


    # 設定狀態
    activity = discord.Game(name="原神")  
    await bot.change_presence(status=discord.Status.online, activity=activity)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if "dot" in content:
        await message.channel.send("dot隊怎麼你了")
    elif "風堇" in content:
        await message.channel.send("有人提到二次元偶像嗎")
    elif "閉嘴" in content:
        await message.channel.send("😡😡😡")
    elif "黑塔" in content:
        await message.channel.send("感覺不如遐蝶一噴")
    elif "遐蝶" in content:
        await message.channel.send("感覺不如白厄一顆隕石")
    elif "白厄" in content:
        await message.channel.send("感覺不如Saber一棒")
    elif "saber" in content:
        await message.channel.send("感覺不如星見雅")
    elif "雅" in content:
        await message.channel.send("感覺不如我")

    await bot.process_commands(message)

# 偵測語音頻道進出
@bot.event
async def on_voice_state_update(member, before, after):
    # before.channel = 原本的語音頻道
    # after.channel  = 現在的語音頻道
    if before.channel is None and after.channel is not None:
        # 成員加入語音頻道
        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.send(f"🎤 {member.display_name} 加入了語音頻道 {after.channel.name}")
    elif before.channel is not None and after.channel is None:
        # 成員離開語音頻道
        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.send(f"👋 {member.display_name} 離開了語音頻道 {before.channel.name}")

@bot.event
async def on_typing(channel, user, when):
    if isinstance(channel, discord.TextChannel):
        await channel.send(
            f"💬 {user.display_name} 正在打字...",
            delete_after=15  # 5 秒後自動刪除
        )

bot.run(TOKEN)






