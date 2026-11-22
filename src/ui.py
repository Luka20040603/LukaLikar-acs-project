"""Simple reusable UI widgets (menu buttons for now)."""

import pygame

import config


class Button:
    """A rectangular text button with a hover highlight.

    Positions are given as the button *center* so layouts work in fullscreen.
    """

    def __init__(self, center, width, height, text, font,
                 base_color=config.GRAY, hover_color=config.BLUE, text_color=config.WHITE):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.label = self.font.render(self.text, True, self.text_color)
        self.label_rect = self.label.get_rect(center=self.rect.center)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos))

    def draw(self, screen):
        color = self.hover_color if self.is_hovered() else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, config.WHITE, self.rect, width=2, border_radius=8)
        self.label_rect.center = self.rect.center
        screen.blit(self.label, self.label_rect)
