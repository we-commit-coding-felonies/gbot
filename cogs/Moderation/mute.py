## Initialization
import discord
from discord.ext import commands
from common import config, embedMessage, category, modFunc

## Class setup
class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        ## Help stuff
        self.hidden = False
        self.category = category.getCategory(self.__module__)
        self.description = "Mutes the specified user"
        self.usage = f"""
        {config.cfg['options']['prefix']}mute <@user> <reason>
        """

    ## Mutes target
    @commands.command(aliases=['gag','shutup','stfu'])
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, target: discord.Member, *args):
        if len(args) > 1:
            reason = " ".join(args)
        elif len(args) == 1:
            reason = args[0]
        else:
            reason = f'Muted by {ctx.author}'
        muteOverwrite = discord.PermissionOverwrite()
        muteOverwrite.add_reactions = False
        muteOverwrite.send_messages = False
        muteOverwrite.speak = False
        muteOverwrite.stream = False
        if target == ctx.author:
            embed = embedMessage.embed(
            title = 'ERROR',
            description = f'You cannot mute yourself!',
            color = embedMessage.errorColor
            )
            await ctx.send(embed=embed)
            return
        if target == self.bot.user:
            embed = embedMessage.embed(
            title = f'twitter.com: @{self.bot.user.display_name} updated their status',
            description = f'***I\'ve come to make an announcement: {ctx.author.mention}\'s a bitch-ass motherfucker. He pissed on my fucking wife. That\'s right, he took his hedgehog fuckin\' quilly dick out and he pissed on my fucking wife, and he said his dick was \"THIS BIG\", and I said \"That\'s disgusting!\" So I\'m making a callout post on my Twitter dot com. {ctx.author.mention}, you got a small dick! It\'s the size of this walnut except WAY smaller! And guess what? Here\'s what my dong looks like! That\'s right, baby! All points, no quills, no pillows, look at that, it looks like two balls and a bong! He fucked my wife, so guess what, I\'m gonna fuck the Earth! That\'s right, this is what you get, my SUPER LASER PISS! Except I\'m not gonna piss on the Earth, I\'m gonna go higher. I\'m pissing on the MOON! HOW DO YOU LIKE THAT, OBAMA? I PISSED ON THE MOON, YOU IDIOT!  You have 23 hours before the piss DRRRROPLLLETS hit the fucking Earth! Now get out of my fucking sight, before I piss on you too!***',
            color = discord.Color.from_rgb(42, 169, 224)
            )
            await ctx.send(embed=embed)
            return
        await modFunc.mute(target, reason)
        embed = embedMessage.embed(
            title = 'SUCCESS',
            description = f'{target.mention} has been muted.'
        )
        await ctx.send(embed=embed)

## Allow use of cog class by main bot instance
def setup(bot):
    bot.add_cog(mute(bot))