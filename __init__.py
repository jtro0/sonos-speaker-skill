from mycroft import MycroftSkill, intent_file_handler
import urllib.parse
import requests

class SonosSpeaker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.domain = self.settings.get('domain')
        self.port = self.settings.get('port')
        self.speak_api = '/api/speakText'

        self.add_event('speak', self.handle_speaker_sonos)

        self.get_household_url = '/api/households'
        self.get_devices_url = '/api/clipCapableSpeakers'

        self.get_device()

    def get_device(self):
        households = requests.get(f'{self.domain}:{self.port}{self.get_household_url}')
        if households.json().get('success') and len(households.json().get('households')) == 1:
            self.household_id = households.json().get('households')[0].get('id')

        devices = requests.get(f'{self.domain}:{self.port}{self.get_devices_url}', params={'household':self.household_id})
        if devices.json().get('success') and len(devices.json().get('players')) == 1:
            self.device_id = devices.json().get('players')[0].get('id')


    @intent_file_handler('speaker.sonos.intent')
    def handle_speaker_sonos(self, message):
        # self.speak_dialog('speaker.sonos')
        self.log.info('what to say: ' + message.data.get('utterance'))
        encoded = urllib.parse.quote(message.data.get('utterance'))



def create_skill():
    return SonosSpeaker()

