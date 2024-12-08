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
btn4 = pygame.Rect(300, 500, 200, 50)

def exit():
    global running
    running = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if btn1.collidepoint(mouse_pos):
                print("Generate clicked")
            if btn2.collidepoint(mouse_pos):
                print("Solve clicked")
            if btn3.collidepoint(mouse_pos):
                print("Rankings clicked")
            if btn4.collidepoint(mouse_pos):
                exit()        


    screen.fill((0, 0, 0))

    font1.set_italic(True)
    font1.set_underline(True)
    text_surface = font1.render("Maze Flow", True, (0, 255, 0))
    screen.blit(text_surface, (300, 50))
    font1.set_italic(False)
    font1.set_underline(False)

   
    btn1_txt = font1.render("GENERATE", True, (0, 255, 0))
    if btn1.collidepoint(pygame.mouse.get_pos()):
        btn1_txt = font1.render("GENERATE", True, (255,255, 255))
    btn1_txt_rect = btn1_txt.get_rect(center=btn1.center)
    screen.blit(btn1_txt, btn1_txt_rect)

    btn2_txt = font1.render("SOLVE", True, (0, 255, 0))
    if btn2.collidepoint(pygame.mouse.get_pos()):
        btn2_txt = font1.render("SOLVE", True, (255,255, 255))
    btn2_txt_rect = btn2_txt.get_rect(center=btn2.center)
    screen.blit(btn2_txt, btn2_txt_rect)

    btn3_txt = font1.render("RANKINGS", True, (0, 255, 0))
    if btn3.collidepoint(pygame.mouse.get_pos()):
        btn3_txt = font1.render("RANKINGS", True, (255,255, 255))
    btn3_txt_rect = btn3_txt.get_rect(center=btn3.center)
    screen.blit(btn3_txt, btn3_txt_rect)

    btn4_txt = font1.render("EXIT", True, (0, 255, 0))
    if btn4.collidepoint(pygame.mouse.get_pos()):
        btn4_txt = font1.render("EXIT", True, (255,255, 255))
    btn4_txt_rect = btn4_txt.get_rect(center=btn4.center)
    screen.blit(btn4_txt, btn4_txt_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
