from kivy.app import App
from kivy.lang import Builder


import model

game = model.Game()


class Controller(object):
    """Klasse Controller."""

    def __init__(self, game):
        self.game = game

    def toggle_factor(self, factor):
        return self.game.toggle_factor(factor)

    def toggle_level(self, l):
        return self.game.toggle_level(l)

    def get_solution(self):
        return self.game.get_solution()

    def restart(self):
        return self.game.restart()



class TermeApp(App):
    """Dies ist die Main Class, in der die App erstellt wird."""
    controller = Controller(game)

    def build(self):
        """Erstellt die APP."""
        presentation = Builder.load_file("terme.kv")  # darf erst hier geladen werden, da sonst die App erstellt wird
        # nachdem builder geladen wird
        return presentation
