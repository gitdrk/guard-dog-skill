from mycroft import MycroftSkill, intent_file_handler


class GuardDog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dog.guard.intent')
    def handle_dog_guard(self, message):
        self.speak_dialog('dog.guard')


def create_skill():
    return GuardDog()

