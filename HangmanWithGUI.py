import pygame
import math
import random
from wordsvault import wordsare


def draw():
    window.fill(WHITE)

    # draw title
    text = title_font.render("HANGMAN", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_Font.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))
    
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), Radius, 3)
            text = letter_font.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(700)
    window.fill(WHITE)
    text = word_Font.render(message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

def gameloop():
    pygame.mixer.music.load("images/game-start-6104.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.7)
    global hangman_status        
    # Setup game loop
    FPS = 60
    clock = pygame.time.Clock()
    exit_game = True

    while exit_game:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if distance < Radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            if event.type == pygame.KEYDOWN:
                n=event
                keypressed(n)

        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You WON!")
            break
        if hangman_status == 6:
            display_message("You LOST! The word was "+ word)
            break
            
def keypressed(n):
    if n.key == pygame.K_a:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_b:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_c:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_d:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_e:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_f:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_g:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_h:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_i:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_j:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_k:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_l:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_m:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_n:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_o:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_p:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_q:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_r:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_s:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_t:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_u:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_v:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_w:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_x:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_y:
        k = n.unicode
        keyvalue(k)
    if n.key == pygame.K_z:
        k = n.unicode
        keyvalue(k)
def keyvalue(k):
    global hangman_status
    for letter in letters:
        x, y, ltr, visible = letter
        if visible  :
            if k == ltr.lower() :
                letter[3] = False
                guessed.append(ltr)
                if ltr not in word:
                    hangman_status += 1

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    
    exit_game = True
    
    # setup display
    WIDTH, HEIGHT = 800, 500
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman Game!")
    
    while exit_game:
        
        # button variables
        Radius = 20
        Gap = 15
        letters = []
        startx = round((WIDTH - (Radius * 2 + Gap) * 13) / 2)
        starty = 400
        A = 65
        for i in range(26):
            x = startx + Gap * 2 + ((Radius * 2 + Gap) * (i % 13))
            y = starty + ((i // 13) * (Gap + Radius * 2))
            letters.append([x, y, chr(A + i), True])

        # fonts
        letter_font = pygame.font.SysFont('comicsans', 40)
        word_Font = pygame.font.SysFont('comicsans', 60)
        title_font = pygame.font.SysFont('comicsans', 70)

        # load images.
        images = []
        for i in range(7):
            myimage = pygame.image.load("images/hangman" + str(i) + ".png")
            images.append(myimage)

        # colors
        WHITE = (225,225,225)
        BLACK = (0,0,0)

        # game variables
        hangman_status = 0
        word = random.choice(wordsare).upper()
        # Neglecting words that have '- 'or 'space'
        while '-' in word or ' ' in word:
            word = random.choice(wordsare)
        print(word)
        guessed = []
        
        gameloop()
        