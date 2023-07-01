import pygame

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














rows = 20  # Número de filas visibles
rows_logicos=24
cols = 10  # Número de columnas visibles
cell_size = 28  # Tamaño de cada celda en píxeles

frame_width = cols * cell_size + 2  # Ancho del marco
frame_height = rows * cell_size + 2  # Alto del marco
frame_x = 490 #(screen.get_width() - frame_width) // 2  # Posición x del marco
frame_y =150 #(screen.get_height() - frame_height) // 2  # Posición y del marco


class Figure:
    def __init__(self, color, figure):
        self.color = color
        self.figure = figure
# Figura L
class Figura_L:
    color="orange"
    block=0
    move=1
    matris=[[0,0,0,0],
            [0,1,1,1],
            [0,1,0,0],
            [0,0,0,0]] 
#print(figura_L.figure[1])

# Figura J
class Figura_J:
    color="blue"
    block=0
    move=1
    matris= [[0,0,0,0],
             [0,1,0,0],
             [0,1,1,1],
             [0,0,0,0]]  

# Figura T
class Figura_T :
    color="purple"
    block=0
    move=1
    matris= [[0,0,0,0],
             [0,0,1,0],
             [0,1,1,1],
             [0,0,0,0]]  

# Figura S
class Figura_S :
    color="green"
    block=0
    move=1
    matris= [[0,0,1,0],
             [0,1,1,0],
             [0,1,0,0],
             [0,0,0,0]]  

# Figura Z
class Figura_Z: 
        color="green"
        block=0
        move=1
        matris= [[0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,0,0]] 

# Figura I
class Figura_I :
        color="cyan"
        block=0
        move=1
        matris=[[0,1,1,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]  

# Figura O
class Figura_O :
        color="yellow"
        block=0
        move=1
        matris=[[0,0,0,0],
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,0]]  
class Figura_cubo:
    color="black"
    block=0
    move=1
    matris=[[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
figura=Figura_Z #para prueba    

class Posicion:
    def __init__(self,):
        self.color="red"
        self.valor=0
        self.block=0 # sinifica que no se mueva
        self.move=0 #sinifica que se mueva con el cursor
    def get_color(self,):
        return self.color
        

p=Posicion()


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


#############CONFIG BOTONES############
DELAY = 200

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    def fun_insertar(table,obj,startrow=1,colestart=4):#inserta la figura en la tabla
        row=startrow
        col=colestart
        figura_ancho=4 #len(obj[0])
        figura_alto=4 #len(obj)
        for i in range(figura_alto):
            #table[row][col]=obj.matris[i][1]
            for e in range(figura_ancho):
                    #print("por defecto",table[i][(e+figura_ancho)].valor,(obj.matris[i][e]))
                    table[i][(e+figura_ancho)-1].valor=(obj.matris[i][e])
                    table[i][(e+figura_ancho)-1].color=obj.color
                    if obj.matris[i][e]:
                        table[i][(e+figura_ancho)-1].block=(obj.block)
                        table[i][(e+figura_ancho)-1].move=(obj.move)


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
    
            # Obtener la figura dentro de la matriz
        
        figura = []
        
        for i in range(y1, y2+1):
            fila = []
            for j in range(x1, x2+1):
                fila.append([table[i][j].move,table[i][j].color])
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
        for rowx in nueva_matriz:
            for element in rowx:
                print(element, end=' ')
            print()

        if len(nueva_matriz) ==len(nueva_matriz[0]) :
            # Actualizar la matriz original con la figura girada
            for i in range(height):
                for j in range(width):
                    table[y1+i][x1+j].move = nueva_matriz[i][j][0]
                    table[y1+i][x1+j].color = nueva_matriz[i][j][1]
                    table[y1+i][x1+j].valor= nueva_matriz[i][j][0]
        if (len(nueva_matriz) == 2 and len(nueva_matriz[0]) == 3)or (len(nueva_matriz) == 3 and len(nueva_matriz[0]) == 2):
            for i in range(len(nueva_matriz)):
                for j in range(len(nueva_matriz[0])):
                    try:
                        if table[y1+i][x1+j]:
                            table[y1+i][x1+j].move = nueva_matriz[i][j][0]
                            table[y1+i][x1+j].color = nueva_matriz[i][j][1]
                            table[y1+i][x1+j].valor= nueva_matriz[i][j][0]
                    
                    except Exception as e:
                        return None
                        # Manejo de excepciones
                        print(f"Ocurrió un error: {e}")
            print("paso por aqui")
        # Imprimir la matriz con la figura girada
        
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
        
    def fun_acople(table):
        filas = len(table)
        cols = len(table[0])
        for z in range(filas):
            if all(table[z][j].block == 1 for j in range(cols)):
                table.pop(z)  # Elimina la fila completa
                table.insert(0, [Posicion() for _ in range(cols)])  # Agrega una nueva fila vacía en la parte superior

        return table

                   
        
    fun_acople(table)
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


    pygame.draw.rect(screen, (255, 255, 255), (frame_x, frame_y, frame_width, frame_height), 2)#recatanguro del cuadro principal
    pygame.draw.rect(screen, "red", (player_pos.x - 20, player_pos.y - 20, 40, 40))#player
    # Dibujar líneas horizontales --
    
    for row in range(rows + 1):
        
        pygame.draw.line(screen, (255, 255, 255), (frame_x, (row * cell_size) + frame_y), (cols * cell_size + frame_x, row * cell_size + frame_y))
        
    # Dibujar líneas verticales |
    for col in range(cols + 1):
        
        pygame.draw.line(screen, (255, 255, 255), (frame_x + (col * cell_size), frame_y), ((col * cell_size) + frame_x,(rows * cell_size)+ frame_y))
        #table[].append(n)

    
    # Dibujar la tabla en la cuadrícula
    for row in range(rows_logicos):
        for col in range(cols):
            if table[row][col].valor == 1 :
                # Dibujar celda ocupada
                pygame.draw.rect(screen, (table[row][col].color), (frame_x + col * cell_size + 1, (frame_y-111) + row * cell_size + 1, cell_size - 2, cell_size - 2))
                
            else:
               # Dibujar celda libre
                pygame.draw.rect(screen, ("blue"), (frame_x + col * cell_size + 1, (frame_y-111) + row * cell_size + 1, cell_size - 2, cell_size - 2))
                

    pygame.display.flip()
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_s]:
        
        
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

        pygame.time.delay(DELAY)



    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
        i = 0
        for fila in table:
            e = 0
            for columna in fila:
                if table[i][e].move == 1:
                    if table[i][0] != 1:
                        valoractual = table[i][e].valor
                        valoranterior = table[i][e-1].valor
                        table[i][e-1].valor = valoractual
                        table[i][e].valor = valoranterior

                        moveactual = table[i][e].move
                        moveanterior = table[i][e-1].move
                        table[i][e-1].move = moveactual
                        table[i][e].move = moveanterior

                        coloractual = table[i][e].color
                        coloranterior = table[i][e-1].color
                        table[i][e-1].color = coloractual
                        table[i][e].color = coloranterior

                e += 1
            i += 1

    if keys[pygame.K_a]:
        
        
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

        pygame.time.delay(DELAY)


                


    if keys[pygame.K_d]:
        
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

        pygame.time.delay(DELAY)


        

        



        
    if keys[pygame.K_i]:
        fun_insertar(table,figura)
        pygame.time.delay(DELAY)
    if keys[pygame.K_j]:
        
        cordenadas=fun_encontrar_matris(table)
        fun_girar_figura(table,cordenadas)
        
        pygame.time.delay(DELAY)


    

    
    
    
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
