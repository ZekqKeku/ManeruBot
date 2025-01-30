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
                await message.channel.send(gif[random.randint(0, len(gif) - 1)])

    @client.slash_command(description="Ping - pong!")
    @application_checks.has_permissions(administrator=True)
    async def ping(interaction: Interaction):
        await interaction.response.send_message("Pong!", ephemeral=True)


    # @todo Automation of limits realitivie to the current date
    @client.slash_command(name="proposal", description="Send proposal of meeting date")
    @application_checks.has_permissions(administrator=True)
    async def proposal(interaction: Interaction,
                       title: str = SlashOption(name="title",
                                                description="Title",
                                                required=True),
                       description: str = SlashOption(name="description",
                                                      description="Description",
                                                      required=True),
                       day: int = SlashOption(name="day",
                                              description="Day",
                                              required=True,
                                              min_value=1,
                                              max_value=31),
                       month: int = SlashOption(name="month",
                                                description="Month (if not selected, set current month)",
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
                       # month: int = SlashOption(name="month",
                       #                          description="Month (if not selected, set current month)",
                       #                          min_value=1,
                       #                          max_value=12),
                       year: int = SlashOption(name="year",
                                               description="Year (if not selected, set current year)",
                                               min_value=2025,
                                               max_value=2125)):
        test_payload = f'''\n
        **Date:** {day} - {month} - {year}
        **Title:** {title}
        **Description:** {description}
        '''
        await interaction.response.send_message(test_payload, ephemeral=True)


    client.run(config.get_bot_token())


if __name__ == '__main__':
    main()
