import pygame

'''COSE DA AGGIUNGERE
*VITTORIA
'''
pygame.init()
''' INIZIO SPAZIO DEDICATO A VARIABILI GLOBALI'''
clock = pygame.time.Clock()
dim = (1000, 800)  # dimensioni gioco (risoluzione)
schermo = pygame.display.set_mode(dim)
pygame.display.set_caption("Escape X")  # titolo
velocita = 4
velocita_mostro = 2
punteggio_temp = 0
punteggio = 0
morti = 0
frame = 0
speed_frame = 6  # (velocità animazione sprite personaggio)
mura = []
mostri = []
# dimensioni
dim = 44  # spessore mura
dim_pg = 30  # dimensioni personaggio
# global tempo
tempo = 0
tempo_limite = 30
tempo_effettivo = tempo_limite
# var pressione tasti
m_su = False
m_sx = False
m_giu = False
m_dx = False
spazio = False
# colori
nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)
# font
font = pygame.font.SysFont("calibri", 45)
font_rip = pygame.font.SysFont("freesansbold.ttf", 60, True)
font_rip_c = pygame.font.SysFont("freesansbold.ttf", 65, True)
font_rip_piccolo = pygame.font.SysFont("freesansbold.ttf", 45, True)

# label_sconfitta = font_rip.render("Sei morto, hai colpito un muro.", 1, (0,0,0))
label_ricomincia = font_rip.render("Clicca SPAZIO per ricominciare.", True, (0, 0, 0))
# label_tempo = font_rip.render(str(tempo), 1, (0,0,0))
# label_chiavi = font.render("Chiavi:")
# print(pygame.font.get_fonts())
# livello 1
livello_giocato = 0
livelli = []
# livelli_mod = []
'''
LEGENDA
W = Wall/Muro
E = Exit/Uscita
K = Key/Chiave
I = Invisible/Muro invisibile
P = Porta/Porta
H = Horizontal/Mostro che si muove in orizzontale
V = Vertical/  Mostro che si muove in verticale
1 = Stellina livello 1, 50 punti
2 = Stellina livello 2, 500 punti
'''
'''
livello=[
'''
livello = [  # 1
    "WWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWW",
    "WW 1         2 HWW",
    "WW              WW",
    "WWH           1 WW",
    "WW             EWW",
    "WW             HWW",
    "WW1             WW",
    "WW              WW",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 2
    "WWWWWWWWWWWWWWWWWW",
    "W    EE         EW",
    "W   EE       E  2W",
    "WWWWWWWWPPWWWWWWWW",
    "W 1              W",
    "W       KK       W",
    "W           1    W",
    "WH      WW      HW",
    "W  1             W",
    "W               1W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 3
    "WWWWWWWWWWWWWWWWWW",
    "WE               W",
    "WWWWWWWWPPWWWWWWWW",
    "W   K           1W",
    "W        H       W",
    "W1               W",
    "WWWWWWWWPPWWWWWWWW",
    "W   K           1W",
    "W        H     V W",
    "W               2W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 4
    "WWWWWWWWWWWWWWWWWW",
    "W    K      K  V W",
    "W    WWWPPWWW   1W",
    "W 1  W V   VW    W",
    "W    W      W1   W",
    "W    W  EEEEW  2 W",
    "W    W     2W   1W",
    "W    WWWWWWWW  V W",
    "W                W",
    "W                W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 5
    "WWWWWWWWWWWWWWWWWW",
    "W   P    1    P  W",
    "W   W         W  W",
    "W V  W   H   W V W",
    "W1    W     W   1W",
    "W  K   W   W  K  W",
    "W      W   W     W",
    "WPWWWWWW   WWWWWPW",
    "W  H  2W K W2 H  W",
    "W     EW   WE    W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 6
    "WWWWWWWWWWWWWWWWWW",
    "W 2 W           1W",
    "WWPWWH           W",
    "W   W  WWWWWWW   W",
    "WH  W  W1KKKKW   W",
    "W   P    KKK1W   W",
    "WWPWWWWWWWWWWW   W",
    "W     1W         W",
    "WH     W   WWWWWWW",
    "W     EW   WH   HW",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 7
    "WWWWWWWWWWWWWWWWWW",
    "W1   P      P    W",
    "W    W  EE 2W    W",
    "WH   WWWWWWWW   HW",
    "W    WK  1 KW    W",
    "W    W      W    W",
    "WH      WW      HW",
    "W                W",
    "W      HWWH      W",
    "W1               W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 8
    "WWWWWWWWWWWWWWWWWW",
    "W2  WE  H    W1K1W",
    "W   W   P   HW K W",
    "WH  WWWWPWWWWW  HW",
    "W   W       1W   W",
    "WH  W        W   W",
    "W   WWWWPWWWWW   W",
    "W               HW",
    "WWWWWWW          W",
    "W1KK  P         KW",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 9
    "WWWWWWWWWWWWWWWWWW",
    "W  1 H   K  H    W",
    "W               HW",
    "WH   WWWWPWWWW  HW",
    "W    W   P   W 1 W",
    "W V HW       WHV W",
    "W    W2  E   WK  W",
    "WH  WWWWWWWWWWW HW",
    "W    W      W P  W",
    "W1 W   W  W   W  W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)
livello = [  # 10
    "WWWWWWWWWWWWWWWWWW",
    "WK  P   H    P   W",
    "W   W1H     KW  KW",
    "WPWWWWWWWWWWWWPWWW",
    "W  1W2 V   V W  1W",
    "W   W        P   W",
    "W  KWE   V   W  KW",
    "WWPWWWWWWWWWWWWWWW",
    "W  HP           1W",
    "WK  W          HKW",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
livelli.append(livello)


# inizializzo immagini

# sprite personaggio
c_idle_1_dx = pygame.image.load('immagini/Personaggio/Idle/Idle_11.png').convert_alpha()
c_idle_2_dx = pygame.image.load('immagini/Personaggio/Idle/Idle_12.png').convert_alpha()
c_idle_3_dx = pygame.image.load('immagini/Personaggio/Idle/Idle_13.png').convert_alpha()
c_idle_4_dx = pygame.image.load('immagini/Personaggio/Idle/Idle_14.png').convert_alpha()
c_run_1_dx = pygame.image.load('immagini/Personaggio/Run/Run_11.png').convert_alpha()
c_run_2_dx = pygame.image.load('immagini/Personaggio/Run/Run_12.png').convert_alpha()
c_run_3_dx = pygame.image.load('immagini/Personaggio/Run/Run_13.png').convert_alpha()
c_run_4_dx = pygame.image.load('immagini/Personaggio/Run/Run_14.png').convert_alpha()
c_run_5_dx = pygame.image.load('immagini/Personaggio/Run/Run_15.png').convert_alpha()
c_run_6_dx = pygame.image.load('immagini/Personaggio/Run/Run_16.png').convert_alpha()
c_run_7_dx = pygame.image.load('immagini/Personaggio/Run/Run_17.png').convert_alpha()
c_run_8_dx = pygame.image.load('immagini/Personaggio/Run/Run_18.png').convert_alpha()

# trasformazione sprite
c_idle_1_dx = pygame.transform.scale(c_idle_1_dx, (dim_pg + 5, dim_pg + 5))
c_idle_2_dx = pygame.transform.scale(c_idle_2_dx, (dim_pg + 5, dim_pg + 5))
c_idle_3_dx = pygame.transform.scale(c_idle_3_dx, (dim_pg + 5, dim_pg + 5))
c_idle_4_dx = pygame.transform.scale(c_idle_4_dx, (dim_pg + 5, dim_pg + 5))
c_run_1_dx = pygame.transform.scale(c_run_1_dx, (dim_pg + 5, dim_pg + 5))
c_run_2_dx = pygame.transform.scale(c_run_2_dx, (dim_pg + 5, dim_pg + 5))
c_run_3_dx = pygame.transform.scale(c_run_3_dx, (dim_pg + 5, dim_pg + 5))
c_run_4_dx = pygame.transform.scale(c_run_4_dx, (dim_pg + 5, dim_pg + 5))
c_run_5_dx = pygame.transform.scale(c_run_5_dx, (dim_pg + 5, dim_pg + 5))
c_run_6_dx = pygame.transform.scale(c_run_6_dx, (dim_pg + 5, dim_pg + 5))
c_run_7_dx = pygame.transform.scale(c_run_7_dx, (dim_pg + 5, dim_pg + 5))
c_run_8_dx = pygame.transform.scale(c_run_8_dx, (dim_pg + 5, dim_pg + 5))

c_idle_1_sx = pygame.transform.flip(c_idle_1_dx, True, False)
c_idle_2_sx = pygame.transform.flip(c_idle_2_dx, True, False)
c_idle_3_sx = pygame.transform.flip(c_idle_3_dx, True, False)
c_idle_4_sx = pygame.transform.flip(c_idle_4_dx, True, False)
c_run_1_sx = pygame.transform.flip(c_run_1_dx, True, False)
c_run_2_sx = pygame.transform.flip(c_run_2_dx, True, False)
c_run_3_sx = pygame.transform.flip(c_run_3_dx, True, False)
c_run_4_sx = pygame.transform.flip(c_run_4_dx, True, False)
c_run_5_sx = pygame.transform.flip(c_run_5_dx, True, False)
c_run_6_sx = pygame.transform.flip(c_run_6_dx, True, False)
c_run_7_sx = pygame.transform.flip(c_run_7_dx, True, False)
c_run_8_sx = pygame.transform.flip(c_run_8_dx, True, False)

c_idle_dx = [c_idle_1_dx, c_idle_2_dx, c_idle_3_dx, c_idle_4_dx]
# c_idle_dx.append(c_idle_1_dx)
# c_idle_dx.append(c_idle_2_dx)
# c_idle_dx.append(c_idle_3_dx)
# c_idle_dx.append(c_idle_4_dx)

c_idle_sx = [c_idle_1_sx, c_idle_2_sx, c_idle_3_sx, c_idle_4_sx]
# c_idle_sx.append(c_idle_1_sx)
# c_idle_sx.append(c_idle_2_sx)
# c_idle_sx.append(c_idle_3_sx)
# c_idle_sx.append(c_idle_4_sx)

c_run_dx = [c_run_1_dx, c_run_2_dx, c_run_3_dx, c_run_4_dx, c_run_5_dx, c_run_6_dx, c_run_7_dx, c_run_8_dx]
# c_run_dx.append(c_run_1_dx)
# c_run_dx.append(c_run_2_dx)
# c_run_dx.append(c_run_3_dx)
# c_run_dx.append(c_run_4_dx)
# c_run_dx.append(c_run_5_dx)
# c_run_dx.append(c_run_6_dx)
# c_run_dx.append(c_run_7_dx)
# c_run_dx.append(c_run_8_dx)

c_run_sx = [c_run_1_sx, c_run_2_sx, c_run_3_sx, c_run_4_sx, c_run_5_sx, c_run_6_sx, c_run_7_sx, c_run_8_sx]
# c_run_sx.append(c_run_1_sx)
# c_run_sx.append(c_run_2_sx)
# c_run_sx.append(c_run_3_sx)
# c_run_sx.append(c_run_4_sx)
# c_run_sx.append(c_run_5_sx)
# c_run_sx.append(c_run_6_sx)
# c_run_sx.append(c_run_7_sx)
# c_run_sx.append(c_run_8_sx)


# mostri

slime_bot1_run = pygame.image.load('immagini/sprite_slime/SlimeBot1R.png').convert_alpha()
slime_bot2_run = pygame.image.load('immagini/sprite_slime/SlimeBot2R.png').convert_alpha()
slime_bot3_run = pygame.image.load('immagini/sprite_slime/SlimeBot3R.png').convert_alpha()
slime_bot4_run = pygame.image.load('immagini/sprite_slime/SlimeBot4R.png').convert_alpha()
slime_top1_run = pygame.image.load('immagini/sprite_slime/SlimeTop1R.png').convert_alpha()
slime_top2_run = pygame.image.load('immagini/sprite_slime/SlimeTop2R.png').convert_alpha()
slime_top3_run = pygame.image.load('immagini/sprite_slime/SlimeTop3R.png').convert_alpha()
slime_top4_run = pygame.image.load('immagini/sprite_slime/SlimeTop4R.png').convert_alpha()
slime_dx1_run = pygame.image.load('immagini/sprite_slime/SlimeDx1R.png').convert_alpha()
slime_dx2_run = pygame.image.load('immagini/sprite_slime/SlimeDx2R.png').convert_alpha()
slime_dx3_run = pygame.image.load('immagini/sprite_slime/SlimeDx3R.png').convert_alpha()
slime_dx4_run = pygame.image.load('immagini/sprite_slime/SlimeDx4R.png').convert_alpha()
slime_sx1_run = pygame.image.load('immagini/sprite_slime/SlimeSx1R.png').convert_alpha()
slime_sx2_run = pygame.image.load('immagini/sprite_slime/SlimeSx2R.png').convert_alpha()
slime_sx3_run = pygame.image.load('immagini/sprite_slime/SlimeSx3R.png').convert_alpha()
slime_sx4_run = pygame.image.load('immagini/sprite_slime/SlimeSx4R.png').convert_alpha()

# slime_bot1_run = pygame.transform.scale(slime_bot1_run, (dim_pg+25, dim_pg+25))

slime_bot_run = [slime_bot1_run, slime_bot2_run, slime_bot3_run, slime_bot4_run]
slime_top_run = [slime_top1_run, slime_top2_run, slime_top3_run, slime_top4_run]
slime_dx_run = [slime_dx1_run, slime_dx2_run, slime_dx3_run, slime_dx4_run]
slime_sx_run = [slime_sx1_run, slime_sx2_run, slime_sx3_run, slime_sx4_run]

# trasformazione mostri
for i in range(len(slime_bot_run)):
    slime_bot_run[i] = pygame.transform.scale(slime_bot_run[i], (dim_pg + 10, dim_pg))
for i in range(len(slime_top_run)):
    slime_top_run[i] = pygame.transform.scale(slime_top_run[i], (dim_pg + 10, dim_pg))
for i in range(len(slime_dx_run)):
    slime_dx_run[i] = pygame.transform.scale(slime_dx_run[i], (dim_pg + 10, dim_pg))
for i in range(len(slime_sx_run)):
    slime_sx_run[i] = pygame.transform.scale(slime_sx_run[i], (dim_pg + 10, dim_pg))

sfondo_red = pygame.image.load('immagini/Sfondi/sfondo_redchiaro.png').convert()
sfondo_red = pygame.transform.scale(sfondo_red, (930, 200))
cornice2 = pygame.image.load('immagini/Sfondi/cornice2.png').convert_alpha()
cornice2 = pygame.transform.scale(cornice2, (1500, 750))
sfondo_game1 = pygame.image.load('immagini/Sfondi/brick_verde.png').convert()
sfondo_game1 = pygame.transform.scale(sfondo_game1, (800, 500))
brick_imm = pygame.image.load('immagini/Muro/muroFulmine.png').convert()
brick_imm = pygame.transform.scale(brick_imm, (dim, dim))
brick_porta_imm = pygame.image.load('immagini/Muro/Porta.png').convert()
brick_porta_imm = pygame.transform.scale(brick_porta_imm, (dim, dim))
porta_aperta_imm = pygame.image.load('immagini/Muro/PortaAperta.png').convert()
porta_aperta_imm = pygame.transform.scale(porta_aperta_imm, (dim, dim))
chiave_imm = pygame.image.load('immagini/Muro/chiave.png').convert_alpha()
chiave_imm = pygame.transform.scale(chiave_imm, (dim, dim))
trapdoor_imm = pygame.image.load('immagini/Muro/trapdoor.png').convert()  # _alpha()
trapdoor_imm = pygame.transform.scale(trapdoor_imm, (dim, dim))
stellaGialla_imm = pygame.image.load('immagini/Muro/StellaGialla.png').convert_alpha()
stellaGialla_imm = pygame.transform.scale(stellaGialla_imm, (dim, dim))
stellaGrigia_imm = pygame.image.load('immagini/Muro/StellaGrigia.png').convert_alpha()
stellaGrigia_imm = pygame.transform.scale(stellaGrigia_imm, (dim, dim))
skull = pygame.image.load('immagini/Sfondi/skull.png').convert_alpha()
skull = pygame.transform.scale(skull, (dim, dim))
I    = pygame.image.load('immagini/Icone/I.png').convert_alpha()
I =  pygame.transform.scale(I, (dim, dim))
II   = pygame.image.load('immagini/Icone/II.png').convert_alpha()
II =  pygame.transform.scale(II, (dim, dim))
III  = pygame.image.load('immagini/Icone/III.png').convert_alpha()
III =  pygame.transform.scale(III, (dim, dim))
IV   = pygame.image.load('immagini/Icone/IV.png').convert_alpha()
IV=  pygame.transform.scale(IV, (dim, dim))
V    = pygame.image.load('immagini/Icone/V.png').convert_alpha()
V =  pygame.transform.scale(V, (dim, dim))
VI   = pygame.image.load('immagini/Icone/VI.png').convert_alpha()
VI =  pygame.transform.scale(VI, (dim, dim))
VII  = pygame.image.load('immagini/Icone/VII.png').convert_alpha()
VII =  pygame.transform.scale(VII, (dim, dim))
VIII = pygame.image.load('immagini/Icone/VIII.png').convert_alpha()
VIII =  pygame.transform.scale(VIII, (dim, dim))
IX   = pygame.image.load('immagini/Icone/IX.png').convert_alpha()
IX=  pygame.transform.scale(IX, (dim, dim))
X    = pygame.image.load('immagini/Icone/X.png').convert_alpha()
X =  pygame.transform.scale(X, (dim, dim))
icone = [I,II,III,IV,V,VI,VII,VIII,IX,X]
# inizializzo suoni
porta = pygame.mixer.Sound('suoni/porta.mp3')
chiave = pygame.mixer.Sound('suoni/chiave.mp3')
tunnel = pygame.mixer.Sound('suoni/tunnel.mp3')
morto = pygame.mixer.Sound('suoni/morto.mp3')
ok = pygame.mixer.Sound('suoni/ok.mp3')
stella = pygame.mixer.Sound('suoni/Stella.mp3')
pygame.mixer.music.load('suoni/Bicycle.mp3')
''' FINE SPAZIO DEDICATO A VARIABILI GLOBALI'''

''' INIZIO SPAZIO DEDICATO A DICHIARAZIONE FUNZIONI E CLASSI'''


# classe timer
# classe muro
class Muro:
    def __init__(self, posizione, tipo):  # posizione è una tupla (x,y), tipo è un carattere (K = Key, W = wall ecc.)
        mura.append(self)
        self.rect = pygame.Rect(posizione[0], posizione[1], dim, dim)
        self.tipo = tipo
        self.aperto = False
        self.preso = False


class Mostro:
    def __init__(self, posizione, tipo):
        mostri.append(self)
        self.rect = pygame.Rect(posizione[0], posizione[1], dim, dim)
        self.tipo = tipo
        self.velocita_mostro = velocita_mostro
        if tipo == 'V':
            self.orientamento = 'bot'
        elif tipo == 'H':
            self.orientamento = 'dx'

    def muovi_mostro(self):
        # muovo il mostro
        if self.tipo == 'V':
            self.rect.y += self.velocita_mostro
        elif self.tipo == 'H':
            self.rect.x += self.velocita_mostro
        # controllo che collida con un muro, in tal caso inverto la sua velocità
        for muro in mura:
            if self.rect.colliderect(muro.rect):
                if muro.tipo == 'W' or (muro.tipo == 'P' and not muro.aperto) or (muro.tipo == '1' and not muro.preso) or (muro.tipo == '2' and not muro.preso) or muro.tipo == 'E' or (muro.tipo == 'K' and not muro.preso):
                    self.cambia_velocita()
        # controllo hitbox giocatore mostro, se collidono chiamo sconfitta
        if self.rect.colliderect(giocatore.rect):
            sconfitta('mostro')

    def cambia_velocita(self):
        self.velocita_mostro = -self.velocita_mostro
        # cambia l'orientamento (serve per la texture)
        if self.orientamento == 'bot':
            self.orientamento = 'top'
        elif self.orientamento == 'top':
            self.orientamento = 'bot'
        elif self.orientamento == 'dx':
            self.orientamento = 'sx'
        elif self.orientamento == 'sx':
            self.orientamento = 'dx'

    def get_orientamento(self):
        return self.orientamento


# classe giocatore
class Giocatore:
    def __init__(self):
        # Dalla documentazione ufficiale un rect ha i parametri:
        # Rect(left, top, width, height)
        # quindi  (x,y,spessore,altezza)
        self.rect = pygame.Rect(490, 620, dim_pg + 10, dim_pg)  # dim_pg+10,dim_pg
        self.orientamento = 'dx'
        # self.imm_personaggio = imm_personaggio_dx
        self.chiavi = 0
        self.stato = 'idle'

    def get_orientamento(self):
        return self.orientamento

    def get_stato(self):
        return self.stato

    def cambia_orientamento(self, orient):
        if self.orientamento == 'sx' and orient == 'dx':
            self.orientamento = 'dx'
            # self.imm_personaggio = imm_personaggio_dx
        elif self.orientamento == 'dx' and orient == 'sx':
            self.orientamento = 'sx'
            # self.imm_personaggio = imm_personaggio_sx

    def muovi(self, x, y):
        if x != 0:
            self.muovi_ascissa(x, y)
        if y != 0:
            self.muovi_ascissa(x, y)

    def muovi_ascissa(self, x, y):  # per un movimento più fluido ne muovo una alla volta
        global punteggio
        self.stato = 'run'
        self.rect.x += x * velocita
        self.rect.y += y * velocita
        for muro in mura:
            if self.rect.colliderect(muro.rect):
                if muro.tipo == 'W' or muro.tipo == 'I':
                    sconfitta('muro')
                    pygame.event.clear()
                elif muro.tipo == 'P':
                    if not muro.aperto:
                        if self.chiavi < 1:
                            sconfitta('porta')
                            pygame.event.clear()
                        else:
                            self.chiavi -= 1
                            pygame.mixer.Sound.play(porta)
                            muro.aperto = True
                            #  global punteggio
                            punteggio += 25
                elif muro.tipo == 'K':
                    if not muro.preso:
                        pygame.mixer.Sound.play(chiave)
                        self.chiavi += 1
                        muro.preso = True
                elif muro.tipo == 'E':
                    aggiungi_punti()
                    prossimo_livello()
                    pygame.mixer.Sound.play(tunnel)
                elif muro.tipo == '1' and not muro.preso:
                    muro.preso = True
                    punteggio += 50
                    pygame.mixer.Sound.play(stella)
                elif muro.tipo == '2' and not muro.preso:
                    muro.preso = True
                    punteggio += 500
                    pygame.mixer.Sound.play(stella)


def aggiorna():
    schermo.fill(blu)
    ### Contatore chiavi a schermo
    if giocatore.chiavi > 0:
        vuoto = ''
    else:
        vuoto = '0'
    label_chiavi = font.render("Chiavi:" + vuoto, True, (255, 255, 0))
    x = 30
    y = 750
    schermo.blit(label_chiavi, (x, y))
    x += 125
    if giocatore.chiavi < 5:
        for _ in range(giocatore.chiavi):
            schermo.blit(chiave_imm, (x, y))
            x += 50
    else:
        schermo.blit(chiave_imm, (x, y))
        label_chiavi = font.render('    X' + str(giocatore.chiavi), True, (255, 255, 0))
        schermo.blit(label_chiavi, (x + 10, y))
    ### Contatore punteggio a schermo
    label_punteggio = font.render("Punteggio : " + str(punteggio).rjust(5, '0'), True, (255, 255, 0))
    schermo.blit(label_punteggio, (360, 50))
    K=186
    schermo.blit(icone[livello_giocato],(500-K,50))
    schermo.blit(icone[livello_giocato],(500+K,50))
    ### Contatore Morti
    label_morti = font.render("Morti : " + str(morti).rjust(2, '0'), True, (255, 255, 0))  # .rjust(2,'0')
    schermo.blit(label_morti, (432, 10))
    K=115
    schermo.blit(skull,(500-K,8))
    schermo.blit(skull,(500+K,8))
    ### Scritta gioco
    label_game_contorno = font_rip_c.render("Escape X", True, (0, 0, 0))
    schermo.blit(label_game_contorno,(750+5,750+2))
    label_game = font_rip.render("Escape X", True, (255, 255, 0))
    schermo.blit(label_game,(750,750))
    ### Sfondo gioco
    schermo.blit(sfondo_game1, (100, 200))
    ### Texture mura
    for muro in mura:
        if muro.tipo == 'W':
            schermo.blit(brick_imm, muro.rect)
        elif muro.tipo == 'P' and not muro.aperto:
            if not giocatore.chiavi:
                schermo.blit(brick_porta_imm, muro.rect)
            else:
                schermo.blit(porta_aperta_imm, muro.rect)
        elif muro.tipo == 'K' and not muro.preso:
            schermo.blit(chiave_imm, muro.rect)
        elif muro.tipo == 'E':
            schermo.blit(trapdoor_imm, muro.rect)
        elif muro.tipo == '1' and not muro.preso:
            schermo.blit(stellaGrigia_imm, muro.rect)
        elif muro.tipo == '2' and not muro.preso:
            schermo.blit(stellaGialla_imm, muro.rect)
    ### Texture mostri
    for mostro in mostri:
        orient_mostro = mostro.get_orientamento()
        if orient_mostro == 'bot':
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(slime_bot_run[0], mostro.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(slime_bot_run[1], mostro.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(slime_bot_run[2], mostro.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(slime_bot_run[3], mostro.rect)
        elif orient_mostro == 'top':
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(slime_top_run[0], mostro.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(slime_top_run[1], mostro.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(slime_top_run[2], mostro.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(slime_top_run[3], mostro.rect)
        elif orient_mostro == 'dx':
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(slime_dx_run[0], mostro.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(slime_dx_run[1], mostro.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(slime_dx_run[2], mostro.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(slime_dx_run[3], mostro.rect)
        elif orient_mostro == 'sx':
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(slime_sx_run[0], mostro.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(slime_sx_run[1], mostro.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(slime_sx_run[2], mostro.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(slime_sx_run[3], mostro.rect)
        # schermo.blit(slime_bot_run[0],mostro.rect)
    ### Tempo
    sfondo_timer_rect = pygame.Rect(250, 100, 500, 75)  # 210,100,600,75
    schermo.fill(rosso, sfondo_timer_rect)
    timer_rect = pygame.Rect(250, 100, 500 - (tempo * (500 // tempo_limite)), 75)
    schermo.fill(verde, timer_rect)
    ### Cornice gioco
    schermo.blit(cornice2, (-250, -6))
    ### Texture personaggio
    orientamento = giocatore.get_orientamento()
    stato_giocatore = giocatore.get_stato()
    if stato_giocatore == 'idle':
        if orientamento == 'dx':
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(c_idle_dx[0], giocatore.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(c_idle_dx[1], giocatore.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(c_idle_dx[2], giocatore.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(c_idle_dx[3], giocatore.rect)
        else:
            if 0 <= frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(c_idle_sx[0], giocatore.rect)
            elif 1 * speed_frame <= frame % (4 * speed_frame) < 2 * speed_frame:
                schermo.blit(c_idle_sx[1], giocatore.rect)
            elif 2 * speed_frame <= frame % (4 * speed_frame) < 3 * speed_frame:
                schermo.blit(c_idle_sx[2], giocatore.rect)
            elif 3 * speed_frame <= frame % (4 * speed_frame) < 4 * speed_frame:
                schermo.blit(c_idle_sx[3], giocatore.rect)
    else:
        if orientamento == 'dx':
            if frame % (8 * speed_frame) >= 0 and frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(c_run_dx[0], giocatore.rect)
            elif 1 * speed_frame <= frame % (8 * speed_frame) < 2 * speed_frame:
                schermo.blit(c_run_dx[1], giocatore.rect)
            elif 2 * speed_frame <= frame % (8 * speed_frame) < 3 * speed_frame:
                schermo.blit(c_run_dx[2], giocatore.rect)
            elif 3 * speed_frame <= frame % (8 * speed_frame) < 4 * speed_frame:
                schermo.blit(c_run_dx[3], giocatore.rect)
            elif 4 * speed_frame <= frame % (8 * speed_frame) < 5 * speed_frame:
                schermo.blit(c_run_dx[4], giocatore.rect)
            elif 5 * speed_frame <= frame % (8 * speed_frame) < 6 * speed_frame:
                schermo.blit(c_run_dx[5], giocatore.rect)
            elif 6 * speed_frame <= frame % (8 * speed_frame) < 7 * speed_frame:
                schermo.blit(c_run_dx[6], giocatore.rect)
            elif 7 * speed_frame <= frame % (8 * speed_frame) < 8 * speed_frame:
                schermo.blit(c_run_dx[7], giocatore.rect)
        else:
            if frame % (8 * speed_frame) >= 0 and frame % (4 * speed_frame) < 1 * speed_frame:
                schermo.blit(c_run_sx[0], giocatore.rect)
            elif 1 * speed_frame <= frame % (8 * speed_frame) < 2 * speed_frame:
                schermo.blit(c_run_sx[1], giocatore.rect)
            elif 2 * speed_frame <= frame % (8 * speed_frame) < 3 * speed_frame:
                schermo.blit(c_run_sx[2], giocatore.rect)
            elif 3 * speed_frame <= frame % (8 * speed_frame) < 4 * speed_frame:
                schermo.blit(c_run_sx[3], giocatore.rect)
            elif 4 * speed_frame <= frame % (8 * speed_frame) < 5 * speed_frame:
                schermo.blit(c_run_sx[4], giocatore.rect)
            elif 5 * speed_frame <= frame % (8 * speed_frame) < 6 * speed_frame:
                schermo.blit(c_run_sx[5], giocatore.rect)
            elif 6 * speed_frame <= frame % (8 * speed_frame) < 7 * speed_frame:
                schermo.blit(c_run_sx[6], giocatore.rect)
            elif 7 * speed_frame <= frame % (8 * speed_frame) < 8 * speed_frame:
                schermo.blit(c_run_sx[7], giocatore.rect)

    # schermo.blit(giocatore.imm_personaggio,giocatore.rect)# (vecchio sprite, senza animazione)
    ### Refresh dello schermo
    pygame.display.update()
    


def muovi(g):  # ,m_su,m_sx,m_giu,m_dx,spazio
    if m_su:
        g.muovi(0, -1)
    if m_sx:
        if g.orientamento == 'dx':  # serve a specchiare il personaggio quando cambia direzione
            g.cambia_orientamento('sx')
        g.muovi(-1, 0)
    if m_giu:
        g.muovi(0, 1)
    if m_dx:
        if g.orientamento == 'sx':
            g.cambia_orientamento('dx')
        g.muovi(1, 0)
    if not m_su and not m_sx and not m_giu and not m_dx:
        g.stato = 'idle'


def muovi_mostri():
    for mostro in mostri:
        mostro.muovi_mostro()


def inizializza_mura(liv):
    x = 108
    y = 220
    for riga in liv:
        for elem in riga:
            if elem != ' ':
                if elem != 'H' and elem != 'V':
                    Muro((x, y), elem)  # tramite elem passo il tipo di muro (porta con lucchetto o muro)
                else:
                    Mostro((x, y), elem)
            x += dim
        y += dim
        x = 108


def inizializza_tempo():
    global tempo
    tempo = 0


def inizio():
    inizializza_mura(livelli[livello_giocato])
    # pygame.time.delay(10000)#
    inizializza_tempo()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    # pygame.mixer.Sound.play(ok)
    ok.play(fade_ms=1000)
    ok.fadeout(2000)
    # pygame.mixer.Sound.fadeout(ok)
    pygame.mixer.music.play(-1, fade_ms=1000)
    pygame.mixer.music.set_volume(0.1)


def sconfitta(morte):
    global morti
    global punteggio
    global punteggio_temp
    if morte == 'muro':
        label_sconfitta = font_rip.render("Sei morto, hai colpito un muro.", True, (0, 0, 0))
    elif morte == 'tempo':
        label_sconfitta = font_rip.render("Sei morto, è finito il tempo.", True, (0, 0, 0))
    elif morte == 'porta':
        label_sconfitta = font_rip_piccolo.render("Sei morto, hai colpito una porta (senza chiave)", True, (0, 0, 0))
    elif morte == 'mostro':
        label_sconfitta = font_rip_piccolo.render("Sei morto, un mostro ti ha mangiato.", True, (0, 0, 0))
    else:
        label_sconfitta = font_rip_piccolo.render("Sei morto.", True, (0, 0, 0))
    morti += 1
    punteggio -= 100
    punteggio_temp-=100
    schermo.blit(sfondo_red, (35, 390))
    schermo.blit(label_sconfitta, (50, 400))
    pygame.mixer.Sound.play(morto)
    pygame.display.update()
    pygame.time.delay(2000)
    schermo.blit(label_ricomincia, (50, 500))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # (premi spazio per ricominciare)
                ricomincia()
                return
            elif event.type == pygame.QUIT:
                pygame.quit()


def ricomincia(successivo=False):
    pygame.event.clear()
    global m_su
    global m_sx
    global m_dx
    global m_giu
    global spazio
    m_su = False
    m_sx = False
    m_dx = False
    m_giu = False
    spazio = False
    reset_mostri()
    reset_livelli()  # livello1_mod = livello1[:]
    reset_tempo()
    reset_chiavi()
    if not successivo:
        reset_punteggio()
    giocatore.rect = pygame.Rect(470, 620, dim_pg, dim_pg)
    aggiorna()
    pygame.event.clear()


def reset_livelli():
    liv_mod = livelli[livello_giocato][:]
    mura.clear()
    inizializza_mura(liv_mod)


def reset_mostri():
    mostri.clear()


def reset_chiavi():
    giocatore.chiavi = 0


def reset_tempo():
    global tempo
    tempo = 0


def reset_punteggio():
    global punteggio
    punteggio = punteggio_temp


def aggiungi_punti():
    global tempo_effettivo
    global tempo
    global punteggio
    while tempo_effettivo >= 0:  # tempo < tempo_limite
        tempo_effettivo -= 1  # questa si può togliere
        tempo += 1
        aggiorna()
        punteggio += 25
        pygame.time.delay(100)
    global punteggio_temp
    punteggio_temp = punteggio


def prossimo_livello():
    global livello_giocato
    livello_giocato += 1
    if livello_giocato >= len(livelli):
        vittoria()
    ricomincia(True)  # True significa che non è il primo livello, quindi non deve resettare il punteggio


def vittoria():
    pass


''' FINE SPAZIO DEDICATO A DICHIARAZIONE FUNZIONI E CLASSI'''

''' MAIN '''
giocatore = Giocatore()
inizio()
while True:
    clock.tick(30)
    # pygame.time.delay(1000)
    for evento in pygame.event.get():
        if evento.type == pygame.USEREVENT:
            tempo += 1
            tempo_effettivo = tempo_limite - tempo
            if tempo_effettivo < 1:
                aggiorna()
                sconfitta("tempo")
        elif evento.type == pygame.KEYDOWN:  # eventi legati alla tastiera
            if evento.key == pygame.K_w:
                m_su = True
            if evento.key == pygame.K_a:
                m_sx = True
            if evento.key == pygame.K_s:
                m_giu = True
            if evento.key == pygame.K_d:
                m_dx = True
            if evento.key == pygame.K_SPACE:
                spazio = True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                m_su = False
            if evento.key == pygame.K_a:
                m_sx = False
            if evento.key == pygame.K_s:
                m_giu = False
            if evento.key == pygame.K_d:
                m_dx = False
            if evento.key == pygame.K_SPACE:
                spazio = False
        elif evento.type == pygame.QUIT:
            pygame.quit()
    frame += 1
    frame %= 32 * 100  # 32 è semplicemente il massimo comune divisore di tutti i frame, in modo da non farli "scattare"
    muovi(giocatore)  # ,m_su,m_sx,m_giu,m_dx,spazio
    muovi_mostri()
    aggiorna()
