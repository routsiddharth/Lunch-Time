import pygame, random, math, time
from pygame import mixer

pygame.init()

mixer.init()
mixer.music.load("Music/music.mp3")
mixer.music.set_volume(0.7)

frame = 0
MAX_FPS = 30
clock = pygame.time.Clock()
pygame.display.set_caption('Lunch Time - A Game by Siddharth Rout')

WIDTH, HEIGHT = 900, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 102, 0, 255)
LIME = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
YELLOW = (255, 255, 0, 255)

FONT_S = pygame.font.SysFont('comicsans', 40)
FONT_M = pygame.font.SysFont('comicsans', 60)
FONT_L = pygame.font.SysFont('comicsans', 100)

PIZZA = pygame.transform.scale(pygame.image.load("Skins/pizza.png"), (80, 80))
BURGER = pygame.transform.scale(pygame.image.load("Skins/burger.png"), (60, 60))
BURRITO = pygame.transform.scale(pygame.image.load("Skins/burrito.png"), (70, 70))

TITLE = pygame.transform.scale(pygame.image.load("Backgrounds/LUNCHtime.png"), (900, 100))

CHOC = pygame.transform.scale(pygame.image.load("Food/chocolate.png"), (100, 100))
PINE = pygame.transform.scale(pygame.image.load("Food/pineapple.png"), (100, 100))
CHILI = pygame.transform.scale(pygame.image.load("Food/chili.png"), (100, 100))
CHEESE = pygame.transform.scale(pygame.image.load("Food/cheese.png"), (100, 80))

X2 = pygame.transform.scale(pygame.image.load("PowerUps/x2.png"), (100, 100))

skins = [[PIZZA], [BURGER], [BURRITO]]

backgrounds = []
background = 0

for i in range(7):
    BKGR = pygame.transform.scale(pygame.image.load(f"Backgrounds/bg_{i}.png"), (900, 900))
    backgrounds.append(BKGR)

for i in range(len(skins)):
    skin = skins[i][0]

    t = FONT_L.render("EQUIP", 1, BLACK)

    xpos = 120
    width = t.get_width() + 20
    height = t.get_height() + 20
    ypos = (t.get_height() + 80) + (i * (height + 20))

    price = i * 75

    extend = [False, (xpos, ypos), (width, height), price, i]
    extend[0] = True if i == 0 else False
    skins[i].extend(extend)

menu_buttons = []

t = FONT_L.render("PLAY", 1, WHITE)

width = t.get_width() + 20
height = t.get_height() + 20
xpos = (WIDTH / 2) - (t.get_width() / 2) - 10
ypos = 400

x = xpos + 10
y = ypos + 10

menu_buttons.append([(xpos, ypos, width, height), t, (x, y), "game"])

t = FONT_L.render("SHOP", 1, WHITE)

width = t.get_width() + 20
height = t.get_height() + 20
xpos = (WIDTH / 2) - (t.get_width() / 2) - 10
ypos = 500

x = xpos + 10
y = ypos + 10

menu_buttons.append([(xpos, ypos, width, height), t, (x, y), "shop"])

t = FONT_L.render("HOW TO PLAY", 1, WHITE)

width = t.get_width() + 20
height = t.get_height() + 20
xpos = (WIDTH / 2) - (t.get_width() / 2) - 10
ypos = 600

x = xpos + 10
y = ypos + 10

menu_buttons.append([(xpos, ypos, width, height), t, (x, y), "howto"])


class Player:

    def __init__(self):

        self.skin = 0
        self.img = skins[self.skin][0]

        self.height = self.img.get_height()
        self.width = self.img.get_width()
        self.player_x = (WIDTH / 2) - (self.img.get_width() / 2)
        self.player_y = (HEIGHT / 2) - (self.img.get_height() / 2)

        self.top = self.player_y
        self.bottom = self.player_y + self.img.get_height()
        self.left = self.player_x
        self.right = self.player_x + self.img.get_width()

        self.speed = round((self.height / 50) * 3, 1)

        self.max = 150
        self.min = 50

        self.shields = 0

        self.boost_timer = 0

    def reset(self):

        self.player_x = (WIDTH / 2) - (self.img.get_width() / 2)
        self.player_y = (HEIGHT / 2) - (self.img.get_height() / 2)

        self.top = self.player_y
        self.bottom = self.player_y + self.img.get_height()
        self.left = self.player_x
        self.right = self.player_x + self.img.get_width()

        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.img = skins[self.skin][0]
        self.speed = round((self.height / 50) * 3, 1)

        self.boost_timer = 0

    def move_up(self):

        self.player_y -= self.speed
        self.top -= self.speed
        self.bottom -= self.speed

    def move_down(self):

        self.player_y += self.speed
        self.top += self.speed
        self.bottom += self.speed

    def move_left(self):

        self.player_x -= self.speed
        self.left -= self.speed
        self.right -= self.speed

    def move_right(self):

        self.player_x += self.speed
        self.left += self.speed
        self.right += self.speed

    def change_skin(self, new):

        self.skin = new
        self.img = skins[self.skin][0]

        self.update_vars()

    def enlarge(self):

        if (self.img.get_width() < self.max) and (self.img.get_height() < self.max):
            width = round(self.img.get_width() * 1.05)
            height = round(self.img.get_height() * 1.05)

            self.img = pygame.transform.scale(skins[self.skin][0], (width, height))

        self.update_vars()

    def shrink(self):

        if (self.img.get_width() > self.min) and (self.img.get_height() > self.min):
            width = round(self.img.get_width() * 0.95)
            height = round(self.img.get_height() * 0.95)

            self.img = pygame.transform.scale(skins[self.skin][0], (width, height))

        self.update_vars()

    def update_vars(self):

        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.top = self.player_y
        self.bottom = self.player_y + self.height
        self.left = self.player_x
        self.right = self.player_x + self.width

        self.speed = round((self.height / 50) * 3, 1)


class Obstacle:

    def __init__(self):

        good_imgs = [CHILI, CHEESE]
        bad_imgs = [CHOC, PINE]

        power_ups = [[X2, "x2"]]

        if random.randint(1, 100) == 29:

            self.good = None
            self.img, self.code = random.choice(power_ups)

        else:

            if random.randint(0, 1) == 0:

                self.good = True
                self.img = random.choice(good_imgs)

            else:

                self.good = False
                self.img = random.choice(bad_imgs)

        size = random.uniform(0.4, 0.8)
        self.img = pygame.transform.rotozoom(self.img, 0, size)

        min_y = 100
        max_y = HEIGHT - 250 - self.img.get_height()

        self.y = random.randint(min_y, max_y)

        self.speed = random.randint(3, 7)

        self.x = WIDTH + self.speed

        self.top = self.y
        self.bottom = self.y + self.img.get_height()
        self.left = self.x
        self.right = self.x + self.img.get_width()

        obstacles.append(self)

    def move(self):

        self.top = self.y
        self.bottom = self.y + self.img.get_height()
        self.left = self.x
        self.right = self.x + self.img.get_width()

        self.x = self.x - self.speed

        if self.x <= 0:
            obstacles.remove(self)

        window.blit(self.img, (self.x, self.y))


score = 0
currency = 0
wait_for_key = False
status = "menu"
running = True

player = Player()

obstacles = []


def draw():
    global window
    global status
    global player
    global obstacles
    global update_bkgr
    global bkgr_price
    global include_button

    window.fill(WHITE)

    if status == "game":

        power_ups()
        window.fill(WHITE)

        if score == 0:
            max_obs = 5
        else:
            max_obs = math.ceil(score / 15) * 5

        # Image and obstacle management

        if len(obstacles) <= max_obs:
            ob = Obstacle()

        window.blit(player.img, (player.player_x, player.player_y))

        for ob in obstacles:
            ob.move()

        t = FONT_L.render(str(score), 1, BLACK)
        xpos = 20
        ypos = 20

        window.blit(t, (xpos, ypos))

        if player.boost_timer > 0:
            boost_bar()

    elif status == "fin":

        t = FONT_L.render("GAME OVER", 1, BLACK)

        xpos = (WIDTH / 2) - (t.get_width() / 2)
        ypos = (HEIGHT / 2) - (t.get_height() / 2)

        window.blit(t, (xpos, ypos))

        text = FONT_S.render("Press any key to play continue.", 1, BLACK)

        xpos = (WIDTH / 2) - (text.get_width() / 2)
        ypos = ypos + t.get_height() + 10

        window.blit(text, (xpos, ypos))

    elif status == "shop":

        power_ups()

        text = FONT_L.render("BACK", 1, WHITE)

        pygame.draw.rect(window, BLACK, (20, 20, text.get_width() + 20, text.get_height() + 20))

        xpos = 30
        ypos = 30

        window.blit(text, (xpos, ypos))

        for item in skins:

            image, purchased, pos, dim, price, skin_id = item

            if player.skin == skin_id:
                pygame.draw.rect(window, BLUE, (pos[0], pos[1], dim[0], dim[1]))
            else:
                pygame.draw.rect(window, BLACK, (pos[0], pos[1], dim[0], dim[1]))

            if purchased == True:

                t = FONT_L.render("EQUIP", 1, WHITE)

            else:

                t = FONT_L.render(f"<{str(price)}>", 1, WHITE)

            xpos = (pos[0] + dim[0] / 2) - (t.get_width() / 2)
            ypos = pos[1] + 10

            window.blit(t, (xpos, ypos))

            xpos = (pos[0] / 2) - (image.get_width() / 2)
            ypos = pos[1] + ((dim[1] / 2) - (image.get_height() / 2))

            window.blit(image, (xpos, ypos))

        # Background Updating and Displaying

        if background == len(backgrounds) - 1:
            img = pygame.transform.scale(backgrounds[background], (300, 300))
        else:
            img = pygame.transform.scale(backgrounds[background + 1], (300, 300))

        xpos = (900 * 3) / 4 - (img.get_width() / 2)
        ypos = 250

        x = xpos - 10
        y = ypos - 10
        length = img.get_width() + 20
        height = img.get_height() + 20

        pygame.draw.rect(window, BLACK, (x, y, length, height))

        window.blit(img, (xpos, ypos))

        if not background == len(backgrounds) - 1:

            t = FONT_S.render(f"NEXT BACKGROUND", 1, BLACK)
            include_button = True

        else:

            t = FONT_S.render(f"MAX BACKGROUND {str(background + 1)}", 1, BLACK)
            include_button = False

        ypos = y - 20 - t.get_height()
        xpos = (900 * 3) / 4 - (t.get_width() / 2)

        window.blit(t, (xpos, ypos))

        if include_button:
            bkgr_price = (background + 1) * 100
            text = FONT_L.render(f"<{bkgr_price}>", 1, WHITE)

            y = y + height + 20
            x = (900 * 3) / 4 - (text.get_width() / 2) - 10
            width = text.get_width() + 20
            height = text.get_height() + 20
            update_bkgr = (x, y, width, height)

            pygame.draw.rect(window, BLACK, update_bkgr)

            window.blit(text, (x + 10, y + 10))

    elif status == "menu":

        window.blit(TITLE, (0, 200))

        for item in menu_buttons:
            rect_details, t, t_details, code = item

            pygame.draw.rect(window, BLACK, rect_details)
            window.blit(t, t_details)

    elif status == "review":

        t = FONT_L.render("REVIEW GAME", 1, BLACK)

        xpos = (WIDTH/2) - (t.get_width()/2)
        ypos = 40

        window.blit(t, (xpos, ypos))

        t = FONT_L.render(f"SCORE: {str(score)}", 1, BLACK)

        xpos = (WIDTH/2) - (t.get_width()/2)
        ypos = 80 + t.get_height()

        window.blit(t, (xpos, ypos))

        t = FONT_L.render(f"TIME: {time_passed}sec", 1, BLACK)

        xpos = (WIDTH/2) - (t.get_width()/2)
        ypos = 100 + (2 * t.get_height())

        window.blit(t, (xpos, ypos))

        t = FONT_L.render("PRESS KEY", 1, BLUE)

        xpos = (WIDTH/2) - (t.get_width()/2)
        ypos = HEIGHT - (20 + t.get_height())

        window.blit(t, (xpos, ypos))

    if status != "review":

        t = FONT_L.render(f"<{str(currency)}>", 1, BLACK)

        xpos = WIDTH - t.get_width() - 20
        ypos = 20

        window.blit(t, (xpos, ypos))

    pygame.display.update()

def power_ups():

    global powerups
    global window

    powerups = []

    # Shields

    radius = 50
    center = (40 + radius, HEIGHT - 30 - 2 * radius)

    pygame.draw.circle(window, BLACK, center, radius)

    powerups.append([center, radius, 50, "shields"])

    t = FONT_S.render("<50>", 1, WHITE)

    ypos = center[1] - (t.get_height()/2)
    xpos = center[0] - (t.get_width() /2)

    window.blit(t, (xpos, ypos))

    t = FONT_S.render("Shield", 1, BLACK)

    ypos = center[1] - radius - (10 + t.get_height())
    xpos = center[0] - t.get_width() / 2

    window.blit(t, (xpos, ypos))

    t = FONT_M.render("Owned: " + str(player.shields), 1, BLACK)

    xpos = center[0] + radius + 20
    ypos = center[1] - t.get_height() / 2

    window.blit(t, (xpos, ypos))

def boost_bar():
    global window
    global player

    width = player.boost_timer
    height = 30

    xpos = (WIDTH - 30) - width
    ypos = HEIGHT - (30 + height)

    pygame.draw.rect(window, BLACK, (xpos, ypos, width, height))

    t = FONT_M.render("x2 Boost", 1, BLACK)

    xpos = (WIDTH - 20) - t.get_width()
    ypos = (HEIGHT - (30 + height)) - 20 - t.get_height()

    window.blit(t, (xpos, ypos))


def collide(obstacle):

    global player

    player_in_ob = (obstacle.right > player.left > obstacle.left or obstacle.right > player.right > obstacle.left) and (
                obstacle.bottom > player.top > obstacle.top or obstacle.bottom > player.bottom > obstacle.top)
    ob_in_player = (player.right > obstacle.left > player.left or player.right > obstacle.right > player.left) and (
                player.bottom > obstacle.top > player.top or player.bottom > obstacle.bottom > player.top)

    return True if (player_in_ob or ob_in_player) else False

# Game loop

mixer.music.play(-1)

while running:

    frame += 1

    clock.tick(MAX_FPS)

    draw()

    if player.boost_timer > 0:
        player.boost_timer -= 1

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_UP] or keys[ord('w')]) and player.player_y > 0:
        player.move_up()

    if (keys[pygame.K_DOWN] or keys[ord('s')]) and player.player_y < HEIGHT - player.img.get_height():
        player.move_down()

    if (keys[pygame.K_LEFT] or keys[ord('a')]) and player.player_x > 0:
        player.move_left()

    if (keys[pygame.K_RIGHT] or keys[ord('d')]) and player.player_x < WIDTH - player.img.get_width():
        player.move_right()

    if keys[ord('o')]:
        player.enlarge()

    if keys[ord('p')]:
        player.shrink()

    for obstacle in obstacles:

        if collide(obstacle):

            obstacles.remove(obstacle)

            if obstacle.good == True:

                gained = 2 if player.boost_timer > 0 else 1

                score += gained
                currency += gained

            elif obstacle.good == False:

                if player.shields > 0:

                    player.shields -= 1

                else:

                    status = "review"
                    end = time.time()
                    time_passed = round(end - start, 2)
                    break

            elif obstacle.good == None:

                code = obstacle.code

                if code == "x2":
                    player.boost_timer += MAX_FPS * 15

        else:

            pass

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            if status == "game":

                for item in powerups:

                    (x, y), radius, price, code = item

                    if ((mx - x) ** 2 + (my - y) ** 2) ** 0.5 < radius:

                        if currency >= price:

                            if code == "shields":
                                currency -= price
                                player.shields += 1


            elif status == "menu":

                for item in menu_buttons:

                    rect_details, t, t_details, code = item
                    xpos, ypos, width, height = rect_details

                    if (xpos + width > mx > xpos) and (ypos + height > my > ypos):

                        if code == "game":

                            start = time.time()
                            status = "game"
                            score = 0
                            player.reset()
                            obstacles = []

                        elif code == "shop":
                            status = "shop"

            elif status == "shop":

                for item in powerups:

                    (x, y), radius, price, code = item

                    if ((mx - x) ** 2 + (my - y) ** 2) ** 0.5 < radius:

                        if currency >= price:

                            if code == "shields":
                                currency -= price
                                player.shields += 1

                if (245 > mx > 15) and (115 > my > 15):
                    status = "menu"

                for i in range(len(skins)):

                    item = skins[i]

                    image, purchased, pos, dim, price, skin_id = item

                    if (pos[0] + dim[0] > mx > pos[0]) and (pos[1] + dim[1] > my > pos[1]):

                        if purchased == True:

                            player.change_skin(new=skin_id)

                        else:

                            if currency >= price:

                                currency -= price
                                skins[i][1] = True

                            else:
                                pass

                        break

                if include_button == True:

                    x, y, width, height = update_bkgr

                    if (x + width > mx > x) and (y + height > my > y) and (currency >= bkgr_price):
                        currency -= bkgr_price
                        background += 1

        elif e.type == pygame.KEYDOWN:
            if status == "review":
                status = "menu"

pygame.quit()