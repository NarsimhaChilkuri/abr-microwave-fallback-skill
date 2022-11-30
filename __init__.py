from mycroft import MycroftSkill, intent_file_handler


class AbrMicrowaveFallback(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fallback.microwave.abr.intent')
    def handle_fallback_microwave_abr(self, message):
        self.speak_dialog('fallback.microwave.abr')


def create_skill():
    return AbrMicrowaveFallback()

