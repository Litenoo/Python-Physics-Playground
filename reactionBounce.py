import pygame
import time

from typing import List

pygame.init()


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Square:
    def __init__(
        self, id: int, size: int, coords: Vector2D, vel: Vector2D, acc: Vector2D, color
    ):
        self.size = size
        self.id = id
        self.coords = coords
        self.vel = vel
        self.acc = acc
        self.color = color
        self.bound = False

    def tick(self):
        if self.coords.y < 380 or self.bounce == True:
            self.bounce = False
            self.vel.y += self.acc.y
            self.coords.y += self.vel.y
            if self.coords.y > 380:
                self.bounce = True
                self.coords.y = 380
                self.vel.y = self.vel.y * -0.6

        self.vel.x += self.acc.x
        self.coords.x += self.vel.x

    def info(self):
        print(f"Id: {self.id}")
        print(f"Coords: {self.coords.x, self.coords.y}")
        print(f"Velocity: {self.vel.x, self.vel.y}")
        print(f"Acceleration: {self.acc.x, self.acc.y}")


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simulation")

g: float = 9.81 * (1 / 60)

objects: List[Square] = []

objects.append(
    Square(0, 20, Vector2D(40, 40), Vector2D(0, 0), Vector2D(0, g), (0, 255, 0))
)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for i, object in enumerate(objects):
        print("__________________")
        objects[i].tick()
        objects[i].info()
        pygame.draw.rect(
            screen,
            objects[i].color,
            (
                (objects[i].coords.x, objects[i].coords.y),
                (objects[i].size, objects[i].size),
            ),
        )
        pygame.display.flip()
    time.sleep(1 / 60)

pygame.quit()
