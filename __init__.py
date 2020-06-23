from mycroft import MycroftSkill, intent_file_handler


class ZigbeeLightController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.light.zigbee.intent')
    def handle_controller_light_zigbee(self, message):
        self.speak_dialog('controller.light.zigbee')


def create_skill():
    return ZigbeeLightController()

