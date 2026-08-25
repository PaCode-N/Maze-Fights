from rich import print
import os
import readchar
import random
from random import randint

#Constants
JUAN_CARLOS = "Juan Carlos"
SAMUEL_DE_MARABEL = "Samuel de Marabel"
RORO_PORRO = "Roro Porro"
ENTER = "Por favor pulsa [bold]ENTER[/bold]"
BUG = "[bold]*[/bold]"
X = 0
Y = 1


#variables
enemy = 40
position = [0, 0]

#Beginning
os.system("cls")
game_title = "[bold]  Bienvenido a 💥💥Maze Fights💥💥  [/bold]"
print("\n\n\n" +game_title + "\n" + "-" * (len(game_title) -9) + "\n\n\n" +ENTER + " para comenzar:")
input()
os.system("cls")

#Story
print("Una tarde muy tranquila, decides ir a dar un paseo por tu huerta...")
input()
os.system("cls")
print("Giras la cabeza y DE REPENTE ves un bicho esponjoso y redondo frente a ti ❗")
input()
print(f"Bicho esponjoso: --{BUG} --")
input()
os.system("cls")
print("El bicho te pide que lo ayudes a defender su rancho con urgencia\n"
      "Ponle un nombre: ")
bug_name = input()
print(f"¡GENIAL! Ahora tú y [bold]{bug_name}[/bold] lucharán juntos contra el mal \n" + ENTER + "para empezar a ayudar a " + BUG)
input()


# Enemies function. This function will randomly select one of our enemies and then display the fight between our user and an enemy
def fight():
    initial_life = 100
    life = initial_life
    initial_enemy_life =100
    enemy_life = initial_enemy_life
    attack_1 = random.randint(15, 25)
    attack_2 = random.randint(25, 32)
    ultimate = random.randint(35, 40)

    enemies_list = [JUAN_CARLOS, SAMUEL_DE_MARABEL, RORO_PORRO] #this line chose a random enemy as oponent for our user
    enemy_selected = random.choice(enemies_list)
    enemy_selected_check = enemy_selected
    def random_attack(life, attack_dictionary):
        options = list(attack_dictionary.keys())  # list of our dictionary options
        if enemy_life > 10:  # This block chose one of our attacks depending on the life and subtract the random value to the user life
            probability = [3, 3, 1]  # probability to choose each power in the dictionary
            chosen_attack = random.choices(options, weights=probability, k=1)[
                0]
        else:
            probability = [1, 1, 3]  # probability to choose each power in the dictionary
            chosen_attack = random.choices(options, weights=probability, k=1)[
                0]  # choose a random option in the dictionary with more probabilities of choosing our ultimate

        attack_value = attack_dictionary[chosen_attack]  # this variable contains the value of the selected option
        life -= attack_value
        if life <= 0:
            life = 0
        return chosen_attack, attack_value, life

    def life_bar(life, enemy_life, current_life, in_turn, not_in_turn): #this function make our health state bar

        bar_filling = 25
        filling = "|"
        space = " "
        dash = "-"
        life_counter = int((life * bar_filling / initial_life))
        enemy_life_counter = int((enemy_life * bar_filling / initial_enemy_life))

        current_life_number = 0
        not_current_life = 0
        not_current_life_number = 0
        current_life_bar = 0
        if current_life == "Enemy":   #This condition check the life used in the current turn
            current_life_bar = life_counter
            current_life_number = life
            not_current_life =enemy_life_counter
            not_current_life_number = enemy_life
        elif current_life == "User":
            current_life_bar =enemy_life_counter
            current_life_number = enemy_life
            not_current_life = life_counter
            not_current_life_number = life


        health = (f"La vida de {not_in_turn} ha sido reducida a:  [{filling * current_life_bar}{space * (bar_filling - current_life_bar)}]{current_life_number} \n"
                  f"La vida de {in_turn} se mantiene en:       [{filling * not_current_life}{space * (bar_filling - not_current_life)}]{not_current_life_number} \n")

        print(health + dash * 100 + "\n")


    input(f"Te has cruzado con {enemy_selected} y no te dejará continuar hasta derrotarlo...")
    os.system("cls")
    while life > 0 and enemy_life > 0:
        in_turn = enemy_selected
        not_in_turn = bug_name
        current_life = "Enemy"

        if enemy_selected == JUAN_CARLOS:

            print(f"👿 No hay escapatoria chaval, si quieres continuar tu recorrido no tienes más opción que esquivar un par de hostias 👿\n\n"
                f"{JUAN_CARLOS} no te da espera con qué te atacara?\n\n"
                f"- Te mete un pulgar a la oreja? \n"
                f"- Te tira una cebolla al ojo?\n"
                f"- Se quita una media y te la tira al ojo\n\n"
                f"...\n\n")
            os.system("cls")

            attack_dictionary = {  # Dictionary of our random values related to the character powers
                "te mete un pulgar a la oreja": attack_1,
                "te tira una cebolla al ojo": attack_2,
                "Se quita una media y te la tira al ojo": ultimate
            }

            result_chosen_attack, result_attack_value, life = random_attack(life, attack_dictionary)

            input(f"{JUAN_CARLOS}, {result_chosen_attack} y te resta {result_attack_value} de vida\n"
                  f"...\n\n")

            life_bar(life, enemy_life, current_life, in_turn, not_in_turn)



        elif enemy_selected == SAMUEL_DE_MARABEL and enemy_life > 0:

            print("Como decía mi abuela, rápido, que las lentejas se enfrían\n\n")
            input(f"Con que te atacara {SAMUEL_DE_MARABEL}???\n"
                  f"- Te pinta de morado\n"
                  f"- PVP cúbico\n"
                  f"- Te deja la cara simétrica\n\n"
                  f"...\n\n")
            os.system("cls")

            attack_dictionary = {
                "te ha pintado de morado hasta los dientes": attack_1,
                "te reta a un PVP cúbico": attack_2,  # aca meter algo de aritmetica al cubo
                "te simetriza la cara": ultimate
            }

            result_chosen_attack, result_attack_value, life = random_attack(life, attack_dictionary)

            print(f"{SAMUEL_DE_MARABEL}, {result_chosen_attack} y te resta {result_attack_value} de vida\n"
                  f"Tu vida restante es: {life}\n\n")

            life_bar(life, enemy_life, current_life, in_turn, not_in_turn)



        elif enemy_selected == RORO_PORRO and enemy_life > 0:

            print("Acabo de escuchar que dijiste algo sobre Pablo?\n\n")
            input(f"{RORO_PORRO} está escuchando la petición de Pablo\n"
                  f"- A Pablo le apetece que te amarren en el sótano\n"
                  f"- Pablo quiere un Cake\n"
                  f"- Pablo quiere una silla nueva\n\n"
                  f"...\n\n")
            os.system("cls")

            attack_dictionary = {
                f"{RORO_PORRO} no duda y te amarra en el sótano": attack_1,
                f"{RORO_PORRO} te obliga a preparar una chantillí en contra de tu voluntad": attack_2,
                f"{RORO_PORRO} te convierte en un taburete": ultimate
            }

            result_chosen_attack, result_attack_value, life = random_attack(life, attack_dictionary)

            print(f"{RORO_PORRO}, {result_chosen_attack} y te resta {result_attack_value} de vida\n"
                  f"Tu vida restante es: {life}\n\n")

            life_bar(life, enemy_life, current_life, in_turn, not_in_turn)


        input(f"{ENTER} para comenzar tu turno")
        os.system("cls")

        # User turn
        in_turn = bug_name
        not_in_turn = enemy_selected
        current_life = "User"
        user_attack =input(f"🔴🔴 Es tu turno de defenderte {bug_name}, no dejes que {enemy_selected} te detenga 🔴🔴\n\n"
                           f"¿Cómo quieres defenderte de {enemy_selected}?\n"
                           f"A) Le tiras una ojota\n"
                           f"B) Le metes un pelotazo\n"
                           f"C) Le explicas una integral (le baja la vida de aburrimiento)\n\n"
                           f"Por favor escribe A, B o C para elegir: ")

        if user_attack.lower() == "a":
            enemy_life -= attack_1
        elif user_attack.lower() == "b":
            enemy_life -= attack_2
        elif user_attack.lower() == "c":
            enemy_life -= ultimate

        life_bar(life, enemy_life, current_life, in_turn, not_in_turn)
        os.system("cls")


# Mejora la redaccion de los personajes, sus ataques y cuando limpiar pantalla durante los combates
# revisa si el final funciona
#Hay que igualar las vidas a 0 si pasan a negativos y poner que ataque realiza cada personaje

    #MAP
game_map = ("""\
     ###################################
##                #######     ########## 
#####    ######       ######        ####
#####   ##    ######    ###      #######
##                #####      ####    ###
#     #######      ########        #####
###    ###       ######   ####      ####
##               ####      #####   ##  #
###    #####           ##     ###      #
###          #####     #####         ###
####      #####     ###        ####   ##
####   #####              ########    ##
#               #####    ##       ######
####      ###    #####      ####       #
####################################    \
""")

#map divided to can work in X and Y
map_split = [list(row) for row in game_map.split("\n")]
width = len(map_split[X]) #Inverted coordinates because we split the map in the coordinate X and the original access to our array is Y
height = len(map_split)

#enemies position
enemies = []
while len(enemies) != enemy:
    enemies_x = random.randint(0, width-1) #it generates random coordinate lists in any position inside the map
    enemies_y = random.randint(0, height-1)
    enemies_coordinates = enemies_x, enemies_y
    #found = False
    if map_split[enemies_y][enemies_x] != "#" and enemies_coordinates != position and enemies_coordinates not in enemies:
        enemies.append(enemies_coordinates) #This adds the random coordinate of an enemy in our enemies list if it's a new value, not our user coordinates or a wall

#Printing map, map obstacles, user and enemies
while enemy > 0 or position == [14, 39]:
    print("+" + "-" * width * 2 + "+") #Upper edge
    for y_map in range(height):
        print("|", end = "") # Left edge

        for x_map in range(width): #Default content of our map
            points = " "

            for enemies_position in enemies: #This print the enemies in the map
                if enemies_position[Y] == y_map and enemies_position[X] == x_map:
                    points = "o"

            if map_split[y_map] [x_map] == "#": #This check our map to print our walls
                points = "#"

            elif y_map == position[Y] and x_map == position[X]: #This print the user
                points = BUG


            print(f"{points} ", end = "") #Thid line print useful information for the user

        print("|") # Right edge
    print("+" + "-" * width * 2 + "+") #Bottom edge


    if tuple(position) in enemies: #This line deletes the enemies points of our tuple when our user steps on it
        enemies.remove(tuple(position))
        os.system("cls")
        fight()

    # user movement input
    direction = readchar.readchar()
    if direction == "w":
        position[Y] -= 1
        if map_split[position[Y]][position[X]] == "#":
            position[Y] += 1

    elif direction == "s":
        position[Y] += 1
        if map_split[position[Y]][position[X]] == "#":
            position[Y] -= 1

    elif direction == "a":
        position[X] -= 1
        if map_split[position[Y]][position[X]] == "#":
            position[X] += 1

    elif direction == "d":
        position[X] += 1
        if map_split[position[Y]][position[X]] == "#":
            position[X] -= 1

    elif direction == "q":
        exit()
    os.system("cls")

input(f"¡FELICIDADES! Has logrado salir del laberinto y has ayudado a {bug_name} a salir de ese horrible lugar\n"
      f"""   
                                   .     .     .  
                                . '.   .   . '.  .
                                 .   . '.    .   .  
                                .   .   . '.     .
                              *     .     .     .    *
                              .   '.     . '.   .    .
                                .   .    .   .    .  
                                .  '.   .   . '.  .
                                    *     .    *
                                    
Ya puedes seguir con lo que sea que estuvieses haciendo""")


# Cosas rotas:
# No se muestra el daño que hacemos al atacar al enemigo
# Algunos [Bold] no estan funcionando
# Al llegar a la salida del juego bota un error en vez de mostrar el mensaje de victoria
# Los poderes no estan equilibrados, el unico con el que podemos meter mucho daño es con la C. Estaria guapo meter una suma o algo por el estilo, con un timer o asi
# Si el enemigo gana la pelea, no se me esta reiniciando el juego desde el inicio, sino que me regresa a donde estaba
# Hacer anotaciones en el codigo de que hace cada cosa
# Le podrias meter idiomas
