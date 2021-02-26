import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True
client=discord.Client(intents=intents)

client=commands.Bot(command_prefix='-')
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle,activity=discord.Game('Python'))
	print("the bot is ready")

@client.command()
async def hi(ctx):
    await ctx.reply('hi **how can i help you!**')

@client.command()
async def ping(ctx):
    await ctx.reply(f'**pong!** {round (client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member):
    await ctx.guild.ban(member)
    await ctx.send(f"{member.mention} has been **banned** from the server")

@client.command()
async def unban(ctx, *, member):
	banned_users=await ctx.guild.bans()
	member_name,member_discriminator=member.split('#')

	for ban_entry in banned_users:
		user=ban_entry.user

		if (user.name,user.discriminator)==(member_name,member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'{user.mention} is **Unbanned**')
			return

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member):
    await ctx.guild.kick(member)
    await ctx.send(f"{member.mention} has been **kicked** from the server")

@client.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)
    
@client.command()    
async def cmd(ctx):
    await ctx.reply('**moderation->** **kick**,**ban**,**clear**,**unban**,**warn** and **mute**')    	

client.run("YOUR TOKEN")
