#shows up in allatv.txt as name,max_channel,channel,max_volume,volume
class TV:  

    #create the TV object
    def __init__(self, tv_name = "Default TV", max_channel = 100, current_channel = 1, max_volume = 100, current_volume = 50):
        self.tv_name = tv_name
        self.current_volume = current_volume
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.max_channel = max_channel

    #change the channel if the new channel is valid
    def change_channel(self, new_channel):
        if(new_channel <= self.max_channel and new_channel > 0 and new_channel != self.current_channel):
            self.current_channel = new_channel
            return True
        return False

    def increase_volume(self):
        return self.change_volume(1)

    def decrease_volume(self):
        return self.change_volume(-1)
    
    #change the volume if the new volume is valid
    def change_volume(self, additional_volume):
        if(self.current_volume + additional_volume <= self.max_volume and self.current_volume + additional_volume >= 0):
            self.current_volume += additional_volume
            return True
        return False

    
    def __str__(self):
        return str(self.tv_name) + "\nchannel: " + str(self.current_channel) + "\nvolume: " + str(self.current_volume)
    
    #the format in which the TV object is written to the file
    def str_for_file(self):
        return str(self.tv_name) + "," + str(self.current_channel) + "," + str(self.current_volume) + "," + str(self.max_volume) + "," + str(self.max_channel) + "\n"
