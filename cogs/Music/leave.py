## Initialization
import discord
from discord.ext import commands
from common import config, embedMessage, category

## Class setup
class leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        ## Help stuff
        self.hidden = False
        self.category = category.getCategory(self.__module__)
        self.description = "Makes the bot disconnect from the voice channel it is connected to."
        self.usage = f"""
        {config.cfg['options']['prefix']}leave
        """

    ## Command defining
    @commands.command(aliases=['fuckoff', 'disconnect', 'dc'])
    @commands.has_guild_permissions(connect=True)
    async def leave(self, ctx):
        if ctx.me.voice == None:
            embed = embedMessage.embed(
                title = 'ERROR',
                description = 'I am not connected to a voice channel!',
                color = embedMessage.errorColor
            )
            await ctx.send(embed=embed)
            return
        currentChannel = ctx.me.voice.channel
        if ctx.author.voice.channel != currentChannel:
            embed = embedMessage.embed(
                title = 'ERROR',
                description = 'You must be connected to the same voice channel as the bot to disconnect it.',
                color = embedMessage.errorColor
            )
            await ctx.send(embed=embed)
            return
        await ctx.voice_client.disconnect()
        embed = embedMessage.embed(
            title = 'SUCCESS',
            description = f'Left **{currentChannel}**.'
        )
        await ctx.send(embed=embed)

    ## Reset queue stuff to default
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, pre, post):
        if pre.channel != None:
            if member.id == member.guild.me.id and not post.channel:
                self.bot.player.queue[member.guild.id] = []
                self.bot.player.loopQueue[member.guild.id] = False

## Allow use of cog class by main bot instance
def setup(bot):
    bot.add_cog(leave(bot))