import discord, aiohttp, math
from discord.ext import commands

bot = commands.Bot(command_prefix = '/')

@bot.event
async def on_ready():
    print('Signed In as Math Bot')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('math'))




@bot.command()
async def add(ctx, arg: int, arg2: int):
    """Can be used to add /add {number} {number}"""
    ans = arg + arg2
    await ctx.send(f'The answer is {ans}')

@bot.command()
async def subtract(ctx, arg: int, arg2: int):
    """Can be used to subtract numbers /subtract {number} {number}"""
    ans = arg - arg2
    await ctx.send(f'The answer is {ans}')


@bot.command()
async def multiply(ctx, arg: int, arg2: int):
    """Can be used to multiply numbers /multiply {number} {number}"""
    ans = arg * arg2
    await ctx.send(f'The answer is {ans}')

@bot.command()
async def divide(ctx, arg: int, arg2: int):
    """Can be used to divide numbers /divide {number} {number}"""
    ans = arg / arg2
    await ctx.send(f'The answer is {ans}')

@bot.command(alias='sqrt')
async def squareroot(ctx, arg: int):
    """Gives square root of a number /sqrt {number} or /squareroot {number}"""
    ans = math.sqrt(arg)
    await ctx.send(f'The answer is {ans}')

# Errors 

@add.error
async def add_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please speficy all arguments')

@subtract.error
async def subtract_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please speficy all arguments')

@multiply.error
async def multiply_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please speficy all arguments')

@divide.error
async def diivide_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please speficy all arguments')

@squareroot.error
async def squareroot_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please speficy all arguments')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command! do /help for llist of commands')

# Ping Command

bot.command()
async def ping(ctx):
    """Returns Client Latency"""
    await ctx.send(f'**Pong!** Latency:{round(bot.latency * 1000)}ms')

try:
    file = open("token.txt",'r')
    token = file.read()
    file.close()
    bot.run(token)
except:
    print("Token.txt not found")




