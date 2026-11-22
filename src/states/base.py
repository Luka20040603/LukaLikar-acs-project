"""Base class shared by all game states."""


class GameState:
    """A state receives the game, then handles events, updates and draws.

    Existing states: "menu", "options", "game" ("gameover" planned).
    """

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.w = game.w
        self.h = game.h
        self.font_small = game.font_small
        self.font_medium = game.font_medium
        self.font_large = game.font_large

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def transition(self, name):
        self.game.change_state(name)
