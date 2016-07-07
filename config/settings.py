from .dataIO import fileIO
import discord
import os

path = "config/settings.json"


class Settings:
    def __init__(self, path=path):
        self.path = path
        self.default_settings = {"EMAIL" : "EmailHere", "PASSWORD" : "", "OWNER" : "id_here", "PREFIXES" : [], "default":{"ADMIN_ROLE" : "Transistor", "MOD_ROLE" : "Process"}, "LOGIN_TYPE" : "email"}
        if not fileIO(self.path,"check"):
            self.bot_settings = self.default_settings
            self.save_settings()
        else:
            current = fileIO(self.path, "load")
            if current.keys() != self.default_settings.keys():
                for key in self.default_settings.keys():
                    if key not in current.keys():
                        current[key] = self.default_settings[key]
                        print("Adding " + str(key) + " field to red settings.json")
                fileIO(self.path, "save", current)
            self.bot_settings = fileIO(self.path,"load")

    def save_settings(self):
        fileIO(self.path,"save",self.bot_settings)