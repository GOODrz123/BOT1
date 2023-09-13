import discord
from discord.ext import commands

intents = discord.Intents.all()
token = "MTE0NzUwNTA2ODg0MTY0ODE3OA.GS7f0G.UxAx36AZhV6JqfFl3CO39-yQy8wAkV-pCDwmJ4"

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} 🟢Run Sod🟢')

@bot.event
async def on_disconnect():
   print(f'{bot.user.name} 🔴Off Sod🔴')

@bot.command()
async def off(ctx):
    await bot.close()


@bot.command()
async def salam(ctx):
   await ctx.send("salam")

@bot.command()
async def Bay(ctx):
   await ctx.send("goodBay")
  
@bot.command()
async def Developer(ctx):
   await ctx.send("goodrz123009")

@bot.command()
async def Big_Bang(ctx):
   await ctx.send("https://discord.gg/YDMagrVrzQ")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = "None"):
    
    Ownembed = discord.Embed(title=f"User Kicked", description=f"**Kicked User Name** : `{member.display_name}`\n"
    f"**kicked By** : `{ctx.author.display_name}`\n"
    f"**Reason** : `{reason}`", color= discord.Color.yellow())
    await member.kick(reason=reason)
    await ctx.send(embed=Ownembed)

bot.run(token)