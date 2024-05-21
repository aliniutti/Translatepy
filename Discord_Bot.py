import discord
import requests
import random
from discord.ext import commands



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def translate(ctx, *, a:str):
    """Translate English to persian"""
    url="https://pipesyed.ir/Api/translate.php?lang=en&to=fa&text="+a
    r = requests.get(url = url)
    data= r.text
    print(a," translate to: ",data)
    
    embed = discord.Embed(
        title="ربات مترجم",
        description="ترجمه("+a+"): "+"\n\n"+"**"+data+"**",
        color=discord.Color.blue(),
        )
    await ctx.send(embed=embed)

@bot.command()
async def ترجمه(ctx, *,tr:str):
    """Translate Persian to English"""
    url="https://pipesyed.ir/Api/translate.php?lang=fa&to=en&text="+tr
    r = requests.get(url = url)
    data= r.text
    print(tr," translate to: ",data)
    
    embed = discord.Embed(
        title="ربات مترجم",
        description="Translate("+tr+"): "+"\n\n"+"**"+data+"**",
        color=discord.Color.red(),
        )
    await ctx.send(embed=embed)

@bot.command()
async def status(c,st):
    """Chooses Your Status"""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= st))
    print("Bot status change to: "+st)


# @bot.command()
# async def کمک(ctx):
#     embed = discord.Embed(
#         title="پروژه پایتون",
#         description="این یک ایمبد ساده برای پروژه پایتون است",
#         color=discord.Color.green(),
#     )
#     await ctx.send(embed=embed)


@bot.command()
async def cal(ctx, left: int,middle:str ,right: int):
    """Caculator Numbers"""
    print(middle)
    if middle == "+":{
    await ctx.send(left + right)
    }
    elif middle == "-" :{
    await ctx.send(left - right)
    }
    elif middle == "*" :{
    await ctx.send (left * right)
    }
    elif middle == "/":{
    await ctx.send(left / right)
    }
    else: {
    await ctx.send("please fill the middle world(+-*/)")
    }


@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    print (choices)
    await ctx.send(random.choice(choices))

@bot.command()
async def ping(ctx):
    """Get ping of your bot"""
    latency = bot.latency
    l = float(latency)
    d = 'ping: {:.2f}'.format(l)
    await ctx.send(d)

@bot.command()
async def purge(ctx, amount: int):
    """Purge Some message"""
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages have been deleted.')

@bot.event
async def on_ready():
    print('###############################################')
    print('#                Bot Run Shod!                #')
    print('#                   Ostad                     #') 
    print('###############################################')
    print('                                               ')
    print('                                               ')
    print('                                               ')
    print('                                               ')
    print('                                               ')
    print('                                               ')



    


bot.run("Bot Token")