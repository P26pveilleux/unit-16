class Tvremote:
    def init(self):
        self.channel = 0
        self.volume_level = 0
        self.on = False
    def to_string(self):
        return f"channel: {self.channel},volume level:{self.volume_level}"
    
    def turn_on(self):
        self.on = True 
    
    def self_off(self):
        self.off = False 
    
    def volume_up(self):
        if self.on:
            self.volume_level += 1 

    def volume_down(self):
        if self.on:
            if self.volume_level > 0:
                self.volume_level -= 1

    def channel_up(self):
        if self.on:
            self.channel += 1

    def channel_down(self):
        if self.on:
            if self.channel > 0:
                self.channel -= 1 