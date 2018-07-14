from pygame.locals import *
import pygame
import time

class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 670
        self.screen = screen_temp
        self.image = pygame.image.load("./shoot/hero1.png")
        self.bullet_list = []#存储子弹

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x-=5

    def move_right(self):
        self.x+=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane(object):
    def __init__(self,screen_temp):
        self.x=0
        self.y=0
        self.screen = screen_temp
        self.image = pygame.image.load("./shoot/enemy1.png")
        self.direction = "right"#存储默认方向
        self.bullet_list=[]#存储子弹

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        if self.direction == "right":
            self.x+=5
        elif self.direction == "left":
            self.x-=5

        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"

    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+48
        self.y = y+20
        self.screen = screen_temp
        self.image = pygame.image.load("./shoot/bullet1.png")

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y-=5

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

def key_control(hero_temp):
     #获取按键事件
    for event in pygame.event.get():
         #退出按键
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            elif event.key == K_SPACE:
                hero_temp.fire()


def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    background = pygame.image.load("./background.png")
    #创建飞机

    hero = HeroPlane(screen)

    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))

        hero.display()

        enemy.display()

        enemy.move()

        pygame.display.update()

        key_control(hero)

        #获取按键事件
        time.sleep(0.01)

if __name__=="__main__":
    main()
