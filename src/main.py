"""Entry point: creates the window, runs the loop, dispatches to the current state."""

import os
import sys

import pygame

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
from states.menu import MenuState  # noqa: E402
from states.game import GamePlayState  # noqa: E402
from states.options import OptionsState  # noqa: E402


class Game:
    def __init__(self):
        pygame.init()
        flags = pygame.FULLSCREEN if config.FULLSCREEN else 0
        # In fullscreen use the real monitor resolution so the game is crisp,
        # not a stretched 960x600 surface.
        if flags & pygame.FULLSCREEN:
            info = pygame.display.Info()
            win_w, win_h = info.current_w, info.current_h
        else:
            win_w, win_h = config.WIDTH, config.HEIGHT
        self.screen = pygame.display.set_mode((win_w, win_h), flags)
        # With FULLSCREEN, use the real monitor resolution for all layout math.
        self.w, self.h = self.screen.get_size()
        pygame.display.set_caption(config.TITLE)
        self.clock = pygame.time.Clock()
        # Scale UI/fonts proportionally to the screen height (base: 1080p).
        self.scale = max(0.8, self.h / 1080)
        self.font_small = pygame.font.SysFont("consolas", max(14, round(config.FONT_SMALL * self.scale)))
        self.font_medium = pygame.font.SysFont("consolas", round(config.FONT_MEDIUM * self.scale))
        self.font_large = pygame.font.SysFont("consolas", round(config.FONT_LARGE * self.scale))

        self.states = {
            "menu": MenuState,
            "options": OptionsState,
            "game": GamePlayState,
        }
        self.current_state = None
        self.running = True
        self.change_state("menu")

    def change_state(self, name):
        # Drop-in point for a persistent audio manager and other resets (later milestone)
        self.current_state = self.states[name](self)

    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000.0  # seconds, capped at FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.current_state.handle_event(event)
            self.current_state.update(dt)
            self.current_state.draw()
            pygame.display.flip()
        pygame.quit()


def main():
    Game().run()


if __name__ == "__main__":
    main()
