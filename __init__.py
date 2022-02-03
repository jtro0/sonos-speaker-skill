from mycroft import MycroftSkill, intent_file_handler


class SonosSpeaker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event('speak', self.handle_speaker_sonos)

    @intent_file_handler('speaker.sonos.intent')
    def handle_speaker_sonos(self, message):
        # self.speak_dialog('speaker.sonos')
        self.log.info("start")
        self.log.info(message.utterance)
        self.log.info("stop")


def create_skill():
    return SonosSpeaker()

