import pygame
from generate import create_grid, generate_maze, draw_maze
from solve import dfs,bfs,dead_end_filling
from leaderboard import Leaderboard

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MazeFlow")
clock = pygame.time.Clock()

fontp1 = r"C:\Users\sarim\Desktop\Maze Solver\add-ons\CASCADIACODE.ttf"
font1 = pygame.font.Font(fontp1, 40)
font2 = pygame.font.Font(fontp1, 20)

btn1 = pygame.Rect(300, 200, 200, 50)
btn2 = pygame.Rect(300, 300, 200, 50)
btn3 = pygame.Rect(300, 400, 200, 50)
btn_back = pygame.Rect(700, 10, 50, 50)
btn_generate = pygame.Rect(300, 350, 200, 50)
btn_clear = pygame.Rect(300, 450, 200, 50)

backimg = pygame.image.load(r"C:\Users\sarim\Desktop\Maze Solver\add-ons\back.png")
backimg = pygame.transform.scale(backimg, (50, 50))

grid_input = pygame.Rect(200, 270, 400, 50)
input_active = False
input_text = ""

grid = None
grid_mode = False
leaderboard = Leaderboard()
leaderboard.load_from_file('leaderboard.json')


def generate(grid_size):
    screen.fill((0, 0, 0))
    global grid, grid_mode
    grid = create_grid(grid_size, grid_size)
    grid_mode = True

def solve_dfs():
    if grid:
        elapsed_time = dfs(screen, grid)
        if elapsed_time is not None:
            leaderboard.add_record("Depth-First Search", elapsed_time, f"{len(grid)}x{len(grid[0])}")
            leaderboard.save_to_file('leaderboard.json')
        screen.blit(backimg, (btn_back.x, btn_back.y))
        pygame.display.flip()

def solve_bfs():
    if grid:
        elapsed_time = bfs(screen, grid)
        if elapsed_time is not None:
            leaderboard.add_record("Breadth-First Search", elapsed_time, f"{len(grid)}x{len(grid[0])}")
            leaderboard.save_to_file('leaderboard.json')
        screen.blit(backimg, (btn_back.x, btn_back.y))
        pygame.display.flip()

def solve_dead_end_filling():
    if grid:
        elapsed_time = dead_end_filling(screen, grid)
        if elapsed_time is not None:
            leaderboard.add_record("Dead End Filling", elapsed_time, f"{len(grid)}x{len(grid[0])}")
            leaderboard.save_to_file('leaderboard.json')
        screen.blit(backimg, (btn_back.x, btn_back.y))
        pygame.display.flip()       

def leaderboard_screen():
    screen.fill((0, 0, 0))
    text_surface = font1.render("Leaderboard", True, (0, 255, 0))
    screen.blit(text_surface, (270, 30))
    leaderboard.load_from_file('leaderboard.json')
    leaderboard.display_leaderboard(screen, font2)
    screen.blit(backimg, (btn_back.x, btn_back.y))
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
                if btn2.collidepoint(mouse_pos):
                    current_screen = "leaderboard"
                    leaderboard_screen()
                if btn3.collidepoint(mouse_pos):
                    exit()
            elif current_screen == "generate":
                if grid_input.collidepoint(mouse_pos):
                    input_active = not input_active
                else:
                    input_active = False
                if btn_back.collidepoint(mouse_pos):
                    current_screen = "main"
                    grid = None
                    grid_mode = False
                    input_text = ""
                if btn_generate.collidepoint(mouse_pos):
                    try:
                        grid_size = int(input_text)
                        generate(grid_size)
                    except ValueError:
                        print("Invalid grid size")
            
            elif current_screen == "leaderboard":
                if btn_back.collidepoint(mouse_pos):
                    current_screen = "main"

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if btn_clear.collidepoint(mouse_pos):
                        leaderboard.clear_leaderboard('leaderboard.json')    

            elif current_screen == "grid":
                if btn_back.collidepoint(mouse_pos):
                    current_screen = "generate"
                    grid_mode = False

        if event.type == pygame.KEYDOWN:
            if input_active and current_screen == "generate":
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    try:
                        grid_size = int(input_text)
                        generate(grid_size)
                    except ValueError:
                        print("Invalid grid size")
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

            elif current_screen == "grid":
                if event.key == pygame.K_d:
                    solve_dfs()

                elif event.key == pygame.K_b:
                    solve_bfs()    

                elif event.key == pygame.K_f:
                    solve_dead_end_filling()

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
    
    if current_screen == "leaderboard":
        leaderboard.display_leaderboard(screen, font1)

        btn_clear_txt = font1.render("Clear", True, (255, 0, 0))
        if btn_clear.collidepoint(pygame.mouse.get_pos()):
            btn_clear_txt = font1.render("Clear", True, (255, 255, 255))
        btn_clear_txt_rect = btn_clear_txt.get_rect(center=btn_clear.center)
        pygame.draw.rect(screen, (169, 0, 1), btn_clear, 2)
        screen.blit(btn_clear_txt, btn_clear_txt_rect)

    elif current_screen == "generate":
        screen.fill((0, 0, 0))

        grid_input_txt = font1.render("Enter Grid Size: ", True, (0, 255, 0))
        screen.blit(grid_input_txt, (grid_input.x, grid_input.y - 50))

        pygame.draw.rect(screen, (255, 255, 255), grid_input, 2)
        if input_active:
            pygame.draw.rect(screen, (0, 255, 0), grid_input, 2)
        text_surface = font1.render(input_text, True, (255, 255, 255))
        screen.blit(text_surface, (grid_input.x + 5, grid_input.y + 5))

        btn_generate_txt = font1.render("Generate", True, (0, 255, 0))
        if btn_generate.collidepoint(pygame.mouse.get_pos()):
            btn_generate_txt = font1.render("Generate", True, (255, 255, 255))
        btn_generate_txt_rect = btn_generate_txt.get_rect(center=btn_generate.center)
        pygame.draw.rect(screen, (255, 255, 255), btn_generate, 2)
        screen.blit(btn_generate_txt, btn_generate_txt_rect)

        screen.blit(backimg, (btn_back.x, btn_back.y))

        if grid_mode:
            current_screen = "grid"
            generate_maze(screen, grid, grid_size, grid_size)
            draw_maze(screen, grid)
            screen.blit(backimg, (btn_back.x, btn_back.y)) 
            
            controls = [
                "'D' for DFS",
                "'B' for BFS",
                "'F' for Dead",
                "End Filling"
            ]
            y_offset = btn_back.y + btn_back.height + 10
            for text in controls:
                control_s = font2.render(text, True, (255, 255, 255))
                control_rec = control_s.get_rect(topright=(screen.get_width() - 10, y_offset))
                screen.blit(control_s, control_rec)
                y_offset += 30  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()