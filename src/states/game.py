"""Main playing state (placeholder for now, filled in by later milestones)."""

import pygame

import config
from states.base import GameState


class GamePlayState(GameState):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition("menu")

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill(config.BLACK)

        text = self.font_medium.render("Bastion — game in progress (skeleton)", True, config.WHITE)
        self.screen.blit(text, text.get_rect(center=(self.w // 2, self.h // 2)))

        hint = self.font_small.render("ESC back to menu", True, config.GRAY)
        self.screen.blit(hint, hint.get_rect(center=(self.w // 2, self.h - 40)))
