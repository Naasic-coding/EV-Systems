import discord
from discord.ext import commands
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.now()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Moderation Cog Loaded")

    @commands.hybrid_command(name='warn', aliases=['warning'])
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx: commands.Context, user: discord.Member, *, reason: str):
        embed = discord.Embed(title="You have issued a warning!", color=0xc3e0ff)
        embed.add_field(name="Warned User:", value=user.mention, inline=False)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))