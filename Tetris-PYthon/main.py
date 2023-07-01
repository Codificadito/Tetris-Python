import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fondo = pygame.image.load("Tetrix proyecto/img/fondos/foto-tetris-2.jpg")
fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))  # Escalar el fondo al tamaño de la pantalla
pygame.display.set_caption("TETRIS :D")



######## textos ###############
#####fuente ######
fuente = pygame.font.Font(None, 55)
##################################

texto_lines_numero = 0
texto_nivel_numero = 0
texto_scored_numero = 0
texto_top_numero = 0

texto_figura_1 = 0
texto_figura_2 = 0
texto_figura_3 = 0
texto_figura_4 = 0
texto_figura_5 = 0
texto_figura_6 = 0
texto_figura_7 = 0
#nivel del juego
nivel=0




rows = 20  # Número de filas visibles
rows_logicos=24
cols = 10  # Número de columnas visibles
cell_size = 28  # Tamaño de cada celda en píxeles

frame_width = cols * cell_size + 2  # Ancho del marco
frame_height = rows * cell_size + 2  # Alto del marco
frame_x = 490 #(screen.get_width() - frame_width) // 2  # Posición x del marco
frame_y =150 #(screen.get_height() - frame_height) // 2  # Posición y del marco




class Figura:
    color="color"
    block=0
    move=1
    matris=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]] 
###cuadro del la proxima figura ####
frame_x_figura_proxima = 909 #(screen.get_width() - frame_width) // 2  # Posición x del marco
frame_y_figura_proxima =370 #(screen.get_height() - frame_height) // 2  # Posición y del marco
frame_width_figura_proxima = len(Figura.matris[0]) * cell_size + 2  # Ancho del marco
frame_height_figura_proxima = len(Figura.matris[1]) * cell_size + 2
# Figura L
class Figura_L:
    tipo = "L"
    color="orange"
    block=0
    move=1
    matris=[[0,0,0,0],
            [1,1,1,0],
            [1,0,0,0],
            [0,0,0,0]] 
#print(figura_L.figure[1])

# Figura J
class Figura_J:
    tipo = "J"
    color="blue"
    block=0
    move=1
    matris= [[0,0,0,0],
             [0,1,0,0],
             [0,1,1,1],
             [0,0,0,0]]  

# Figura T
class Figura_T :
    tipo = "T"
    color="purple"
    block=0
    move=1
    matris= [[0,0,0,0],
             [0,0,1,0],
             [0,1,1,1],
             [0,0,0,0]]  

# Figura S
class Figura_S :
    tipo = "S"
    color="green"
    block=0
    move=1
    matris= [[0,0,1,0],
             [0,1,1,0],
             [0,1,0,0],
             [0,0,0,0]]  

# Figura Z
class Figura_Z: 
    tipo = "Z"
    color="white"
    block=0
    move=1
    matris= [[0,1,0,0],
             [0,1,1,0],
             [0,0,1,0],
             [0,0,0,0]] 

# Figura I
class Figura_I :
    tipo = "I"
    color="cyan"
    block=0
    move=1
    matris=[[0,0,0,0],
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0]]  

# Figura O
class Figura_O :
    tipo = "O"
    color="yellow"
    block=0
    move=1
    matris=[[0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]] 

        
class StarFigure():
    
    figuras = [Figura_O, Figura_I, Figura_J, Figura_L, Figura_S, Figura_T, Figura_Z]
    figura_actual = None
    figura_siguiente = None
    
    def __init__(self):
        self.figura_actual = random.choice(self.figuras)
        self.figura_siguiente = random.choice(self.figuras)
    
    def obtener_figura_actual(self):
        return self.figura_actual
    
    def obtener_figura_siguiente(self):
        figura_siguientee=self.figura_siguiente
        
        return figura_siguientee
    
    def cambiar_figura(self):
        self.figura_actual = self.figura_siguiente
        self.figura_siguiente = random.choice(self.figuras)

    def obtener_figura_matris(self):
        return self.figura_actual
    
    def obtener_figura_color(self):
        return self.figura_actual
      
        
   
    """
    figura_actual = figura_siguiente
    figura_siguiente = random.choice(figuras)
    """
    

    
# end def

figura=StarFigure()

class Posicion:
    def __init__(self,):
        self.color=""
        self.valor=0
        self.block=0 # sinifica que no se mueva
        self.move=0 #sinifica que se mueva con el cursor
    
        



velocidad_de_bajada=0
table = []
# matriz
n = 0
if len(table) == 0:
    for row in range(rows_logicos):
        n += 1
        row_list = [Posicion() for _ in range(cols)]
        table.append(row_list)

"""
for row in table:
    for element in row:
        print(element[1].valor, end=' ')
    print() """

def pausar_juego():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausado = False

#############CONFIG BOTONES############


DELAY = 150


############# sub configuraciones ############
game_start = False


while running:
    
    
            ###############################inicio##########################################




    ttexto_lines = fuente.render(str(texto_lines_numero), True, (255, 255, 255))
    ttexto_nivel_numero = fuente.render(str(texto_nivel_numero), True, (255, 255, 255))
    ttexto_top_numero = fuente.render(str(texto_top_numero), True, (255, 255, 255))
    ttexto_scored_numero = fuente.render(str(texto_scored_numero), True, (255, 255, 255))
    ttexto_figura_1 = fuente.render(str(texto_figura_1), True, (255, 255, 255))
    ttexto_figura_2 = fuente.render(str(texto_figura_2), True, (255, 255, 255))
    ttexto_figura_3 = fuente.render(str(texto_figura_3), True, (255, 255, 255))
    ttexto_figura_4 = fuente.render(str(texto_figura_4), True, (255, 255, 255))
    ttexto_figura_5 = fuente.render(str(texto_figura_5), True, (255, 255, 255))
    ttexto_figura_6 = fuente.render(str(texto_figura_6), True, (255, 255, 255))
    ttexto_figura_7 = fuente.render(str(texto_figura_7), True, (255, 255, 255))




    


    
    

    ############### funciones #########################

    def fun_insertar(table,obj):#inserta la figura en la tabla
        
        figura_ancho=len(obj.figura_actual.matris[0])
        figura_alto=len(obj.figura_actual.matris[1])
        existe= False
        for i in range(len(table)):
            for e in range(len(table[1])):
                if (table[i][e-1].move==1):
                    existe =True
                    
        if existe == False:
            for i in range(figura_alto):
                #table[row][col]=obj.matris[i][1]
                for e in range(figura_ancho):
                        #print("por defecto",table[i][(e+figura_ancho)].valor,(obj.matris[i][e]))
                        #print(obj.figura_actual.tipo,"i:",i,"  e:",e)
                        #print("objeto",obj.figura_actual.matris)
                        table[i][(e+figura_ancho)-1].valor=obj.figura_actual.matris[i][e]
                        table[i][(e+figura_ancho)-1].color=obj.figura_actual.color
                        if obj.figura_actual.matris[i][e]:
                            table[i][(e+figura_ancho)-1].block=(obj.figura_actual.block)
                            table[i][(e+figura_ancho)-1].move=(obj.figura_actual.move)
            count_figure(figura)
            figura.cambiar_figura()

        


    def fun_verificar_colicion_izquierda(tabla) -> bool:
        filas = len(tabla)
        cols = len(tabla[0])
        
        for i in range(filas):
            if tabla[i][0].move == 1 :
                return False
        
        return True
    
    def fun_verificar_colicion_bloque_izquierda(table):
        filas = len(table)
        cols = len(table[0])
        for i in range(filas):
            for e in range(1,cols-1):
                if (table[i][e-1].block==1==table[i][e].move):
                    return False
        return True


    def fun_verificar_colicion_derecha(tabla):
        filas = len(tabla)
        cols = len(tabla[0])
        
        for i in range(filas):
            if tabla[i][cols-1].move == 1:
                return False
        
        return True
    
    def fun_verificar_colicion_bloque_derecha(table):
        filas = len(table)
        cols = len(table[0])
        for i in range(filas):
            for e in range(cols-1):
                if (table[i][e+1].block==1==table[i][e].move):
                    return False
        return True
     
    
    def fun_verificar_colicion_base(table):
        filas = len(table)
        cols = len(table[0])

        for j in range(cols):
            #ver que pasa qui
            if table[filas-1][j].move == 1:
                for i in range(len(table)):
                    for e in range(len(table[0])):
                        table[i][e].block=table[i][e].valor
                        table[i][e].move=0
                        
                return True
        
        return True
    
    def fun_verificar_colicion_abajo(table):
        filas = len(table)
        cols = len(table[0])
        for j in range(cols):
            for i in range(filas-1):
                if (table[i+1][j].block)==1==(table[i][j].move):
                    for i in range(len(table)):
                        for e in range(len(table[0])):
                            table[i][e].block=table[i][e].valor
                            table[i][e].move=0
                    return False
        return True
        
        

    def fun_encontrar_matris(table):
        x1 = len(table[0])
        y1 = len(table)
        x2 = 0
        y2 = 0

        for i in range(len(table)):
            for e in range(len(table[1])):#antes era i
                if table[i][e].move == 1:
                    if x1 > e:
                        x1 = e
                    if y1 > i:
                        y1 = i
                    if x2 < e:
                        x2 = e
                    if y2 < i:
                        y2 = i
        cordenadas=(x1,y1,x2,y2)
        return cordenadas
    
   

    
    def fun_girar_figura(table, cordenada):
        x1 = cordenada[0]
        y1 = cordenada[1]
        x2 = cordenada[2]
        y2 = cordenada[3]

        # Obtener la figura dentro de la matris
        figura = []
        for i in range(y1, y2+1):
            fila = []
            for j in range(x1, x2+1):
                fila.append([table[i][j].move, table[i][j].color])
                # Quitar propiedades
                table[i][j].move = 0
                table[i][j].valor = 0
                table[i][j].color = Posicion().color
            figura.append(fila)

        # Calcular las dimensiones de la figura
        width = len(figura[0])
        height = len(figura)

        # Crear una nueva matriz girada
        nueva_matriz = []
        for j in range(width-1, -1, -1):
            fila = []
            for i in range(height):
                fila.append(figura[i][j])
            nueva_matriz.append(fila)

        # Encontrar las dimensiones de la nueva figura
        nueva_width = len(nueva_matriz[0])
        nueva_height = len(nueva_matriz)

        # Calcular las coordenadas iniciales de la figura girada
        ini_x = x1 + (width - nueva_width) // 2
        ini_y = y1 + (height - nueva_height) // 2

        # Verificar si la figura girada se sale de la matriz
        if ini_x < 0:
            ini_x = 0
        elif ini_x + nueva_width > len(table[0]):
            ini_x = len(table[0]) - nueva_width
        if ini_y < 0:
            ini_y = 0
        elif ini_y + nueva_height > len(table):
            ini_y = len(table) - nueva_height

        # Actualizar la matriz original con la figura girada
        for i in range(nueva_height):
            for j in range(nueva_width):
                if table[ini_y + i][ini_x + j]:
                    table[ini_y + i][ini_x + j].move = nueva_matriz[i][j][0]
                    table[ini_y + i][ini_x + j].color = nueva_matriz[i][j][1]
                    table[ini_y + i][ini_x + j].valor = nueva_matriz[i][j][0]




        """
        for row in table:
            for columnas in row:
                print(columnas.move, end=" ")
            print()

        print("Coordenadas del objeto:")
        print("x1 =", x1)
        print("y1 =", y1)
        print("x2 =", x2)
        print("y2 =", y2)
        
        for rowx in table:
            for element in rowx:
                print(element.valor, end=' ')
            print()
        """
    def fun_acople(table):
        filas = len(table)
        cols = len(table[0])
        lineas_eliminadas=0
        global texto_nivel_numero
        global texto_scored_numero
        for z in range(filas):
            if all(table[z][j].block == 1 for j in range(cols)):
                table.pop(z)  # Elimina la fila completa
                table.insert(0, [Posicion() for _ in range(cols)])  # Agrega una nueva fila vacía en la parte superior
                global velocidad_de_bajada 
                velocidad_de_bajada +=1
                global texto_lines_numero
                texto_lines_numero +=1
                
        texto_nivel_numero = (texto_lines_numero // 4) + 1
        texto_scored_numero =(texto_lines_numero ** 2) * texto_nivel_numero
        
        
        
        
    
        
    def boton_bajar(table):
        if fun_verificar_colicion_base(table) and fun_verificar_colicion_abajo(table):
            for i in range(len(table) - 2, -1, -1):
                for e in range(len(table[i])):
                    if table[i][e].move == 1:
                        if table[i + 1][e].valor == 0:
                            # Intercambiar los valores y propiedades entre las celdas
                            valoractual = table[i][e].valor
                            valorsiguiente = table[i + 1][e].valor
                            table[i + 1][e].valor = valoractual
                            table[i][e].valor = valorsiguiente

                            moveactual = table[i][e].move
                            movesiguiente = table[i + 1][e].move
                            table[i + 1][e].move = moveactual
                            table[i][e].move = movesiguiente

                            coloractual = table[i][e].color
                            colorsiguiente = table[i + 1][e].color
                            table[i + 1][e].color = coloractual
                            table[i][e].color = colorsiguiente

    def velocidad_bajada(velocidad_de_bajada=1):
        boton_bajar(table)
        pygame.time.delay(DELAY-velocidad_de_bajada)

    def perder(table):
        filas = len(table)
        cols = len(table[0])
        for i in range(filas-19):
            for j in range(cols):
                if table[i][j].move == 1 and i < filas - 1 and table[i+1][j].block == 1:
                    global game_start
                    game_start = False
                    return False
                    #perdio
        return True
    
    def count_figure(figura):
        tipo=figura.figura_actual.tipo
        if tipo =="T":
            global texto_figura_1
            texto_figura_1 +=1
        if tipo =="J":
            global texto_figura_2
            texto_figura_2 +=1
        if tipo =="S":
            global texto_figura_3
            texto_figura_3 +=1
        if tipo =="O":
            global texto_figura_4
            texto_figura_4 +=1
        if tipo =="Z":
            global texto_figura_5
            texto_figura_5 +=1
        if tipo =="L":
            global texto_figura_6
            texto_figura_6 +=1
        if tipo =="I":
            global texto_figura_7
            texto_figura_7 +=1
        
    def game_restar():
        print("")
        

        
    # funciones de incio
    
    velocidad_bajada(texto_nivel_numero)
    fun_acople(table)
    if game_start == True:
        fun_insertar(table,figura)

        
    perder(table)




    screen.blit(fondo, (0, 0))  # Dibujar el fondo en la posición (0, 0) de la pantalla
    screen.blit(ttexto_lines, (800, 60))#
    screen.blit(ttexto_nivel_numero, (1000, 576))
    screen.blit(ttexto_top_numero, (1000, 130))
    screen.blit(ttexto_scored_numero, (1000, 215))
    screen.blit(ttexto_figura_1, (320, 300))
    screen.blit(ttexto_figura_2, (320, 365))
    screen.blit(ttexto_figura_3, (320, 430))
    screen.blit(ttexto_figura_4, (320, 495))
    screen.blit(ttexto_figura_5, (320, 535))
    screen.blit(ttexto_figura_6, (320, 580))
    screen.blit(ttexto_figura_7, (320, 640))


    # cuadricula de las proxiuma figura#
    for row in range(len(Figura.matris[0])+1):
        pygame.draw.line(screen, (255, 255, 255), (frame_x_figura_proxima, (row * cell_size) + frame_y_figura_proxima), (len(Figura.matris[0]) * cell_size + frame_x_figura_proxima, row * cell_size + frame_y_figura_proxima))

    for col in range(len(Figura.matris[1])+1):
        pygame.draw.line(screen, (255, 255, 255), (frame_x_figura_proxima + (col * cell_size), frame_y_figura_proxima), ((col * cell_size) + frame_x_figura_proxima,(len(Figura.matris[1]) * cell_size)+ frame_y_figura_proxima))
        
    for row in range(len(Figura.matris[0])):
            for col in range(len(figura.figura_actual.matris[1])):
                if figura.figura_actual.matris[row][col] == 1 :
                    # Dibujar celda ocupada
                    pygame.draw.rect(screen, (figura.figura_actual.color), (frame_x_figura_proxima + col * cell_size + 1, (frame_y_figura_proxima) + row * cell_size + 1, cell_size - 2, cell_size - 2))
                    """  
                    else:
                    # Dibujar celda libre
                        pygame.draw.rect(screen, (Posicion().color), (frame_x_figura_proxima + col * cell_size + 1, (frame_y_figura_proxima-111) + row * cell_size + 1, cell_size - 2, cell_size - 2))
                    """  


    # Dibujar líneas horizontales --
    
    for row in range(rows + 1):
        
        pygame.draw.line(screen, (255, 255, 255), (frame_x, (row * cell_size) + frame_y), (cols * cell_size + frame_x, row * cell_size + frame_y))
        
    # Dibujar líneas verticales |
    for col in range(cols + 1):
        
        pygame.draw.line(screen, (255, 255, 255), (frame_x + (col * cell_size), frame_y), ((col * cell_size) + frame_x,(rows * cell_size)+ frame_y))
        #table[].append(n)

    
    # Dibujar la tabla en la cuadrícula
    for row in range(4,rows_logicos):
        for col in range(cols):
            if table[row][col].valor == 1 :
                # Dibujar celda ocupada
                pygame.draw.rect(screen, (table[row][col].color), (frame_x + col * cell_size + 1, (frame_y-111) + row * cell_size + 1, cell_size - 2, cell_size - 2))
            """  
            else:
               # Dibujar celda libre
                pygame.draw.rect(screen, (Posicion().color), (frame_x + col * cell_size + 1, (frame_y-111) + row * cell_size + 1, cell_size - 2, cell_size - 2))
            """  

    pygame.display.flip()
    #keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                boton_bajar(table)
                

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            
            if fun_verificar_colicion_izquierda(table) and fun_verificar_colicion_bloque_izquierda(table):
                i = 0
                for fila in table:
                    e = 0
                    while e < len(fila):
                        if table[i][e].move == 1:
                            if e > 0 and table[i][e-1].valor == 0:
                                # Guardar los valores y propiedades de la celda actual
                                valoractual = table[i][e].valor
                                valorsiguiente = table[i][e-1].valor
                                table[i][e-1].valor = valoractual
                                table[i][e].valor = valorsiguiente

                                moveactual = table[i][e].move
                                movesiguiente = table[i][e-1].move
                                table[i][e-1].move = moveactual
                                table[i][e].move = movesiguiente

                                coloractual = table[i][e].color
                                colorsiguiente = table[i][e-1].color
                                table[i][e-1].color = coloractual
                                table[i][e].color = colorsiguiente

                        e += 1
                    i += 1

            


                


        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            
            if fun_verificar_colicion_derecha(table) and fun_verificar_colicion_bloque_derecha(table):
                i = 0
                for fila in table:
                    e = len(fila) - 1
                    while e >= 0:
                        if table[i][e].move == 1:
                            if e < len(fila) - 1 and table[i][e+1].valor == 0:
                                # Guardar los valores y propiedades de la celda actual
                                valoractual = table[i][e].valor
                                valorsiguiente = table[i][e+1].valor
                                table[i][e+1].valor = valoractual
                                table[i][e].valor = valorsiguiente

                                moveactual = table[i][e].move
                                movesiguiente = table[i][e+1].move
                                table[i][e+1].move = moveactual
                                table[i][e].move = movesiguiente

                                coloractual = table[i][e].color
                                colorsiguiente = table[i][e+1].color
                                table[i][e+1].color = coloractual
                                table[i][e].color = colorsiguiente

                        e -= 1
                    i += 1
          


        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            
            if game_start == False:
                fun_insertar(table,figura)
                game_start = True
            
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            
            cordenadas=fun_encontrar_matris(table)
            fun_girar_figura(table,cordenadas)
            
            
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pausar_juego()
        

    
    
    
    dt = clock.tick(60) / 1000
    """
    for row in table:
        for element in row:
            print(element, end=' ')
        print() """
    #print(table)
    #print(table[2][int(5)].valor)
    #print(figura.matris[2][2])

    #running=False
pygame.quit()