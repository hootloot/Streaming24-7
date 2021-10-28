import os
import json
import random
import discord
from discord.ext import commands

#PLAN for Oct 28 Comp sci class
#Work on last func (showings)
#Downloads videos, run program to test
#Fix

TOKEN = 'token'
client = commands.Bot(command_prefix = '!')
folder = "/path/to/the/video/folder"

@client.event
async def on_ready():
  #opens json file
  f = open('main.json')
  data = json.load(f)
  m_index = 0
  for i in data["overall"]:    
    #IN THIS FUNC MAKE THE PROCESS MORE EFFICENT WITH USE OF LOOPS/DICT (type hint for json reading/writing?)
    channel = client.get_channel(742148980682784793)
    videoList = os.system(folder) #for json; do videoList = os.listdir(i['name']) 
    m_index += 1 
    video = i['path' + str(m_index)]
    dur = i['dur' + str(m_index)]
    desc = i['desc' + str(m_index)]
    genre = i['genre' + str(m_index)]
    target = os.path.join(videoList, video)
    res_str = video.replace('.mp4', '')
    #sending messages; plan to send an embed instead
    await channel.send(res_str + ' is playing')
    await channel.send(i['desc' + str(m_index)])
    os.system('omxplayer "{}" > /dev/null'.format(target))
    open_w = open('current.txt', 'r+')
    open_w.truncate(0)
    open_w.write(res_str + '\n') 
    open_w.write(dur + '\n')
    open_w.write(desc + '\n')
    open_w.write(genre + '\n')


@client.command(name = "help")
#help looks fine, but plan to use thumbnail instead of a image
async def help(ctx,  member: discord.Member = None):
  member = ctx.author if not member else member
  embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="How To Use The Bot")
  embed.set_footer(text=f"yeye, {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_footer(text = "More Commands Coming Soon!")
  embed.add_field(name="**!movie**", value = "Information about the current moive playing")
  embed.set_image(url= 'https://media.istockphoto.com/photos/people-in-the-cinema-auditorium-with-empty-white-screen-picture-id1131545834')

  await ctx.send(embed=embed)

@client.command(name = "movie")
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
  Current_Movie = "Current Moive Playing: " + Lines[0]
  embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title=Current_Movie)
  embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_footer(text="Showing Current Moive")
  embed.add_field(name="Duration", value = Lines[1], inline=False)
  embed.add_field(name="Description", value = Lines[2], inline=False)
  embed.add_field(name="Genre", value = Lines[3], inline=False)
  embed.set_image(url= 'https://media.istockphoto.com/photos/people-in-the-cinema-auditorium-with-empty-white-screen-picture-id1131545834')
  
  await ctx.send(embed=embed)

@client.command(name = "showings")
#Plan to fix the structure of this code it is messey
#move the embed context code under the for loop (can it send messages under a loop?)
async def showings(ctx, member: discord.Member = None):
  member = ctx.author if not member else member
  embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Movie Showings")
  embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
  f = open('main.json')
  data = json.load(f)
  i_index = 0
  for i in data["overall"]:
    i_index += 1
    embed.set_footer(text="The " + str(i_index) + "rd Movie")
    embed.add_field(name=i['path'] + str(i_index), value = i['desc' + str(i_index)])
    await ctx.send(embed=embed)
#open json
#for loop (overall)
#send a embed each time there is a movie for index
#Have footer/Name/Desc/i_index
#time module + the duration from json to caculate the when the movie will be on?
#plan to only show the next 5 movies or the next movies for all (depends on how many movies)

client.run(TOKEN)

