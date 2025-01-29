import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption
from nextcord import permissions
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


    @client.slash_command(description="Ping - pong!")
    @application_checks.has_permissions(administrator=True)
    async def ping(interaction: Interaction):
        await interaction.response.send_message("Pong!", ephemeral=True)

    client.run(config.get_bot_token())


if __name__ == '__main__':
    main()
