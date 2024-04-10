class Tvremote:
    def init(self):
        self.channel = 0
        self.volume_level = 0
        self.on = False
    def to_string(self):
        return f"channel: {self.channel},volume level:{self.volume_level}"
    