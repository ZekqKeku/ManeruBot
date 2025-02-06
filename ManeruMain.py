import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption, SelectOption, SelectMenu
import random
import datetime
from utils import ManeruUtils, ManeruDatabase


def main():
    client = commands.Bot()
    config = ManeruUtils.ConfigReader('config.json')
    super_users = config.get_discord_bot_admin_id()

    @client.event
    async def on_ready():
        print("Client is ready.")
        print(f"Bot name: {client.user.name}")
        print(f"Bot id: {client.user.id}")
        print(f"App id: {config.get_bot_app_id()} - (config file)")

    @client.event
    async def on_message(message):
        gif = ["https://tenor.com/view/purple-guy-lore-gif-24356620",
               "https://tenor.com/view/mikfajter-mikfaighter-mickfighter-mickfajter-gif-3545257223889794839",
               "https://tenor.com/view/pteranodo-jp2pteranodon-jp2-jurassic-park-jurassic-park2-gif-18459492",
               "https://tenor.com/view/ice-age-diego-ice-age-diego-saber-tooth-tiger-dance-gif-9226858265849426684"]
        if 'aftonek' in str(message.content).lower():
            if random.uniform(0, 100) <= 0.01:
                await message.channel.send("Szablozębnik?")
                await message.channel.send(gif[random.randint(0, len(gif)-1)])

    @client.slash_command(description="Ping - pong!")
    @application_checks.has_permissions(administrator=True)
    async def ping(interaction: Interaction):
        await interaction.response.send_message("Pong!", ephemeral=True)

    @client.slash_command(name="proposal", description="Send proposal of meeting date")
    @application_checks.has_permissions(administrator=True)
    async def proposal(interaction: Interaction,
                       title: str = SlashOption(name="title",
                                                description="Title",
                                                required=True),
                       description: str = SlashOption(name="description",
                                                      description="Description",
                                                      required=True),
                       hour: int = SlashOption(name="hour",
                                               description="Hour",
                                               required=True,
                                               min_value=0,
                                               max_value=23),
                       minute: int = SlashOption(name="minute",
                                                 description="Minute",
                                                 required=True,
                                                 min_value=0,
                                                 max_value=59),
                       day: int = SlashOption(name="day",
                                              description="Day",
                                              required=True,
                                              min_value=1,
                                              max_value=31),
                       month: int = SlashOption(name="month",
                                                description="Month (if not selected, set current month)",
                                                required=False,
                                                choices={
                                                  "January": 1,
                                                  "February": 2,
                                                  "March": 3,
                                                  "April": 4,
                                                  "May": 5,
                                                  "June": 6,
                                                  "July": 7,
                                                  "August": 8,
                                                  "September": 9,
                                                  "October": 10,
                                                  "November": 11,
                                                  "December": 12}),
                       year: int = SlashOption(name="year",
                                               description="Year (if not selected, set current year)",
                                               required=False,
                                               min_value=0,
                                               max_value=datetime.datetime.now().year+50)):
        message = await interaction.response.send_message("Thinking...", ephemeral=True)

        months= {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        date = datetime.datetime.now()
        if month == None: month = date.month
        if year == None: year = date.year
        else: year = ManeruUtils.DateTools.short_year(year)

        if day > ManeruUtils.DateTools.get_days_in_month(year, month):
            await message.edit(content="Day value is invalid", delete_after=5)
            return -1

        if ManeruUtils.DateTools.is_date_in_past(year, month, day, hour, minute):
            await message.edit(content="This date has passed", delete_after=5)
            return -1

        embed = nextcord.Embed(
            title=f"**{title}**",
            description=f"_{description}_",
            color=0xFFFFFF,
            timestamp=datetime.datetime.now(),
        )
        embed.add_field(name="**Date**",
                        value=f"_{ManeruUtils.DateTools.short_number(day)} {months[month]} {year}_",
                        inline=True)
        str_hour = ManeruUtils.DateTools.short_number(hour)
        str_minute = ManeruUtils.DateTools.short_number(minute)
        embed.add_field(name="**Time**",
                        value=f"_{str_hour}:{str_minute}_",
                        inline=True)
        embed.set_footer(text=f"Requested by {str(interaction.user).capitalize()}")
        embed.set_thumbnail(url="attachment://calendar.png")
        file = nextcord.File("static/calendar.png", filename="calendar.png")

        await message.edit(content="", embed=embed, file=file)
        return 0

    client.run(config.get_bot_token())


if __name__ == '__main__':
    main()
