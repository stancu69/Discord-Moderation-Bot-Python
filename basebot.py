import discord
from discord import Client
from discord.ext import commands, tasks
import random
import json
import os

client = commands.Bot("#")

@client.event
async def on_ready():
    changeStatus.start()
    print("bot is ONLINE!")

# Moderation

@client.command()
async def ip(ctx):
    await ctx.send("** **")

@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=9999999999):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")
    await ctx.send("https://giphy.com/gifs/trump-ban-LPHbzPcICc86EVte9C")


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discrminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(773284797866311691)
    await member.add_roles(muted_role)
    await ctx.send(f"{member.mention} Has been Muted")


@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(773284797866311691)
    await member.remove_roles(muted_role)
    await ctx.send(f"{member.mention} Has been Unmuted")


@tasks.loop(seconds=10)
async def changeStatus():
    status = random.choice(['Watching...........', 'Playing........', 'Dev: stancu#6969'])
    await client.change_presence(activity=discord.Game(status))

client.run("#yourtokenhere")