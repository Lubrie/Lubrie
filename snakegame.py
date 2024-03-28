import pygame
from random import randint
pygame.init()

x = 1270
y = 700

screen = pygame.display.set_mode((x, y))

rodando = True


#posiçôes
snake_x = 635
snake_y = 350


maca_x = 500
maca_y = 225
x_control = 20
y_control= 0 
pontos = 0
velocity = 10
font = pygame.font.SysFont('arial', 50, False, False)

clock = pygame.time.Clock()

died = False

#functionasd
lista_snake = []
comprimento_inicial = 10
def snake_size(lista_snake):
    for XeY in lista_snake:
        pygame.draw.rect(screen, (0,0,255), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, snake_x, snake_y, lista_snake, lista_cabeca, maca_x, maca_y, died
    pontos = 0
    comprimento_inicial = 0
    snake_x = int(x/2)
    snake_y = int(y/2)
    lista_snake = []
    lista_cabeca = []
    maca_x = randint(100, 999)
    maca_y = randint(100, 680)
    died = False



while rodando:
    screen.fill((255,255,255))
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               if x_control == velocity:
                pass
               else: 
                    x_control = -velocity
                    y_control = 0
            if event.key == pygame.K_d:
                if x_control == -velocity:
                    pass
                else:

                    x_control = velocity
                    y_control = 0
            if event.key == pygame.K_w:
                if y_control == velocity:
                    pass
                else:
                    y_control = -velocity
                    x_control = 0
            if event.key == pygame.K_s:
                if y_control == -velocity:
                    pass
                else:
                    y_control = velocity
                    x_control = 0
    
    snake_x += x_control
    snake_y += y_control
    
    #pontos
    msg = f'Pontos: {pontos}'
    texto_format = font.render(msg, True, (0,0,0))
    
    
    #desenho
    maca = pygame.draw.rect(screen, (255,0,0), (maca_x,maca_y, 10,10))
    snake = pygame.draw.rect(screen, (0,0,255), (snake_x,snake_y, 20,20))
    
    
    #movimentos
    if snake_x > 1270:
        snake_x = 0
    
    if snake_x < -4:
        snake_x = 1270 
        pontos -= 1
    if snake_y > 700 :
        snake_y = 0
        pontos -= 1
    if snake_y < -4:
        snake_y = 700
        pontos -= 1
    
    
    # teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_w]:
    #     snake_y -= 1
    # if teclas[pygame.K_s]:
    #     snake_y +=1
    # if teclas[pygame.K_a]:
    #     snake_x -=1
    # if teclas[pygame.K_d]:
    #     snake_x+=1
    
    
    
    #colisão
    if snake.colliderect(maca):
        #print('SHOW')
        maca_x = randint(100, 999)
        maca_y = randint(100, 680)
        pontos += 1
        comprimento_inicial += 1
    #pontos
    
    screen.blit(texto_format, (980, 50))
    
    
    lista_cabeca = []
    lista_cabeca.append(snake_x)
    lista_cabeca.append(snake_y)    
    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]
    
    
    lista_snake.append(lista_cabeca)
    
    
    # Loop tela de Game Over
    if lista_snake.count(lista_cabeca)> 1 or pontos < 0:
        died = True
        while died:         
            screen.fill((255,255, 255))
            font2 = pygame.font.SysFont('arial', 20, True, True) #termos booleanos: 1 Negrito, 2 Itálico, 
            mensagem = 'Game Over! Precione R para reiniciar'
            
            text_format = font2.render(mensagem, True, (0,0,0))
            rect_text_format = text_format.get_rect()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:   
                        reiniciar_jogo()
            rect_text_format.center = (x//2, y//2)
            screen.blit(text_format, (rect_text_format))
            pygame.display.update()
    snake_size(lista_snake)
    
    
    

    pygame.display.update()