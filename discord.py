import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome to the server, {member.mention}!')

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'{member.mention}, has left a server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hello!')

    await client.process_commands(message)

@client.command()
async def kick(ctx, member: discord.Member, * , reason = None):
    await member.kick(reason = reason)
    channel = discord.utils.get(member.guild.channels, name='general')
    await ctx.send(f'{member} has been kicked for {reason}')

@client.command()
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member} has been banned.')



@client.command()
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f'{member} has been muted.')


@client.command()
async def clear(ctx,amount = 5):
    await ctx.channel.purge(limit= amount)




client.run("MTA4NDE2ODA5NzM4NjIyMTYwOA.G6Nk27.sY83mZLisT4_d4Zwnca8zFXGjYqlCu9AwEtMZo")