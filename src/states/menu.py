"""Main menu state."""

import pygame

import config
from ui import Button
from states.base import GameState


class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        # Scale the menu layout with the screen (base layout assumes 600 px tall)
        s = max(1.0, self.h / 600)
        cx = self.w // 2

        btn_w, btn_h = max(280, int(300 * s)), int(56 * s)
        step = int(90 * s)  # generous distance between buttons
        first_center_y = int(self.h * 0.48)

        self.buttons = {
            "start": Button((cx, first_center_y), btn_w, btn_h, "Start Game", self.font_medium,
                            base_color=config.GREEN),
            "options": Button((cx, first_center_y + step), btn_w, btn_h, "Options", self.font_medium),
            "quit": Button((cx, first_center_y + 2 * step), btn_w, btn_h, "Quit", self.font_medium,
                           base_color=config.RED),
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.transition("game")
            elif event.key == pygame.K_ESCAPE:
                self.game.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for name, button in self.buttons.items():
                if button.is_clicked(event):
                    if name == "start":
                        self.transition("game")
                    elif name == "options":
                        self.transition("options")
                    elif name == "quit":
                        self.game.running = False
                    break  # one click activates at most one button

    def draw(self):
        self.screen.fill(config.BLACK)

        cx, cy = self.w // 2, self.h // 2

        # Title block in the upper part of the screen, clearly above the buttons
        title = self.font_large.render("BASTION", True, config.WHITE)
        self.screen.blit(title, title.get_rect(center=(cx, int(self.h * 0.20))))

        subtitle = self.font_small.render("a tower defense game", True, config.GRAY)
        self.screen.blit(subtitle, subtitle.get_rect(center=(cx, int(self.h * 0.20) + int(self.h * 0.08))))

        for button in self.buttons.values():
            button.draw(self.screen)
