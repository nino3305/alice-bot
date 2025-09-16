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



bot.run(TOKEN)















