import json


class Settings:
    """A class to manage settings."""

    def __init__(self):
        """Initialize the settings."""
        self.raw = self.load_from_json()

    @staticmethod
    def load_from_json():
        """Load settings from a json file."""
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)
        except FileNotFoundError:
            settings = {}
        return settings
