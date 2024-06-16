import os 
import discord
import asyncio
from discord.ext import commands
from discord import app_commands
import datetime 
import logging

# _________________________________

logging.basicConfig(level=logging.ERROR) 

intents = discord.Intents.all() 
intents.presences=False
bot = commands.Bot(command_prefix="=", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    await bot.load_extension("jishaku")
    await bot.tree.sync()
    print(f"Logged in as {bot.user.name}")


# -- Start time
start_time = datetime.datetime.now() 

# Global error handler 
@bot.event
async def on_command_error(ctx, error):
    try:
        if isinstance(error, commands.MissingPermissions):
            embed = (
                discord.Embed(title="Uh oh!", description="Looks like you've encountered an error!", color=0xc3e0ff)
            .add_field(name="**Error:**", value=f"``You do not have permission to run this command``", inline=False)
            .add_field(name="**Support server:**", value="[Invite](https://discord.gg/avkHewUTgf)", inline=False)
            .set_thumbnail(url=ctx.bot.user.avatar.url)
            )
            await ctx.reply(embed=embed, ephemeral=True)
        
        elif isinstance(error, commands.CommandNotFound):
            embed = (
                discord.Embed(title="Uh oh!", description="Looks like you've encountered an error!", color=0xc3e0ff)
            .add_field(name="**Error:**", value=f"``Not a command!`` If you believe this is a mistake, please refer to the support server!", inline=False)
            .add_field(name="**Support server:**", value="[Invite](https://discord.gg/avkHewUTgf)", inline=False)
            .set_thumbnail(url=ctx.bot.user.avatar.url)
            )
            await ctx.reply(embed=embed, ephemeral=True)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed = ( 
                discord.Embed(title="Uh oh!", description="Looks like you've encountered an error!", color=0xc3e0ff)
            .add_field(name="**Error:**", value=f"``Missing required arguments``", inline=False)
            .add_field(name="**Support server:**", value="[Invite](https://discord.gg/avkHewUTgf)", inline=False)
            .set_thumbnail(url=ctx.bot.user.avatar.url)
            )
            await ctx.reply(embed=embed, ephemeral=True)

        elif isinstance(error, commands.MemberNotFound):
            embed = (
                discord.Embed(title="Uh oh!", description="Looks like you've encountered an error!", color=0xc3e0ff)
            .add_field(name="**Error:**", value=f"``Member not found!``", inline=False)
            .add_field(name="**Support server:**", value="[Invite](https://discord.gg/avkHewUTgf)", inline=False)
            .set_thumbnail(url=ctx.bot.user.avatar.url)
            )
            await ctx.reply(embed=embed, ephemeral=True)
        
        else:
            error_message = str(error)
            
            if len(error_message) > 1024:
                error_message = error_message[:1021 ] + "..."
                
            embed = (
                discord.Embed(title="Unknown Error", description="Looks like you've encountered an unsual error, please refer to the support server!")
                .add_field(name="**Error:**", value=str(error), inline=False)
                .add_field(name="**Support server:**", value="[Invite](https://discord.gg/avkHewUTgf)", inline=False)
            )
            
            await ctx.send(embed=embed)
      
    except discord.errors.HTTPException as http_error:
        logging.error(f"HTTP Exception: {http_error}")
        await ctx.send("An error occurred while handling another error. Please try again later or contact support.")
        
    except Exception as error:
        logging.error(f"Failed to handle error: {error}")
        await ctx.send("An error occurred while handling another error. Please try again later or contact support.")

#____________________________________________________________________________________________________________________________________________________________      

# Bot run

async def main():
    async with bot:
        await bot.load_extension('cogs.utility')
        await bot.load_extension('cogs.moderation')
        await bot.start(os.getenv("Token"))

if __name__ == "__main__":
    asyncio.run(main())