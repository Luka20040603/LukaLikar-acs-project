"""Headless smoke test for the game skeleton.

Runs the real game loop with a dummy video driver for a short time,
checks menu -> game -> menu transitions, then exits cleanly.

Run: python tests/test_skeleton.py   (from the repo root)
"""

import os
import sys

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import pygame
from main import Game


def frame(game):
    for event in pygame.event.get():
        if event.type != pygame.QUIT:
            game.current_state.handle_event(event)
    game.current_state.update(1 / 60)
    game.current_state.draw()
    pygame.display.flip()


def main():
    game = Game()
    assert type(game.current_state).__name__ == "MenuState"

    # A few menu frames
    for _ in range(10):
        frame(game)

    # Start with ENTER (exactly like a key press), delivered in the next frame
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    frame(game)
    assert type(game.current_state).__name__ == "GamePlayState"

    for _ in range(10):
        frame(game)

    # Back to menu with ESC
    game.current_state.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    assert type(game.current_state).__name__ == "MenuState"

    # Menu -> Options via the real Options button
    options_button = game.current_state.buttons["options"]
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=options_button.rect.center)
    game.current_state.handle_event(click)
    assert type(game.current_state).__name__ == "OptionsState"

    # Options -> Menu via the real Back button
    back = game.current_state.back_button
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=back.rect.center)
    game.current_state.handle_event(click)
    assert type(game.current_state).__name__ == "MenuState"

    # Start button also works
    start = game.current_state.buttons["start"]
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=start.rect.center)
    game.current_state.handle_event(click)
    assert type(game.current_state).__name__ == "GamePlayState"

    game.running = False
    pygame.quit()
    print("OK: skeleton smoke test passed (menu/options/game transitions, buttons, loop, drawing)")


if __name__ == "__main__":
    main()
