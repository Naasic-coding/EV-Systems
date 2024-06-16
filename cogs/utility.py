import discord
from discord.ext import commands
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.now()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Utility Cog Loaded")

    @commands.hybrid_command(name='ping', aliases=['p', 'pong'])
    async def ping(self, ctx: commands.Context):
        current_time = datetime.datetime.now()
        uptime = current_time - self.start_time
        days, seconds = uptime.days, uptime.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"

        embed = (
            discord.Embed(title="Pong!", color=0xc3e0ff)
        .add_field(name="**Latency:**", value=f"``{round(self.bot.latency * 1000)}ms``", inline=False)
        .add_field(name="\u200b", value="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        .add_field(name="**Uptime:**", value=f"``{uptime_str}``", inline=False)
        .set_thumbnail(url=self.bot.user.avatar.url)
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='info', aliases=['i', 'information'])
    async def   info(self, ctx: commands.Context):
        embed = (
            discord.Embed(title="Welcome to EV systems", color=0xc3e0ff)
        .add_field(name="**Info!**", value=f"Ran by <@506525614589870080>, this server is the official testing ground for his coding capabilities!", inline=False)
        .set_thumbnail(url=ctx.bot.user.avatar.url)
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='invite', aliases=['inv'])
    async def   invite(self, ctx: commands.Context):
        embed = discord.Embed(title="Bot invite!", color=0xc3e0ff)

async def setup(bot):
    await bot.add_cog(Utility(bot))
