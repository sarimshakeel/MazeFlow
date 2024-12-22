import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MazeFlow")
clock = pygame.time.Clock()

fontp1 = r"C:\Users\sarim\Desktop\Maze Solver\add-ons\CASCADIACODE.ttf"
font1 = pygame.font.Font(fontp1, 40)

btn1 = pygame.Rect(300, 200, 200, 50)
btn2 = pygame.Rect(300, 300, 200, 50)
btn3 = pygame.Rect(300, 400, 200, 50)
btn_back = pygame.Rect(10, 10, 50, 50) 

backimg = pygame.image.load(r"C:\Users\sarim\Desktop\Maze Solver\add-ons\back.png")
backimg = pygame.transform.scale(backimg, (50, 50))

def generate():
    screen.fill((0, 0, 0))
    text_surface = font1.render("GENERATE", True, (0, 255, 0))
    screen.blit(text_surface, (300, 200))
    pygame.display.flip()

def solve():
    screen.fill((0, 0, 0))
    text_surface = font1.render("SOLVE", True, (0, 255, 0))
    screen.blit(text_surface, (300, 200))
    pygame.display.flip()

def leaderboard():
    screen.fill((0, 0, 0))
    text_surface = font1.render("LEADERBOARD", True, (0, 255, 0))
    screen.blit(text_surface, (300, 200))
    pygame.display.flip()

def exit():
    global running
    running = False

running = True
current_screen = "main"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == "main":
                if btn1.collidepoint(mouse_pos):
                    current_screen = "generate"
                    generate()
                    solve()
                if btn2.collidepoint(mouse_pos):
                    current_screen = "leaderboard"
                    leaderboard()
                if btn3.collidepoint(mouse_pos):
                    exit()
            else:
                if btn_back.collidepoint(mouse_pos):
                    current_screen = "main"

    if current_screen == "main":
        screen.fill((0, 0, 0))
        font1.set_italic(True)
        font1.set_underline(True)
        text_surface = font1.render("Maze Flow", True, (0, 255, 0))
        screen.blit(text_surface, (300, 50))
        font1.set_italic(False)
        font1.set_underline(False)

        btn1_txt = font1.render("GENERATE & SOLVE", True, (0, 255, 0))
        if btn1.collidepoint(pygame.mouse.get_pos()):
            btn1_txt = font1.render("GENERATE & SOLVE", True, (255, 255, 255))
        btn1_txt_rect = btn1_txt.get_rect(center=btn1.center)
        screen.blit(btn1_txt, btn1_txt_rect)

        btn2_txt = font1.render("LEADERBOARD", True, (0, 255, 0))
        if btn2.collidepoint(pygame.mouse.get_pos()):
            btn2_txt = font1.render("LEADERBOARD", True, (255, 255, 255))
        btn2_txt_rect = btn2_txt.get_rect(center=btn2.center)
        screen.blit(btn2_txt, btn2_txt_rect)

        btn3_txt = font1.render("EXIT", True, (0, 255, 0))
        if btn3.collidepoint(pygame.mouse.get_pos()):
            btn3_txt = font1.render("EXIT", True, (255, 255, 255))
        btn3_txt_rect = btn3_txt.get_rect(center=btn3.center)
        screen.blit(btn3_txt, btn3_txt_rect)
    else:
        # Draw the "Back" button image
        screen.blit(backimg, (btn_back.x, btn_back.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()