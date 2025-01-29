import os
import json


class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Config file not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_bot_token(self):
        return self.config_data.get("bot", {}).get("token", "")

    def get_bot_app_id(self):
        return self.config_data.get("bot", {}).get("app_id", "")

    def get_discord_bot_admin_id(self):
        return self.config_data.get("discord", {}).get("bot_admin_id", [])

    def get_discord_guild_id(self):
        return self.config_data.get("discord", {}).get("guild_id", "")

