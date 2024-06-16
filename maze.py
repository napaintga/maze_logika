#створи гру "Лабіринт"!

om pygame import *

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

wn = display.set_mode((700,500))
display.set_caption("Лабіринт-логіка")
clock = time.Clock()
game = True
finish = False
FPS= 60
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        self.image= transform.scale(image.load(pl_image), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed

    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
background = transform.scale(image.load("background.jpg"),(700,500))
while game:
    wn.blit(background,(0,0))
    player.reset()
    enemy.reset()

    for e in event.get():
        if e.type == QUIT:
            game= False

    display.update()
    clock.tick(FPS)
