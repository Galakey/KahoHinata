import discord
from discord.ext import commands
import json
import pendulum


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, user):
        with open(".\config.json") as file:
            contents = json.loads(file.read())
            channel = int(contents['kaho']['welcome_channel'])
        file.close()
        emoji = discord.utils.get(user.guild.emojis, name="RC_Ohearts")
        welcome_embed = discord.Embed(description=f"\n{emoji} **To access the server, verify in <#744296908083822653>!**"
                                                  f"\nRead through our rules in <#646870858895458304>"
                                                  f"\nPick some roles in <#646870871809720320>"
                                                  f"\nEnjoy your stay! ♡",
                                      color=0xa0ebe4)
        welcome_embed.set_footer(text=f"You are user {user.guild.member_count}")
        welcome_embed.timestamp = pendulum.now('UTC')

        await self.bot.get_channel(channel).send(f"Welcome {user.mention} to Reisei Cafe!~", embed=welcome_embed)

    @commands.command()
    async def test(self, ctx):
        await ctx.send(pendulum.now('UTC').diff_for_humans())


async def setup(bot):
    # take name of class, pass in the bot
    await bot.add_cog(Welcome(bot))
