import discord
import re
import time
import youtube_dl
token = 'Mjk0MTM1Mjg0MjczMjUwMzA1.C7QukQ.gSdGLmWXhKsvjHf9CYgYfCQQfPw'
client = discord.Client()



@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    discord.opus.load_opus('libopus-0.dll')
    print('Opus loaded =', discord.opus.is_loaded())

@client.event
async def on_message(message: discord.Message):
    #if message.author == client.user.name:
     #   return
    usr = message.author
    print(usr, message.content)  # chatlogger

    if message.content.startswith('--join'):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)

        if len(message.attachments) > 0:
            urls = [message.attachments[0]['url']]
        join_channel = usr.voice.voice_channel
        print(join_channel)
        voice = await client.join_voice_channel(join_channel)
        player = await voice.create_ytdl_player(urls[0])
        player.start()

    global millisecond
    global ping

    if message.content.startswith('ping'):

        millisecond = int(round(time.time() * 1000))
        print(millisecond)
        await client.send_message(message.channel, 'pong')
        print (client.user)
    if message.content.startswith('pong') and message.author == client.user:
        ping = int(round(time.time() * 1000))
        print (ping)
        print (ping - millisecond)
        await client.send_message(message.channel, ping - millisecond)



    if (message.content.startswith('leave')):
        await discord.VoiceClient.disconnect()
client.run(token)
