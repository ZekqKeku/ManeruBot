import os
import json
import datetime
import calendar


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


class DateTools:
    @staticmethod
    def short_year(year: int):
        current_year = str(datetime.datetime.now().year)
        year_str = str(year)

        if len(year_str) == 3:
            return int(current_year[:1] + year_str)
        elif len(year_str) == 2:
            return int(current_year[:2] + year_str)
        elif len(year_str) == 1:
            return int(current_year[:3] + year_str)
        else:
            return int(current_year)

    @staticmethod
    def is_date_in_past(year, month, day):
        selected_date = datetime.datetime(year, month, day).date()
        current_date = datetime.datetime.today().date()

        return selected_date < current_date

    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]
