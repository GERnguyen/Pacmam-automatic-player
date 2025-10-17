import os

import pygame
import sys

from constants import FPS, WIDTH, HEIGHT, BLUE, BLACK, WALL, FOOD, WHITE, YELLOW, MONSTER, IMAGE_GHOST, \
    IMAGE_PACMAN, ALGORITHMS

clock = pygame.time.Clock()
bg = pygame.image.load("images/home_bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.init()
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
font_path = os.path.join(parent_dir, 'Fonts', 'MontserratRegular-BWBEl.ttf')
font = pygame.font.Font(font_path, 35)
my_font = pygame.font.Font(font_path, 60)

_N = _M = 0
__map = 0
SIZE_WALL = 20


class Button:
    def __init__(self, x, y, width, height, screen, buttonText="Button", onClickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onClickFunction = onClickFunction
        self.screen = screen

        self.fillColors = {
            'normal': pygame.Color('#777777'),
            'hover': pygame.Color("#ffffff"),
            'pressed': pygame.Color('#ffffff'),
        }

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (255, 255, 255))

        self.is_pressed = False


    def process(self):
        is_hover = False
        mousePos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        color = self.fillColors['normal']

        if self.buttonRect.collidepoint(mousePos):
            color = self.fillColors['hover']
            is_hover = True
            if mouse_pressed:
                color = self.fillColors['pressed']
                if not self.is_pressed: 
                    self.is_pressed = True
                    if self.onClickFunction:
                        self.onClickFunction()
            else:
                self.is_pressed = False
        else:
            self.is_pressed = False

        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonRect, border_radius=20)

        pygame.draw.rect(self.screen, color, self.buttonRect, width=5, border_radius=20)

        text_rect = self.buttonSurf.get_rect(center=self.buttonRect.center)
        self.screen.blit(self.buttonSurf, text_rect)
        return is_hover


class Menu:
    def __init__(self, screen):
        self.current_level = 0
        self.clicked = False
        self.map_name = []
        self.current_map = 0
        self.current_algo = (0, 0)
        self.done = False
        self.current_screen = 1
        self.screen = screen
        self.level_details = -1
        self.btnStart = Button(WIDTH // 2 - 100 + 5, HEIGHT - 170, 200, 100, screen, "Start", self.myFunction)

        self.btnLevel1 = Button(150, HEIGHT // 4 * 0 + 20, 250, 100, screen, "Level 1",
                                self._load_map_level_1)
        self.btnLevel2 = Button(150, HEIGHT // 4 * 1 + 20, 250, 100, screen, "Level 2",
                                self._load_map_level_2)
        self.btnLevel3 = Button(150, HEIGHT // 4 * 2 + 20, 250, 100, screen, "Level 3",
                                self._load_map_level_3)
        self.btnLevel4 = Button(150, HEIGHT // 4 * 3 + 20, 250, 100, screen, "Level 4",
                                self._load_map_level_4)

        self.btnLevel = [self.btnLevel1, self.btnLevel2, self.btnLevel3, self.btnLevel4]

        self.btnPrev = Button(WIDTH // 2 - 540, HEIGHT // 2 - 50, 100, 100, screen, "<", self.prevMap)
        self.btnNext = Button(WIDTH // 2 + 440, HEIGHT // 2 - 50, 100, 100, screen, ">", self.nextMap)
        self.btnPrev_algo = Button(WIDTH // 2 - 220, HEIGHT // 4 * 3 + 35, 100, 100, screen, "<", self.prevAlgo)
        self.btnNext_algo = Button(WIDTH // 2 + 120, HEIGHT // 4 * 3 + 35, 100, 100, screen, ">", self.nextAlgo)
        self.btnPlay = Button(WIDTH - 180, HEIGHT // 4 * 3 + 35, 150, 100, screen, "PLAY", self.selectMap)

        self.btnBack = Button(40, HEIGHT // 4 * 3 + 35, 150, 100, screen, "BACK", self.myFunction)
        

    def nextMap(self):
        if self.clicked:
            self.current_screen = 3
            self.current_map = (self.current_map + 1) % len(self.map_name)
        self.clicked = False

    def prevMap(self):
        if self.clicked:
            self.current_screen = 3
            self.current_map -= 1
            if self.current_map < 0:
                self.current_map += len(self.map_name)
        self.clicked = False

    def nextAlgo(self):
        if self.clicked:
            self.current_screen = 3
            self.current_algo = ((self.current_level - 1), (self.current_algo[1] + 1) % len(ALGORITHMS[self.current_level - 1]))
        self.clicked = False
    
    def prevAlgo(self):
        if self.clicked:
            self.current_screen = 3
            self.current_algo = ((self.current_level - 1), (self.current_algo[1] - 1))
            if self.current_algo[1] < 0:
                self.current_algo = (self.current_level - 1, self.current_algo[1] + len(ALGORITHMS[self.current_level - 1]))
        self.clicked = False

    def myFunction(self):
        self.current_screen = 2
        self.map_name = []
        self.current_map = 0
        self.current_level = 0

    def _load_map_level_1(self):
        if self.clicked:
            self.current_level = 1
            for file in os.listdir('../Input/Level1'):
                self.map_name.append('../Input/Level1/' + file)
            self.current_screen = 3
            self.current_algo = (0, 0)
        self.clicked = False

    def _load_map_level_2(self):
        if self.clicked:
            self.current_level = 2
            for file in os.listdir('../Input/Level2'):
                self.map_name.append('../Input/Level2/' + file)
            self.current_screen = 3
            self.current_algo = (1, 0)
        self.clicked = False

    def _load_map_level_3(self):
        if self.clicked:
            self.current_level = 3
            for file in os.listdir('../Input/Level3'):
                self.map_name.append('../Input/Level3/' + file)
            self.current_screen = 3
            self.current_algo = (2, 0)
        self.clicked = False

    def _load_map_level_4(self):
        if self.clicked:
            self.current_level = 4
            for file in os.listdir('../Input/Level4'):
                self.map_name.append('../Input/Level4/' + file)
            self.current_screen = 3
            self.current_algo = (3, 0)
        self.clicked = False


    def drawDetails(self, level):
        detailsImgs = [
            'images/level1.png',
            'images/level2.png',
            'images/level3.png',
            'images/level4.png',
        ]
        detailsImg = detailsImgs[level - 1]
        image = pygame.image.load(detailsImg).convert_alpha()
        image = pygame.transform.scale(image, (550, 370))
        self.screen.blit(image, (WIDTH // 2 - 80, 120))

    def draw_map(self, fileName):
        text_surface = my_font.render(
            'LEVEL {level} - MAP {map}'.format(level=self.current_level, map=self.current_map + 1), False, WHITE)
        self.screen.blit(text_surface, (WIDTH // 2 - 270, 0))

        f = open(fileName, "r")
        x = f.readline().split()
        count_ghost = 0
        N, M = int(x[0]), int(x[1])

        MARGIN_TOP = 100
        MARGIN_LEFT = (WIDTH - M * SIZE_WALL) // 2

        for i in range(N):
            line = f.readline().split()
            for j in range(M):
                cell = int(line[j])
                if cell == WALL:
                    image = pygame.Surface([SIZE_WALL, SIZE_WALL])
                    image.fill((242, 242, 242))
                    pygame.draw.rect(image, BLUE, (0, 0, SIZE_WALL, SIZE_WALL), 1)
                    top = i * SIZE_WALL + MARGIN_TOP
                    left = j * SIZE_WALL + MARGIN_LEFT
                    self.screen.blit(image, (left, top))
                elif cell == FOOD:
                    image = pygame.Surface([SIZE_WALL // 2, SIZE_WALL // 2])
                    image.fill(WHITE)
                    image.set_colorkey(WHITE)
                    pygame.draw.ellipse(image, YELLOW, [0, 0, SIZE_WALL // 2, SIZE_WALL // 2])

                    top = i * SIZE_WALL + MARGIN_TOP + SIZE_WALL // 2 - SIZE_WALL // 4
                    left = j * SIZE_WALL + MARGIN_LEFT + SIZE_WALL // 2 - SIZE_WALL // 4
                    self.screen.blit(image, (left, top))
                elif cell == MONSTER:
                    image = pygame.image.load(IMAGE_GHOST[count_ghost]).convert_alpha()
                    image = pygame.transform.scale(image, (SIZE_WALL, SIZE_WALL))
                    top = i * SIZE_WALL + MARGIN_TOP
                    left = j * SIZE_WALL + MARGIN_LEFT
                    count_ghost = (count_ghost + 1) % len(IMAGE_GHOST)
                    self.screen.blit(image, (left, top))

        x = f.readline().split()
        image = pygame.image.load(IMAGE_PACMAN[0]).convert_alpha()
        image = pygame.transform.scale(image, (SIZE_WALL, SIZE_WALL))
        top = int(x[0]) * SIZE_WALL + MARGIN_TOP
        left = int(x[1]) * SIZE_WALL + MARGIN_LEFT
        self.screen.blit(image, (left, top))

        f.close()

    def selectMap(self):
        if self.clicked:
            self.done = True

    def run(self):

        while not self.done:
            self.clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True

            if self.current_screen == 1:
                self.screen.blit(bg, (0, 0))
                _ = self.btnStart.process()

            elif self.current_screen == 2:
                self.screen.fill(BLACK)
                is_hoverd = False
                detailsRect = pygame.Rect(WIDTH // 2 - 100, 100, 600, 400)
                pygame.draw.rect(self.screen, (255, 255, 255), detailsRect, width=5, border_radius=20)
                textSurf = font.render("Level Details", True, WHITE)
                self.screen.blit(textSurf, (WIDTH // 2 + 80, 40))
                for i in range(4):
                    _ = self.btnLevel[i].process()
                    if _:
                        self.level_details = i + 1
                        is_hoverd = True
                if is_hoverd:
                    self.drawDetails(self.level_details)

            elif self.current_screen == 3:
                self.screen.fill(BLACK)
                self.current_screen = 4
                self.draw_map(self.map_name[self.current_map])

            elif self.current_screen == 4:
                 self.btnNext.process()
                 self.btnPrev.process()
                 algo_name = ALGORITHMS[self.current_algo[0]][self.current_algo[1]] if self.current_algo else ""
                 words = algo_name.split()
                 if len(words) == 2:
                     surface1 = font.render(words[0], True, WHITE)
                     surface2 = font.render(words[1], True, WHITE)
                     x1 = WIDTH // 2 - surface1.get_width() // 2
                     x2 = WIDTH // 2 - surface2.get_width() // 2
                     y1 = HEIGHT // 4 * 3 + 38
                     y2 = y1 + surface1.get_height() + 5
                     self.screen.blit(surface1, (x1, y1))
                     self.screen.blit(surface2, (x2, y2))
                 else:
                     algo_text_surface = font.render(algo_name, True, WHITE)
                     algo_text_x = WIDTH // 2 - algo_text_surface.get_width() // 2
                     algo_text_y = HEIGHT // 4 * 3 + 60
                     self.screen.blit(algo_text_surface, (algo_text_x, algo_text_y))
                 self.btnPrev_algo.process()
                 self.btnNext_algo.process()
                 self.btnPlay.process()
                 self.btnBack.process()


            pygame.display.flip()
            clock.tick(FPS)

        return [self.current_level, self.map_name[self.current_map], self.current_algo]
