class TV():
    def __init__(self):
        self.is_on =  False
        self.channel_no = 1
        self.available_channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on:
            print("TV is on, " + "channel " + str(self.channel_no))
            print("Current volume is " + str(self.volume))
        else:
            print("TV is off")
             
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.available_channels = channels_list

    def show_channels(self):
        string = ''
        for channel in self.available_channels:
            string += channel + " "
        print('Available channels: ' + string)

    def volume_up(self):
        if (self.volume < 10):
            self.volume += 1
        else:
            print("The volume is already on maximum")

    def volume_down(self):
        if (self.volume > 1):
            self.volume -= 1
        else:
            print("The volume is already on minimum")
        
    





channels_list = ["Polsat","Discovery","TVN","AXN","TLC","BBC","DisneyChannel"]
my_tv = TV()

my_tv.show_status()
my_tv.turn_on()
my_tv.show_status()
my_tv.turn_off()
my_tv.show_status()
my_tv.turn_on()
my_tv.set_channel(5)
my_tv.show_status()
my_tv.turn_off()
my_tv.show_status()
my_tv.set_channels(channels_list)
my_tv.show_channels()
my_tv.turn_on()
my_tv.volume_up()
my_tv.show_status()