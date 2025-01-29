import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from nextcord import permissions


def main():
    client = commands.Bot()

    @client.slash_command(description="Ping - pong!")
    async def ping(interaction: nextcord.Interaction):
        await interaction.send("Pong!", ephemeral=True)

    client.run('token')


if __name__ == '__main__':
    main()
