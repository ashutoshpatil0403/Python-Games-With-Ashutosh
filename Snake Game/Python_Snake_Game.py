import pygame
import random
x=pygame.init() #initialising all the modules from pygame
#print(x)
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

#Creating Window
screen_width=900
screen_height=550
Game_display=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Python_Food")


#Game Specific Variable
def gameloop():    
    exit_game=False
    game_over=False 
    snake_x=50  #initial position in x
    snake_y=70  #initial position in y
    init_velocity=5
    velocity_x=0
    velocity_y=0
    snake_size=10
    food_x=random.randint(25,800)
    food_y=random.randint(20,400)
    fps=35   #frame per second
    clock=pygame.time.Clock()
    score=0

#     For game score on gamescreen  #No ratta mar All things on pygame documentation
    font=pygame.font.SysFont(None,55)

    def plot_snake(Game_dislpay,color,snake_list,snake_size):
        for x,y in snake_list:
            pygame.draw.rect(Game_dislpay,color,[x,y,snake_size,snake_size])

    def text_screen(text,color,x,y):
        screen_text=font.render(text,True,color)
        Game_display.blit(screen_text,[x,y])

    snake_list=[]
    snake_length=1

    #Creating GAme Loops
    while not exit_game:
        if game_over:
            Game_display.fill(white)
            text_screen("Game Over!",red,screen_width*0.5,screen_height*0.5)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()    
        else:

            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_x = snake_x +  10  
                        velocity_x= init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        snake_x = snake_x -  10  
                        velocity_x= - init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        snake_y = snake_y -  10
                        velocity_y = -init_velocity
                        velocity_x=0 

                    if event.key == pygame.K_DOWN:
                        snake_y = snake_y +  10
                        velocity_y = init_velocity
                        velocity_x=0            

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
    
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score += 1
                print("Score :",score*10 )
                food_x=random.randint(25,800)
                food_y=random.randint(20,400)
                snake_length += 2                      

            Game_display.fill(white)
            #screen score
            text_screen("Score :"+str(score*10),green,5,5)
            pygame.draw.rect(Game_display,red,[food_x,food_y,snake_size,snake_size])
    
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)> snake_length:
                del snake_list[0]

            if snake_x <0 or snake_y <0 or snake_y > screen_height or snake_x > screen_width:
                game_over=True
                print("Game Over!")


            #pygame.draw.rect(Game_display,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(Game_display,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
gameloop()    
