class TV:
    def __init__(self, brand: str, size: int):
        self.brand = brand
        self.size = size
        self.channel = 1
        self.volume = 10
        self.power = False

    def turn_on(self):
        self.power = True
        print("TV is turned on.")

    def turn_off(self):
        self.power = False
        print("TV is turned off.")

    def set_channel(self, channel: int):
        if self.power:
            self.channel = channel
            print(f"Channel set to {self.channel}.")
        else:
            print("TV is off. Please turn it on first.")

    def get_channel(self) -> int:
        if self.power:
            return self.channel
        else:
            print("TV is off. Please turn it on first.")
            return None

    def volume_up(self):
        if self.power:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is at maximum.")
        else:
            print("TV is off. Please turn it on first.")

    def volume_down(self):
        if self.power:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is at minimum.")
        else:
            print("TV is off. Please turn it on first.")

    def get_volume(self) -> int:
        if self.power:
            return self.volume
        else:
            print("TV is off. Please turn it on first.")
            return None

# Example usage
tv = TV("Sony", 55)
tv.turn_on()
tv.set_channel(5)
print("Current channel:", tv.get_channel())
tv.volume_up()
print("Current volume:", tv.get_volume())
tv.turn_off()
