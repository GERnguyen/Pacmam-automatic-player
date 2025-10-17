import pygame

from constants import SIZE_WALL, MARGIN


class Player:
    def __init__(self, row, col, fileImage):
        self.image = pygame.image.load(fileImage).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_WALL, SIZE_WALL))

        self.rect = self.image.get_rect()
        self.rect.top = row * SIZE_WALL + MARGIN["TOP"]
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"]
        self.row = row
        self.col = col
        self.path = []

    def change_state(self, rotate, fileImage):
        self.image = pygame.image.load(fileImage).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_WALL, SIZE_WALL))
        self.image = pygame.transform.rotate(self.image, rotate)

        self.rect = self.image.get_rect()
        self.rect.top = self.row * SIZE_WALL + MARGIN["TOP"]
        self.rect.left = self.col * SIZE_WALL + MARGIN["LEFT"]

    def draw(self, screen, level=None, is_Pacman= False):
        screen.blit(self.image, (self.rect.left, self.rect.top))
        if len(self.path) > 2:
            points = []
            for r, c in self.path:
                x = c * SIZE_WALL + MARGIN["LEFT"] + SIZE_WALL // 2
                y = r * SIZE_WALL + MARGIN["TOP"] + SIZE_WALL // 2
                points.append((int(x), int(y)))
            if len(points) > 0:
                points.pop(0)
 
            if len(points) >= 2 and level != 3:
                overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
                glow_strokes = [ (12, 30), (8, 90), (4, 220) ] 
                for width, alpha in glow_strokes:
                    color = (255, 255, 255, alpha)
                    pygame.draw.lines(overlay, color, False, points, width)
                pygame.draw.lines(overlay, (255,255,255,255), False, points, 2)
                screen.blit(overlay, (0, 0))

        if level == 3 and is_Pacman:
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            cx = self.col * SIZE_WALL + MARGIN['LEFT'] + SIZE_WALL // 2
            cy = self.row * SIZE_WALL + MARGIN['TOP'] + SIZE_WALL // 2
            radius = 3 * SIZE_WALL
            glow_strokes = [(24, 30), (16, 90), (8, 200)]
            for width, alpha in glow_strokes:
                color = (255, 255, 255, alpha)
                pygame.draw.circle(overlay, color, (int(cx), int(cy)), radius, width)
            pygame.draw.circle(overlay, (255, 255, 255, 255), (int(cx), int(cy)), radius, 2)
            screen.blit(overlay, (0, 0))
            
        

    def getRC(self):
        return [self.row, self.col]

    def setRC(self, row, col):
        self.row = row
        self.col = col
        self.rect.top = row * SIZE_WALL + MARGIN["TOP"]
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"]

    def move(self, d_R, d_C):
        self.rect.top += d_R
        self.rect.left += d_C

    def touch_New_RC(self, row, col):
        return self.rect.top == row * SIZE_WALL and self.rect.left == col * SIZE_WALL
