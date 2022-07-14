from pygame import *

win_height = 500
win_width = 700
finish = False

display.set_caption('Игра Лабиринт!')
window = display.set_mode((win_height, win_width))
back = (119, 210, 223)
barriers = sprite.Group()


class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,self,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
         GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)

         self.x_speed = player_x_speed
         self.y_speed = player_y_speed
    def update(self):

        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        
        platform_toched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platform_touched:
                self.rect.right = min(self.rect.right,p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = min(self.rect.left, p.rect.right)
        
        if packman.rect.y <= win_width-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed

        platform_toched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platform_touched:
                self.rect.bottom = min(self.rect.bottom,p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = min(self.rect.top, p.rect.bottom)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 420:
            self.side = True
        if self.rect.x >= win_width - 85:
            self.side = False 
        if self.side  == False:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
w1 = GameSprite('wall1.png',win_width / 2 - win_width / 3,win_height / 2,300, 50)
w2 = GameSprite('wall2.png', 370, 100, 50, 400)

barriers.add(w1)
barriers.add(w2)

pacman = Player('hero.png',5,win_weight - 80,80,80, 0 , 0)
final_sprite = GameSprite('cherry.png',win_width - 85, win_height - 100, 80, 80)
monster = GameSprite('monster.png',win_width - 80, 180, 80, 80)
run = True
while run:
    time.delay(50)
    window.fill(back)
    
    for e in event.get():
        if e.type == QUIT:
            run = False 
        

        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.ket == K_DOWN:
                packman.y_speed = 0
    if not finish:
        window.fill(back)
        packman.update()
        final_sprite.reset()
        packman.reset()


    if sprite.collide_rect(packman, monster):
        finish = True
        img = image.load('game_over.png')
        d = img.get_width() // img.get_height()
        window.fill(255, 255, 255)
        window.blit(transform.scale(img,(win_weight * d, win_height)),(90, 0))
    
    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load('win.png')
        window.fill(255, 255, 255)
        window.blit(transform.scale(img,(win_width, win_height)),(0, 0))



    display.update()