import os
import json
import random
import discord
from discord.ext import commands

#playlist path
#path = "/home/pi/Downloads"
TOKEN = 'NzcwNDMyMTA0MzU4MDg0NjM5.X5dezw.D-WmwOvO9FUExkRMguhlROk4Hso'
client = commands.Bot(command_prefix = '!')
folder = "/path/to/the/video/folder"

#ll = input('Server Mode? *Be sure to have ssh on?: ')

@client.event
async def on_ready():
  #opens json file
  f = open('main.json')
  data = json.load(f)
  for i in data["overall"]:
    #iter in the json, sections of overall
    #opens channel and path every ilter
    channel = client.get_channel(742148980682784793)
    videoList = os.system(folder) #for json; do videoList = os.listdir(i['name']) 

    m_index = 0
    for i in data['overall']:
      m_index += 1 
      video = i['path' + str(m_index)]

      dur = i['dur' + str(m_index)]
      desc = i['desc' + str(m_index)]
      genre = i['genre' + str(m_index)]


      target = os.path.join(videoList, video)
      res_str = video.replace('.mp4', '')
      await channel.send(res_str + ' is playing')
      await channel.send(i['desc' + str(m_index)])
      os.system('omxplayer "{}" > /dev/null'.format(target))
      open_w = open('current.txt', 'r+')
      #open txt file, then clears, then writes name of file name - .mp4
      open_w.truncate(0)
      open_w.write(res_str + '\n') 
      open_w.write(dur)
      open_w.write(desc)
      open_w.write(genre)
      #video is playing, add commands below


@client.command
async def movie(ctx, member: discord.Member = None):
  #reads the txt file to read lines 1 n 2
  current = open('current.txt', 'r')
  Lines = current.readlines()
  #for oo in range(len(Lines)):
    #does this for how many lines written in the txt
    #await ctx.send(Lines[oo])
    
  #Line0 = path
  #Line1 = duration
  #Line2 = description
  #Line3 = genre
  member = ctx.author if not member else member
  embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Current Moive Playing")
  embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.add_field(name="Movie Title", value = Lines[0], inline=False)
  embed.add_field(name="Duration", value = Lines[1], inline=False)
  embed.add_field(name="Description", value = Lines[2], inline=False)
  embed.add_field(name="Genre", value = Lines[3], inline=False)
  embed.set_image(url= 'https://media.istockphoto.com/photos/people-in-the-cinema-auditorium-with-empty-white-screen-picture-id1131545834')
  

  await ctx.send(embed=embed)
  

client.run(TOKEN)