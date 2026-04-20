import random

import pygame


GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
REGENERATION_INTERVAL_MS = 5000


def generate_color_grid() -> list[list[tuple[int, int, int]]]:
  return [
    [
      (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
      )
      for _ in range(GRID_SIZE)
    ]
    for _ in range(GRID_SIZE)
  ]


def draw_grid(surface: pygame.Surface, grid: list[list[tuple[int, int, int]]]) -> None:
  for row_index, row in enumerate(grid):
    for column_index, color in enumerate(row):
      pygame.draw.rect(
        surface,
        color,
        (column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE),
      )


def main() -> None:
  pygame.init()

  screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
  pygame.display.set_caption("Procedural Color Grid")

  clock = pygame.time.Clock()
  color_grid = generate_color_grid()
  last_regeneration_time = pygame.time.get_ticks()
  running = True

  while running:
    current_time = pygame.time.get_ticks()
    if current_time - last_regeneration_time >= REGENERATION_INTERVAL_MS:
      color_grid = generate_color_grid()
      last_regeneration_time = current_time

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))
    draw_grid(screen, color_grid)
    pygame.display.flip()
    clock.tick(60)

  pygame.quit()


if __name__ == "__main__":
  main()