from common import config
from discord import Embed, Colour, Color

hr='~~- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -~~'

# Default color variables
defaultColor = Color.from_rgb(**config.cfg["options"]["embed"]["color"]["default"])
errorColor = Color.from_rgb(**config.cfg["options"]["embed"]["color"]["error"])
def embed(**kwargs):
    """
    Created an embed from the provided details
    title - Title of embed
    description - Text in embed, pre body
    sections - list of (title,content) tuples
    body - list of entries to be seperated by a <hr>, follows sections
    colour - discord.Colour object to ovveride default
    url - webpage to link to
    thumbnail - url to image to display (small on the side of embed)
    image - url to image to display (large at bottom of embed)
    footer - Text to put at the bottom of the embed
    """
    embed=Embed()
    if ("title" in kwargs.keys()):
        embed.title = kwargs["title"]
    if ("description" in kwargs.keys()):
        embed.description = kwargs["description"]
    if ("sections" in kwargs.keys()):
        for elem in kwargs["sections"]:
            embed.add_field(name=elem[0],value=elem[1])
    if ("body" in kwargs.keys()):
        for elem in kwargs["body"]:
            embed.add_field(name=hr,value=elem)
    if ("colour" in kwargs.keys()):
        embed.colour = kwargs["colour"]
    elif ("color" in kwargs.keys()):
        embed.color = kwargs["color"] 
    else:
        embed.colour = defaultColor
    if ("url" in kwargs.keys()):
        embed.url = kwargs["url"]
    if ("thumbnail" in kwargs.keys()):
        embed.set_thumbnail(url=kwargs["thumbnail"])
    if ("image" in kwargs.keys()):
        embed.set_image(url=kwargs["image"])
    if ("footer" in kwargs.keys()):
        embed.set_footer(text=kwargs["footer"])
    return embed