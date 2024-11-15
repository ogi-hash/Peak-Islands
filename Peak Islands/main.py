from sprites import *
from settings import *

pygame.init()
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    clock = pygame.time.Clock()
    counter = 6
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock_mode = False
    counter_text = str(counter)

    def new(self):
        self.board = Board(TILESIZE, WIDTH, HEIGHT, self.clock_mode)
        self.board.display_board()

    window = 0
    lives = 3
    vulcano_active = False
    vulcano_enabled = True
    vulcano = 0
    sunk = 0
    score= 0

    choice_size = [(219, 219, 0),(255, 255, 0),(219, 219, 0)]
    choice_vulcano = [(255, 255, 0),(219, 219, 0)]
    choice_mode = [(255, 255, 0),(219, 219, 0)]

    #HOVERED variables for all buttons
    hovered_start = False
    hovered_settings = False
    hovered_instructions = False
    hovered_begin = False
    hovered_small = False
    hovered_medium = False
    hovered_large = False
    hovered_back = False
    hovered_enable = False
    hovered_disable = False
    hovered_normal= False
    hovered_extreme = False
    hovered_game_over = False

    #FONTS
    title_font_size =  None
    option_font_size = None
    button_font_size = None
    time_font_size = None
    txt_font_size = None

    font = None
    button_font = None
    option_font = None
    time_font = None
    txt_font= None

    #WINDOW 0
    title_text = None
    title_rect = None

    start_text = None
    start_rect = None

    background_image = None
    vulcano_image =None

    #WINDOW 2
    menu_text = None
    menu_rect = None

    settings_text = None
    settings_rect = None

    instructions_text = None
    instructions_rect = None

    begin_text = None
    begin_rect = None

    #WINDOW 3
    settings_title_text = None
    settings_title_rect = None

    back_text = None
    back_rect = None

    size_title_text = None
    size_title_rect = None
    small_text = None
    small_rect = None
    medium_text = None
    medium_rect = None
    large_text = None
    large_rect = None
    bomb_title_text = None
    bomb_title_rect = None
    enable_text = None
    enable_rect = None
    disable_text = None
    disable_rect = None
    mode_title_text = None
    mode_title_rect = None
    normal_text = None
    normal_rect = None
    extreme_text = None
    extreme_rect = None
    instructions_title_text =None
    instructions_title_rect = None

    #WINDOW 5
    game_over_text = None
    game_over_rect = None
    game_over_image = None


    def initialize(self):
        # Set font sizes based on screen height
        self.new()

        self.title_font_size = int(HEIGHT * 0.15)
        self.option_font_size = int(HEIGHT * 0.08)
        self.button_font_size = int(HEIGHT * 0.08)
        self.time_font_size = int(HEIGHT /33 * 2.7)
        self.txt_font_size = int (HEIGHT / 33 *1.15 )

        # Load fonts
        self.font = pygame.font.Font('Pixellettersfull-BnJ5.ttf', self.title_font_size)
        self.font.set_bold(True)
        self.button_font = pygame.font.Font('Pixellettersfull-BnJ5.ttf', self.button_font_size)
        self.option_font = pygame.font.Font('Pixellettersfull-BnJ5.ttf', self.option_font_size)
        self.option_font.set_bold(True)
        self.time_font = pygame.font.Font('Pixellettersfull-BnJ5.ttf', self.time_font_size)
        self.time_font.set_bold(True)
        self.txt_font = pygame.font.Font('Pixellettersfull-BnJ5.ttf', self.txt_font_size)

        # Initialize text and rect for the title
        self.title_text = self.font.render(TITLE, True, (255, 0, 0))
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))

        # Initialize text and rect for the start button
        self.start_text = self.button_font.render("Start", True, (255, 0, 0))  # Red text color
        self.start_rect = self.start_text.get_rect(center=(WIDTH // 2, HEIGHT // 4 * 3))

        # Initialize background image
        self.background_image = pygame.image.load(os.path.join("pictures", "start.png"))
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Initialize attributes for menu screen
        self.menu_text = self.font.render("Main Menu", True, (255, 0, 0))
        self.menu_rect = self.menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))

        self.settings_text = self.button_font.render("Settings", True, (255, 0, 0))  # Red text color
        self.settings_rect = self.settings_text.get_rect(center=(WIDTH // 2, HEIGHT // 33 * 12))

        self.instructions_text = self.button_font.render("Instructions", True, (255, 0, 0))  # Red text color
        self.instructions_rect = self.instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 33 * 16))

        self.begin_text = self.button_font.render("Begin", True, (255, 0, 0))  # Red text color
        self.begin_rect = self.begin_text.get_rect(center=(WIDTH // 2, HEIGHT // 33 * 20))

        # Initialize attributes for settings screen
        self.settings_title_text = self.font.render("Settings", True, (255, 0, 0))
        self.settings_title_rect = self.settings_title_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))

        self.back_text = self.button_font.render("Back", True, (255, 0, 0))  # Red text color
        self.back_rect = self.back_text.get_rect(center=(WIDTH // 2, HEIGHT // 33 * 30))

        self.size_title_text = self.option_font.render("Screen size:", True, (255, 0, 0))
        self.size_title_rect = self.size_title_text.get_rect(center=(WIDTH // 33 * 6, HEIGHT // 33 * 12))

        self.small_text = self.button_font.render("Small", True, (255, 0, 0))  # Red text color
        self.small_rect = self.small_text.get_rect(center=(WIDTH // 33 * 15, HEIGHT // 33 * 12))

        self.medium_text = self.button_font.render("Medium", True, (255, 0, 0))  # Red text color
        self.medium_rect = self.medium_text.get_rect(center=(WIDTH // 33 * 22, HEIGHT // 33 * 12))

        self.large_text = self.button_font.render("Large", True, (255, 0, 0))  # Red text color
        self.large_rect = self.large_text.get_rect(center=(WIDTH // 33 * 29, HEIGHT // 33 * 12))

        self.bomb_title_text = self.option_font.render("Vulcano:", True, (255, 0, 0))
        self.bomb_title_rect = self.bomb_title_text.get_rect(center=(WIDTH // 33 * 6, HEIGHT // 33 * 18))

        self.enable_text = self.button_font.render("Enable", True, (255, 0, 0))  # Red text color
        self.enable_rect = self.enable_text.get_rect(center=(WIDTH // 33 * 16, HEIGHT // 33 * 18))

        self.disable_text = self.button_font.render("Disable", True, (255, 0, 0))  # Red text color
        self.disable_rect = self.disable_text.get_rect(center=(WIDTH // 33 * 25, HEIGHT // 33 * 18))

        self.mode_title_text = self.option_font.render("Mode:", True, (255, 0, 0))
        self.mode_title_rect = self.mode_title_text.get_rect(center=(WIDTH // 33 * 6, HEIGHT // 33 * 24))

        self.normal_text = self.button_font.render("Normal", True, (255, 0, 0))  # Red text color
        self.normal_rect = self.normal_text.get_rect(center=(WIDTH // 33 * 16, HEIGHT // 33 * 24))

        self.extreme_text = self.button_font.render("Extreme", True, (255, 0, 0))  # Red text color
        self.extreme_rect = self.extreme_text.get_rect(center=(WIDTH // 33 * 26, HEIGHT // 33 * 24))

        # Initialize attributes for game screen
        self.time_text = self.time_font.render(self.counter_text,  True, (255, 0, 0))
        self.time_rect = self.extreme_text.get_rect(center=(WIDTH // 33 * 27, HEIGHT // 33 * 31.5))

        self.vulcano_image = pygame.transform.scale(pygame.image.load(os.path.join("pictures", f"Vulcano.webp")),
                                              (TILESIZE * 2.55, TILESIZE * 2.55))

        # Initialize attriutes for instructions screen
        self.instructions_title_text = self.font.render("Instructions", True, (255, 0, 0))
        self.instructions_title_rect = self.instructions_title_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))

        #Initialize atributes for game over screen
        self.game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))

        self.game_over_image = pygame.image.load(os.path.join("pictures", "game_over4.png"))
        self.game_over_image = pygame.transform.scale(self.game_over_image, (WIDTH, HEIGHT))

        self.score_text = self.option_font.render("Score: "+ str(self.score), True, (255, 0, 0))
        self.score_rect = self.menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 7 * 2))



    def run(self):
        self.playing = True
        self.initialize()


        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()


    def button_click(self, but, text, hovered, colour):
        # Padding for the shadow and the "raise" effect
        padding_w = int(WIDTH * 0.01)  # Padding around the button for hover effect
        padding_h = int(HEIGHT * 0.01)
        but_offset = int(WIDTH * 0.005)  # Offset for shadow for the raised effect

        # If the button is hovered, enlarge it, add shadow, and shift it
        if hovered:
            # Shadow effect for the button background
            shadow_rect = but.inflate(padding_w, padding_h)  # Enlarge the rect for hover effect
            pygame.draw.rect(self.screen, (0, 0, 0), shadow_rect)  # Draw the shadow

            # Shifted button background and text: Move temporarily for the hover effect
            but_temp = but.copy()
            but_temp.x -= but_offset  # Shift the button position
            but_temp.y -= but_offset
            pygame.draw.rect(self.screen, colour, but_temp)  # Draw the background for shifted button

            # Draw the text, centered on the button
            text_rect = text.get_rect(center=but_temp.center)
            self.screen.blit(text, text_rect)
        else:
            # Draw the button normally without hover effect
            pygame.draw.rect(self.screen, colour, but)
            text_rect = text.get_rect(center=but.center)
            self.screen.blit(text, text_rect)

    def check_hovered(self, but):
        return but.collidepoint(pygame.mouse.get_pos())

    def draw(self):
        colour = (255, 255, 0)
        if self.window == 0:
            self.screen.fill(WHITE)

            self.screen.blit(self.background_image, (0,0))


            self.screen.blit(self.title_text, self.title_rect)


            self.button_click(self.start_rect, self.start_text, self.hovered_start, colour)

        if self.window == 1:

            self.screen.fill(BGCOLOUR)
            self.board.draw(self.screen, self.lives, self.vulcano_active)

            if self.clock_mode == True:
                if self.counter == 6:
                    self.counter_text = '5'
                else:
                    self.counter_text = str(self.counter)
                self.time_text = self.time_font.render(self.counter_text, True, (255, 0, 0))
                self.screen.blit(self.time_text, self.time_rect)

            if self.vulcano == 3:
                self.screen.blit(self.vulcano_image, (TILESIZE * 30.2, TILESIZE *30.2))

        if self.window == 2:
            self.screen.fill((235, 180, 100))
            self.screen.blit(self.menu_text, self.menu_rect)

            self.button_click(self.settings_rect, self.settings_text, self.hovered_settings,colour)
            self.button_click(self.instructions_rect, self.instructions_text, self.hovered_instructions, colour)
            self.button_click(self.begin_rect, self.begin_text, self.hovered_begin, colour)

        if self.window == 3:

            self.screen.fill((235, 180, 100))
            self.screen.blit(self.settings_title_text, self.settings_title_rect)

            self.screen.blit(self.size_title_text, self.size_title_rect)

            self.button_click(self.small_rect, self.small_text, self.hovered_small, self.choice_size[0])
            self.button_click(self.medium_rect, self.medium_text, self.hovered_medium,self.choice_size[1])
            self.button_click(self.large_rect, self.large_text, self.hovered_large,self.choice_size[2])

            self.screen.blit(self.bomb_title_text, self.bomb_title_rect)
            self.button_click(self.enable_rect, self.enable_text, self.hovered_enable, self.choice_vulcano[0])
            self.button_click(self.disable_rect, self.disable_text, self.hovered_disable, self.choice_vulcano[1])

            self.screen.blit(self.mode_title_text, self.mode_title_rect)
            self.button_click(self.normal_rect, self.normal_text, self.hovered_normal, self.choice_mode[0])
            self.button_click(self.extreme_rect, self.extreme_text, self.hovered_extreme, self.choice_mode[1])

            self.button_click(self.back_rect, self.back_text, self.hovered_back, colour)

        if self.window == 4:
            self.screen.fill((235, 180, 100))
            self.screen.blit(self.instructions_title_text, self.instructions_title_rect)


            with open("instructions.txt", "r") as file:
                instructions_text = file.read()


            lines = instructions_text.splitlines()

            line_height = self.txt_font.get_height()
            title_offset = TILESIZE* 2.5
            y_offset = TILESIZE / 4 + title_offset

            for line in lines:

                if "**" in line:    
                    line = line.replace("**", "")
                    self.txt_font.set_bold(True)
                line_surface = self.txt_font.render(line, True, (255, 0, 0))
                line_rect = line_surface.get_rect(topleft=(TILESIZE, HEIGHT // 7 + y_offset))
                self.screen.blit(line_surface, line_rect)
                y_offset += line_height + TILESIZE / 4
                self.txt_font.set_bold(False)


            self.button_click(self.back_rect, self.back_text, self.hovered_back, colour)

        if self.window == 5:
            self.screen.fill(WHITE)

            self.screen.blit(self.game_over_image, (0, 0))

            self.screen.blit(self.game_over_text, self.game_over_rect)

            self.screen.blit(self.score_text, self.score_rect)

            self.button_click(self.back_rect, self.back_text, self.hovered_back, colour)

        pygame.display.flip()


    def check_win(self):
        pass


    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            global WIDTH, HEIGHT, TILESIZE

            if self.window == 0:
                self.hovered_start = self.check_hovered(self.start_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        self.window = 2

            elif self.window == 2:
                self.hovered_settings = self.check_hovered(self.settings_rect)
                self.hovered_instructions = self.check_hovered(self.instructions_rect)
                self.hovered_begin = self.check_hovered(self.begin_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.begin_rect.collidepoint(event.pos):
                        self.window = 1
                        self.lives = 3
                        self.sunk = 0
                        self.vulcano = 0
                        self.counter = 6
                        self.score = 0
                        game.new()
                        game.run()

                    if self.settings_rect.collidepoint(event.pos):
                        self.window = 3

                    if self.instructions_rect.collidepoint(event.pos):
                        self.window = 4


            elif self.window == 1:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    mx //= TILESIZE
                    my //= TILESIZE
                    if my > 29 or mx > 29:
                        continue

                    if event.button == 1:
                        if self.board.board_list[my][mx].height == 0:
                            continue
                        elif self.board.board_list[my][mx].island_id == self.board.best_island:
                            if self.lives < 3 and self.clock_mode == False:
                                self.lives += 1
                            if self.vulcano_enabled == True and self.vulcano < 3:
                                self.vulcano += 1
                                if self.vulcano == 3:
                                    self.vulcano_active = True
                            self.counter = 6
                            self.sunk = 0
                            self.score += 1
                            game.new()
                            game.run()
                        else:
                            self.lives -= 1
                            self.sunk += 1
                            self.board.island_mistake(self.screen, self.board.board_list[my][mx].island_id)
                            if self.lives == 0:
                                self.window = 5

                    elif event.button == 3 and self.vulcano_active == True:
                        self.vulcano = 0
                        self.vulcano_active = False
                        self.board.vulcano_errupts(self.screen, self.sunk)

                elif event.type == pygame.USEREVENT and self.clock_mode == True:
                    self.counter -= 1
                    if self.counter == 0:
                        self.window = 5

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.window = 2


            elif self.window == 3:
                self.hovered_small = self.check_hovered(self.small_rect)
                self.hovered_medium = self.check_hovered(self.medium_rect)
                self.hovered_large = self.check_hovered(self.large_rect)

                self.hovered_enable = self.check_hovered(self.enable_rect)
                self.hovered_disable = self.check_hovered(self.disable_rect)

                self.hovered_normal = self.check_hovered(self.normal_rect)
                self.hovered_extreme = self.check_hovered(self.extreme_rect)

                self.hovered_back = self.check_hovered(self.back_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.small_rect.collidepoint(event.pos):
                        TILESIZE = 10
                        WIDTH = TILESIZE * ROWS
                        HEIGHT = TILESIZE * COLS
                        self.choice_size = [(255, 255, 0),(219, 219, 0),(219, 219, 0)]
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        self.initialize()


                    elif self.medium_rect.collidepoint(event.pos):
                        TILESIZE = 20
                        WIDTH = TILESIZE * ROWS
                        HEIGHT = TILESIZE * COLS
                        self.choice_size = [(219, 219, 0),(255, 255, 0), (219, 219, 0)]
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        self.initialize()


                    elif self.large_rect.collidepoint(event.pos):
                        TILESIZE = 30
                        WIDTH = TILESIZE * ROWS
                        HEIGHT = TILESIZE * COLS
                        self.choice_size = [(219, 219, 0),(219, 219, 0),(255, 255, 0)]
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        self.initialize()


                    elif self.enable_rect.collidepoint(event.pos):
                        self.vulcano_enabled = True
                        self.choice_vulcano =[(255, 255, 0), (219, 219, 0)]

                    elif self.disable_rect.collidepoint(event.pos):
                        self.vulcano_enabled = False
                        self.choice_vulcano = [(219, 219, 0),(255, 255, 0)]

                    elif self.normal_rect.collidepoint(event.pos):
                        self.clock_mode = False
                        self.choice_mode = [(255, 255, 0), (219, 219, 0)]

                    elif self.extreme_rect.collidepoint(event.pos):
                        self.clock_mode = True
                        self.choice_mode = [(219, 219, 0), (255, 255, 0)]

                    elif self.back_rect.collidepoint(event.pos):
                            self.window = 2

            elif self.window == 4:
                self.hovered_back = self.check_hovered(self.back_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.back_rect.collidepoint(event.pos):
                            self.window = 2

            elif self.window == 5:
                self.hovered_back = self.check_hovered(self.back_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.back_rect.collidepoint(event.pos):
                            self.window = 2

game = Game()
while True:
    game.run()