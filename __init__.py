from mycroft import MycroftSkill, intent_handler
import subprocess

class ZigbeeLightController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def send_command(self,command):
        process = subprocess.run(['mqttcli', 'pub', '-t', 'zigbee2mqtt/group_1/set', '-m', command],
                                 stdout=subprocess.PIPE, universal_newlines=True)
        #process = subprocess.run(['mqttcli', 'pub', '-t', 'zigbee2mqtt/0x680ae2fffe2cc3b4/set', '-m', command],
        #                         stdout=subprocess.PIPE, universal_newlines=True)
        #process = subprocess.run(['mqttcli', 'pub', '-t', 'zigbee2mqtt/0xec1bbdfffeb4c3e5/set', '-m', command],
        #                         stdout=subprocess.PIPE, universal_newlines=True)

    @intent_handler('lights.bright.intent')
    def handle_controller_lights_bright(self, message):
        self.send_command('{"state":"ON","transition":1,"brightness": 255}')
        #self.speak_dialog('controller.light.zigbee')

    @intent_handler('lights.dim.intent')
    def handle_controller_lights_dim(self, message):
        self.send_command('{"state":"ON","transition":1,"brightness": 1}')
        #self.speak_dialog('controller.light.zigbee')

    @intent_handler('lights.medium.intent')
    def handle_controller_lights_medium(self, message):
        self.send_command('{"state":"ON","transition":1,"brightness": 100}')
        #self.speak_dialog('controller.light.zigbee')

    @intent_handler('lights.on.intent')
    def handle_controller_lights_on(self, message):
        self.send_command('{"state":"ON"}')
        #self.speak_dialog('controller.light.zigbee')

    @intent_handler('lights.off.intent')
    def handle_controller_lights_off(self, message):
        self.send_command('{"state":"OFF"}')
        #self.speak_dialog('controller.light.zigbee')

    @intent_handler('lights.percentage.intent')
    def handle_controller_lights_percentage(self, message):
        percentage = message.data.get('percentage')
        if percentage is not None:
            pct = int(percentage)
            pct = int(pct*255/100)
            self.send_command('{"state":"ON","transition":1,"brightness": '+str(pct)+'}')
            #self.speak("Setting brightness to " + str(pct) );


def create_skill():
    return ZigbeeLightController()

