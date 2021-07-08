## Initialization
import discord
from discord.ext import commands
from common import config, log, embedMessage, category

## Class setup
class selfDeaf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        ## Help stuff
        self.hidden = True

    ## Self deafen when voice state changes.
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, pre, post):
        if member == member.guild.me and member.voice.deaf == False:
            await member.guild.me.edit(deafen=True)

## Allow use of cog class by main bot instance
def setup(bot):
    bot.add_cog(selfDeaf(bot))