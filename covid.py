import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Pick size of window
SIZE = (800, 600)

# Initialize the window
window = pygame.display.set_mode(SIZE)

# Control the frame rate
FPS = 30
clock = pygame.time.Clock()

# Object oriented
class Person:
    def __init__(self, x, y, infected=False):
        self.infected = infected
        self.rect = pygame.Rect(x, y, 10, 10)

    def dist(self, other_person):
        delta_x = self.rect.x - other_person.rect.x
        delta_y = self.rect.y - other_person.rect.y
        distance = (delta_x**2 + delta_y**2)**(1/2)
        return distance

    def draw(self):
        if self.infected:
            colour = pygame.Color("Red")
        else:
            colour = pygame.Color("Green")

        pygame.draw.rect(window, colour, self.rect)

    def move(self):
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)

        # Bounds within window
        self.rect.left = max(self.rect.left, 0)
        self.rect.top = max(self.rect.top, 0)

        self.rect.right = min(self.rect.right, SIZE[0])
        self.rect.bottom = min(self.rect.bottom, SIZE[1])

persons = []
for i in range(100):
    persons.append(Person(random.randint(100, 500), random.randint(100, 500)))

persons.append(Person(x=400, y=400, infected=True))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Refresh the screen
    window.fill(pygame.Color("Black"))

    for person in persons:
        # Move people
        person.move()

        # Infect people
        if person.infected:
            for other_person in persons:
                if other_person == person:
                    continue
                if person.dist(other_person) < 40:
                    other_person.infected = True

        # Draw people
        person.draw()

    # Update the screen
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)
