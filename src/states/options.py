"""Options state (placeholder — real options will be added later)."""

import pygame

import config
from ui import Button
from states.base import GameState


class OptionsState(GameState):
    def __init__(self, game):
        super().__init__(game)
        s = max(1.0, self.h / 600)
        self.back_button = Button((self.w // 2, int(self.h * 0.85)), int(220 * s), int(56 * s),
                                  "Back", self.font_medium, base_color=config.GREEN)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition("menu")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.back_button.is_clicked(event):
                self.transition("menu")

    def draw(self):
        self.screen.fill(config.BLACK)

        title = self.font_large.render("OPTIONS", True, config.WHITE)
        self.screen.blit(title, title.get_rect(center=(self.w // 2, int(self.h * 0.20))))

        note = self.font_small.render("Settings coming soon…", True, config.GRAY)
        self.screen.blit(note, note.get_rect(center=(self.w // 2, self.h // 2)))

        self.back_button.draw(self.screen)
