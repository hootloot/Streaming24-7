import os
import json
import random
import discord
from discord.ext import commands
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime, timedelta

TOKEN = 'ODA2ODg0MDI2MzA3NzA2OTEx.YBv7Tw.Xz3KmDQj3ZeJCXDOxe8hlwFRcoE'
client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
  f = open('main.json')
  data = json.load(f)
  m_index = 0
  current_time = datetime.now()
  current_open = open('showings.txt', 'r+')

  for i in data["overall"]:    
    channel = client.get_channel(742148980682784793)
    m_index += 1
    video = i['path' + str(m_index)]
    dur = i['dur' + str(m_index)]
    desc = i['desc' + str(m_index)]
    genre = i['genre' + str(m_index)]



    current_time += timedelta(hours=dur)
    current_open.write(current_time)
    #rewrote to open showings txt to have writing 
    #write some code to read the txt file and have proper showings

    res_str = video.replace('.mp4', '')

    embed = discord.Embed(color=0x5207df, timestamp=channel.message.created_at, title = res_str + ' is playing')
    embed.set_footer(text=f"yeye, {channel.author}", icon_url=channel.author.avatar_url)
    embed.set_footer(text = i['desc' + str(m_index)])
    embed.add_field(name="**!movie**", value = "Information about the current moive playing")
    embed.set_image(url= 'https://media.istockphoto.com/photos/people-in-the-cinema-auditorium-with-empty-white-screen-picture-id1131545834')

    await channel.send(embed=embed)
    
    #og await
    #await channel.send(res_str + ' is playing')
    #await channel.send(i['desc' + str(m_index)])
    open_w = open('current.txt', 'r+')
    open_w.truncate(0)
    open_w.write(res_str + '\n') 
    open_w.write(str(dur) + '\n')
    open_w.write(desc + '\n')
    open_w.write(genre + '\n')

    #this change in structure may fix the og issue
    target = os.path.join(video)

    os.system('omxplayer "{}" > /dev/null'.format(target))


@client.command(name = "info")
async def info(ctx,  member: discord.Member = None):
  member = ctx.author if not member else member
  embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="How To Use The Bot")
  embed.set_footer(text=f"yeye, {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.set_footer(text = "More Commands Coming Soon!")
  embed.add_field(name="**!movie**", value = "Information about the current moive playing")
  embed.set_image(url= 'https://media.istockphoto.com/photos/people-in-the-cinema-auditorium-with-empty-white-screen-picture-id1131545834')

  await ctx.send(embed=embed)


@client.command(name = "movie")
async def movie(ctx, member: discord.Member = None):
  current = open('current.txt', 'r')
  Lines = current.readlines()
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


client.run(TOKEN)
