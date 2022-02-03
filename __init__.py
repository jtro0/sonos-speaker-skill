from mycroft import MycroftSkill, intent_file_handler


class SonosSpeaker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('speaker.sonos.intent')
    def handle_speaker_sonos(self, message):
        self.speak_dialog('speaker.sonos')


def create_skill():
    return SonosSpeaker()

