import pygame, sys
from pygame.locals import *
import random

def draw_grid(n):
    """Draw a pygame grid of size 2^n by 2^n.

    Precondition: n >= 1

    @type n: int
    @rtype: None
    """
    # Initialize a pygame screen filled in black.
    pygame.init()
    screen = pygame.display.set_mode((2**n * 2, 2**n * 2))
    screen.fill(black)

    # Draw white gridlines in the screen.
    for i in range(2 ** n):
        for j in range(2 ** n):
            rect = (i * 2, j * 2,
                    # UPDATE: Last two coordinates are *width and height*
                    # http://www.pygame.org/docs/ref/rect.html
                    # (i + 1) * SQUARE_SIZE, (j + 1) * SQUARE_SIZE)
                    2, 2)
            pygame.draw.rect(screen, WHITE, rect, 1)

    # Uncomment the following part after you've implemented tile_with_dominoes
    # tiling = tile_with_dominoes(n)
    # for domino in tiling:
    #     domino.draw(screen)

    # Display the screen to the user.
    pygame.display.flip()


class Domino:
    """A domino on a grid.

    === Attributes ===
    @type position: list[(int, int)]
        The location of the domino on the grid.
    @type colour: (int, int, int)
        The colour of the domino, representing in RGB colour form.

    === Representation invariants ===
    - len(position) == 2
    - position's two tuples are adjacent squares on the grid
      For a 2^n by 2^n grid, each tuple's (x, y) coordinates should both be
      between 0 and 2^n - 1, inclusive.

      The position should *not* depend on SQUARE_SIZE - this constant is only
      used when drawing the domino using pygame.

      **IMPORTANT!!!**
      In pygame, the origin (0, 0) position is located at the *top-left* corner
      of the window. Increasing the y coordinate moves *down* the grid.

    - each number in colour is between 0 and 255, inclusive

    """
    def __init__(self, square1, square2):
        """Initialize a new domino with the given two squares.

        Pick a random colour for the domino.

        Precondition: square1 and square2 are adjacent

        @type self: Domino
        @type square1: (int, int)
        @type square2: (int, int)
        @rtype: None
        """
        self.position = [square1, square2]

        self.colour = (random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))

    def add_offset(self, x_offset, y_offset):
        """Add the given offset to each square in this domino.

        @type self: Domino
        @type x_offset: int
        @type y_offset: int
        @rtype: None
        """
        for i in range(len(self.position)):
            old_x, old_y = self.position[i]
            self.position[i] = (old_x + x_offset, old_y + y_offset)

    def draw(self, screen):
        """Draw this domino onto the given screen.
        """
        x_coords = [self.position[0][0], self.position[1][0]]
        y_coords = [self.position[0][1], self.position[1][1]]

        pygame.draw.rect(screen, self.colour,
                         (min(x_coords) * 2,
                          min(y_coords) * 2,
                          (max(x_coords) - min(x_coords) + 1) * 2,
                          (max(y_coords) - min(y_coords) + 1) * 2))


# TODO: implement this function!
def tile_with_dominoes(n):
    """Return a random tiling of a 2^n by 2^n grid by dominoes.

    Remember that you should be returning a list of dominoes here.
    Think recursively! Mentally divide up the 2^n by 2^n grid
    into four quadrants, each of size 2^(n-1).

    Precondition: n >= 1.

    **IMPORTANT!!!**
    In pygame, the origin (0, 0) position is located at the *top-left* corner
    of the window. Increasing the y coordinate moves *down* the grid.

    @type n: int
    @rtype: list[Domino]
    """
    if n == 1:
        return _tile_2_by_2()
    else:
        # TODO (1)
        # Compute four different tilings of a 2^(n-1) by 2^(n-1) grid,
        # for the four different quadrants.
        upper_left_tiling = []
        upper_right_tiling = []
        lower_left_tiling = []
        lower_right_tiling = []

        # TODO (2)
        # Each tiling will have square coordinates between 0 and 2^(n-1),
        # but these coordinates are only good for the *upper-left* quadrant.
        # Add an offset to the upper-right, lower-left, and lower-right tilings
        # so that the dominoes are placed in the correct quadrant.
        #
        # Remember that the positions here do *not* depend on SQUARE_SIZE.

        # TODO (3)
        # Return the combined tiling for all four quadrants.


def _tile_2_by_2():
    """Return a random tiling of a 2 by 2 grid.

    Randomly choose between tiling the grid vertically or horizontally.

    @rtype: list[Domino]
    """
    # Remember that the positions here do *not* depend on SQUARE_SIZE.
    pass


def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,blue,(200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()