import pygame #导入pygame
from pygame.locals import * #导入pygame本地所有的函数和常量
import time #导入时间对象
import random #导入随机数对象

pygame.init() #初始化pygame

screen=pygame.display.set_mode((480,500)) #创建飞机大战窗口
pygame.display.set_caption('飞机大战') #窗口命名为飞机大战
bg=pygame.image.load('background.png') #加载背景图片

num=0 #时间计时器
#加载敌飞机1
enemy1=pygame.image.load('enemy1.png')
enemy1_x=[]
enemy1_y=[]
#加载敌飞机2    
enemy2=pygame.image.load('enemy2.png')
enemy2_x=[]
enemy2_y=[]
enemy2_blood=[]
#加载敌飞机3
enemy3=pygame.image.load('enemy3.png')
enemy3_x=[]
enemy3_y=[]
enemy3_blood=[]
#加载英雄机
hero0=pygame.image.load('hero0.png') #加载英雄机图片一
hero1=pygame.image.load('hero1.png') #加载英雄机图片二
hero_down=pygame.image.load('hero_down.png') #英雄机牺牲图片
heroX=200
heroY=400

#加载子弹图片
bullet=pygame.image.load('bullet.png')
bullet_x=[]
bullet_y=[]

#计分文字
font=pygame.font.Font('simsun.ttc',40)
text=font.render('得分:',True,(255,0,0))
score=0

#载入游戏结束图片
Isgameover=0
gameoverImage=pygame.image.load('gameover.png')
gameoverImage=pygame.transform.scale(gameoverImage,(480,800))

#生成敌机并下降
def enemy(image,n,x,y):     #参数：enemy代表敌飞机类型，n代表节奏数字，x,y代表敌飞机坐标的列表,speed代表节奏
    if num % n == 0:
        x.append(random.randint(0,480))
        y.append(0)
    for i in range(len(x)):
        screen.blit(image,(x[i],y[i]))
    for i in range(len(y)):
        y[i]=y[i]+2
        if y[i]>800:
            y[i] = 0 
            x[i] = random.randint(0,700)
            break
        
#敌机消除 边界判定法
def enemy_died(enemy,enemy_x,enemy_y,n):
    global score
    for i in range(len(bullet_x)):
        for j in range(len(enemy_x)):
            if bullet_x[i]>enemy_x[j]-bullet.get_width() and bullet_x[i]<enemy_x[j]+enemy.get_width() and bullet_y[i]>enemy_y[j]-bullet.get_height() and bullet_y[i]<enemy_y[j]+enemy.get_height():
                score += n
                del enemy_x[j]
                del enemy_y[j]
                break                       
                    
#主循环体
while True:
    screen.blit(bg,(0,0)) #将背景图片贴到窗口中

    screen.blit(text,(10,10))
    text_score=font.render(str(score),True,(255,0,0))
    screen.blit(text_score, (120, 10))

    if Isgameover==0:
        num +=1
        #调用方法传参生成3架敌机
        enemy(enemy1,30,enemy1_x,enemy1_y)
        enemy(enemy2,150,enemy2_x,enemy2_y)   
        enemy(enemy3,600,enemy3_x,enemy3_y)
        
        #生成英雄机并随鼠标移动
        if num%2==0:
            screen.blit(hero1,(heroX,heroY))
        else:
            screen.blit(hero0,(heroX,heroY))
        #英雄机随鼠标移动    
        pos=pygame.mouse.get_pos()        #pos=[x,y] 鼠标的X,Y坐标值
        heroX=pos[0]-hero0.get_width()/2  #让英雄机的X坐标等于当前鼠标的X坐标值
        heroY=pos[1]-hero0.get_height()/2 #让英雄机的Y坐标等于当前鼠标的Y坐标值
        
        #生成子弹并发射                   
        if num%10==0:   #两颗子弹的位置坐标
            bullet_x.append(heroX+hero0.get_width()/4-bullet.get_width()/2-8)
            bullet_y.append(heroY+hero0.get_height()/4)     
            bullet_x.append(heroX+3*hero0.get_width()/4+5)
            bullet_y.append(heroY+hero0.get_height()/4)
        #将子弹贴到窗口英雄飞机的头上
        for i in range(len(bullet_x)):
            screen.blit(bullet,(bullet_x[i],bullet_y[i]))
        #让子弹打出去
        for i in range(len(bullet_x)):
            bullet_y[i]=bullet_y[i]-10
            if bullet_y[i]<0:
                del bullet_y[i]
                del bullet_x[i]
                break  
            
        enemy_died(enemy1,enemy1_x,enemy1_y,1) #调用方法，敌机1消除 边界判定法
        enemy_died(enemy2,enemy2_x,enemy2_y,5) #调用方法，敌机2消除 边界判定法
        enemy_died(enemy3,enemy3_x,enemy3_y,10) #调用方法，敌机3消除 边界判定法
        
        #英雄机牺牲
        for i in range(len(enemy1_x)):
            if enemy1_x[i]>heroX-enemy1.get_width() and enemy1_x[i]<heroX+hero0.get_width() and enemy1_y[i]>heroY-enemy1.get_height() and enemy1_y[i]<heroY+hero0.get_height():
                screen.blit(hero_down,(heroX,heroY))
                Isgameover=1
                break
        
    else:
        screen.blit(gameoverImage,(0,0))
         
    #窗口退出
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update() #屏幕更新
    
    
