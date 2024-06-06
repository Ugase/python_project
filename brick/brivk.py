import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class GameObject:
    def __init__(self, sprite_img: str, transform=True):
        self.sprite = self.load_sprite_no(sprite_img)
        if transform:
            self.sprite = self.load_sprite(sprite_img)
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def load_sprite(self, sprite_img: str) -> pygame.Surface:
        spr = pygame.image.load(sprite_img)
        return pygame.transform.scale(spr, (100, 100))

    def load_sprite_no(self, sprite_img: str):
        spr = pygame.image.load(sprite_img)
        return spr

    def draw(self):
        screen.blit(self.sprite, self.position)

    def move(self, x: int, y: int):
        self.position = (self.position[0] + x, self.position[1] + y)

    def set_position(self, xy: tuple):
        self.position = xy

    def collides_with(self, other_object: "GameObject") -> bool:
        left1, top1 = self.position
        right1 = left1 + self.sprite.get_width()
        bottom1 = top1 + self.sprite.get_height()
        left2, top2 = other_object.position
        right2 = left2 + other_object.sprite.get_width()
        bottom2 = top2 + other_object.sprite.get_height()
        return left1 < right2 and right1 > left2 and top1 < bottom2 and bottom1 > top2


class Brick(GameObject):
    def __init__(self, position: tuple):
        super().__init__("E:\\Coding_Projects\\Python\\brick\\img\\brick.png")
        self.set_position(position)
        self.break_level = 0

    def check_is_broken(self):
        if self.break_level == 0:
            self.sprite = self.load_sprite(
                "E:\\Coding_Projects\\Python\\brick\\img\\brick.png"
            )
        elif self.break_level == 1:
            self.sprite = self.load_sprite(
                "E:\\Coding_Projects\\Python\\brick\\img\\brick1.png"
            )
        elif self.break_level == 2:
            self.sprite = self.load_sprite(
                "E:\\Coding_Projects\\Python\\brick\\img\\brick2.png"
            )
        elif self.break_level == 3:
            self.sprite = self.load_sprite(
                "E:\\Coding_Projects\\Python\\brick\\img\\brick3.png"
            )
        elif self.break_level == 4:
            self.sprite = self.load_sprite(
                "E:\\Coding_Projects\\Python\\brick\\img\\brick4.png"
            )
        else:
            self.set_position((10000000, 1000000000))

    def break_brick(self):
        self.break_level += 1
        self.check_is_broken()


class BrickGroup:
    def __init__(self):
        self.bricks = []
        self.last_broken_time = 0
    def add_brick(self, brick: Brick):
        self.bricks.append(brick)
    def draw(self):
        for brick in self.bricks:
            brick.draw()
    def check_collision(self, object: GameObject):
        current_time = pygame.time.get_ticks()
        inx = -1
        result: list[bool, int] = [True, inx]
        for brick in self.bricks:
            inx += 1
            result: list[bool, int] = [True, inx]
            if object.collides_with(brick):
                if current_time - self.last_broken_time > 200:  # 200ms delay
                    brick.break_brick()
                    self.last_broken_time = current_time
                return result
        return False

    def check_if_broken(self):
        for t in self.bricks:
            if t.break_level > 4:
                self.bricks.remove(t)
    def increse_broken(self, brick_num: int):
        self.bricks[brick_num - 1].break_level += 1


def random_position() -> tuple:
    return (
        random.randint(1, SCREEN_WIDTH - 100),
        random.randint(1, SCREEN_HEIGHT - 100),
    )


brick_group = BrickGroup()
for _ in range(50):
    brick = Brick(random_position())
    brick_group.add_brick(brick)

player = GameObject("E:\\Coding_Projects\\Python\\brick\\img\\car.png", transform=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key_presses = pygame.key.get_pressed()
    x_move, y_move = 0, 0
    if key_presses[pygame.K_w]:
        y_move = -5
    if key_presses[pygame.K_s]:
        y_move = 5
    if key_presses[pygame.K_a]:
        x_move = -5
    if key_presses[pygame.K_d]:
        x_move = 5
    new_position = (player.position[0] + x_move, player.position[1] + y_move)
    if (
        0 <= new_position[0] <= SCREEN_WIDTH - player.sprite.get_width()
        and 0 <= new_position[1] <= SCREEN_HEIGHT - player.sprite.get_height()
    ):
        player.set_position(new_position)
        if brick_group.check_collision(player):
            player.set_position(
                (player.position[0] - x_move, player.position[1] - y_move)
            )
    screen.fill((0, 0, 0))
    brick_group.draw()
    player.draw()
    pygame.display.update()

pygame.quit()