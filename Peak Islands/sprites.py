import requests
import random

from settings import *

class Tile:
    def __init__(self, row, col, board, TILESIZE):
        self.x, self.y = col, row
        self.TILESIZE =TILESIZE
        self.tile_area = pygame.Rect(self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE)
        self.island_id = 0
        self.height = self.get_height(board)
        self.color = self.get_color(self.height)
        self.type = 0

    def draw(self, board_surface, lives, vulcano):
        pygame.draw.rect(board_surface, self.color, self.tile_area)

        if self.type == 1 and self.x < lives * 2 + 9:
            board_surface.blit(tile_hearth, (self.x * self.TILESIZE, self.y* self.TILESIZE))

        if self.type == 3:
            board_surface.blit(tile_numbers[self.y-3], (self.x * self.TILESIZE, self.y * self.TILESIZE))

        if self.type == 4:
            board_surface.blit(tile_numbers[self.y - 15], (self.x * self.TILESIZE, self.y * self.TILESIZE))

        if self.type == 5:
            board_surface.blit(tile_numbers[self.x + 8], (self.x * self.TILESIZE, self.y * self.TILESIZE))

        if self.type == 6:
            board_surface.blit(tile_numbers[self.x -1 ], (self.x * self.TILESIZE, self.y * self.TILESIZE))




    def draw_error(self, board_surface):
        self.color = (0, 105, 248)
        self.height = 0
        self.island_id = 0
        pygame.draw.rect(board_surface, self.color, self.tile_area)

    def draw_magma(self, board_surface):
        self.color = (161,36,36)
        self.height = 0
        self.island_id = 0
        pygame.draw.rect(board_surface, self.color, self.tile_area)

    def assign_island(self, which):
        self.island_id = which

    def get_height(self, board):
        if self.x > 29 or self.y > 29:
            return -1
        else:
            return board.heights[self.y][self.x]

    def get_color(self, value):
        if value == 0:
            return (0, 105, 248)

        elif value == -1:
            return (211, 211, 211)

        elif 1 <= value <= 200:
            green_value = int(255 - (value * (255 - 180) / 200))
            return (97, green_value, 0)

        elif 201 <= value <= 400:
            green_value = int(255 - ((value - 200) * (255 - 180) / 200))
            return (97, green_value, 0)

        elif 401 <= value <= 600:
            green_value = int(180 - ((value - 400) * (180 - 85) / 200))
            return (20, green_value, 0)

        elif 601 <= value <= 900:
            brown_value = int(225 - ((value - 600) * (225 - 175) / 300))
            return (brown_value, brown_value // 2, brown_value // 4)

        elif 901 <= value <= 999:
            gray_value = int(255 - ((999 - value) * (255 - 175) / 98))
            return (gray_value, gray_value, gray_value)

        elif value == 1000:
            return (255, 255, 255)

    def __repr__(self):
        return str(self.island_id)

class Board:
    def __init__(self, TILESIZE, WIDTH, HEIGHT, clock_mode):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.response = requests.get('https://jobfair.nordeus.com/jf24-fullstack-challenge/test')
        self.heights = self.get_heights()
        self.board_list = [[Tile(row, col, self, TILESIZE) for col in range(COLS)] for row in range(ROWS)]
        self.islands = self.find_islands()
        self.best_island = self.find_best()
        self.clock_mode = clock_mode

        self.make_legend()

        global tile_numbers, tile_hearth, tile_vulcano

        tile_numbers = []
        for i in range(1, 23):
            tile_numbers.append(
                pygame.transform.scale(pygame.image.load(os.path.join("pictures", f"{i}.png")), (TILESIZE, TILESIZE)))

        tile_hearth = pygame.transform.scale(pygame.image.load(os.path.join("pictures", f"TileHearth.webp")),
                                             (TILESIZE, TILESIZE))

    def get_heights(self):
        map_data = self.response.text
        rows = map_data.split('\n')

        map_values = []
        for row in rows:
            if row.strip():
                map_values.append([int(value)for value in row.split()])

        return map_values

    def mark_island(self, Tile, island_id, island_map):
        if Tile.height == 0 or Tile.island_id != 0:
            return

        Tile.island_id = island_id
        island_map[island_id].append(Tile)

        if Tile.y != 29:
            self.mark_island(self.board_list[Tile.y+1][Tile.x], island_id, island_map)
        if Tile.y != 0:
            self.mark_island(self.board_list[Tile.y-1][Tile.x], island_id, island_map)
        if Tile.x != 29:
            self.mark_island(self.board_list[Tile.y][Tile.x+1], island_id, island_map)
        if Tile.x != 0:
            self.mark_island(self.board_list[Tile.y][Tile.x-1], island_id, island_map)

    def find_islands(self):
        island_id = 1
        island_map = {}

        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[0])):
                if self.board_list[i][j].height > 0 and self.board_list[i][j].island_id == 0:  # Novi deo ostrva
                    island_map[island_id] = []
                    self.mark_island(self.board_list[i][j], island_id, island_map)
                    island_id += 1

        return island_map

    def find_best(self):

        best = 0
        best_id = 0
        cur = 0
        for id in self.islands.values():
            sum = 0
            num = 0

            for elem in id:
                sum = elem.height + sum
                num = num + 1
            sum = sum / num

            if best < sum:
                best = sum
                best_id = cur

            cur = cur + 1

        return best_id + 1

    def make_legend(self):

        for x in range(3, 9):
            tile = self.board_list[31][x]
            tile.type = 5

        self.board_list[31][10].type = 1
        self.board_list[31][12].type = 1
        self.board_list[31][14].type = 1

        if self.clock_mode == True:
            for x in range(18, 23):
                tile = self.board_list[31][x]
                tile.type = 6


        for y in range(3, 9):
            tile = self.board_list[y][31]
            tile.type = 3

        for y in range(21, 26):
            tile = self.board_list[y][31]
            tile.type = 4

        for y in range(10, 20):
            tile = self.board_list[y][31]
            tile.type = 2

            if y == 10:
                tile.color = (255, 255, 255)
            elif 11 <= y <= 12:
                gray_value = 135 + ((12 - y) * 40)
                tile.color = (gray_value, gray_value, gray_value)
            elif 13 <= y <= 15:
                brown_value = 70 + ((y - 13) * 40)
                tile.color = (brown_value, brown_value // 2, brown_value // 4)
            elif 16 <= y <= 18:
                green_value = 175 + ((y - 16) * 40)
                tile.color = (0, green_value, 0)
            elif y == 19:
                tile.color = (0, 105, 248)

    def draw(self, screen, lives, vulcano):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface, lives, vulcano)
        screen.blit(self.board_surface, (0, 0))

    def island_mistake(self, screen, id):
        for tile in self.islands[id]:
            tile.draw_error(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def vulcano_errupts(self, screen, sunk):
        if len(self.islands) - sunk >2:
            k=2
        elif len(self.islands) - sunk == 2:
            k=1
        else:
            k=0

        for j in range(0,k):
            while(True):
                i=random.randint(1, len(self.islands))
                if i == self.best_island:
                    continue
                elif self.islands[i][0].island_id == 0:
                    continue
                break
            for tile in self.islands[i]:
                tile.draw_magma(self.board_surface)
            screen.blit(self.board_surface, (0, 0))

    def display_board(self):
        for row in self.board_list:
            print(row)
        print("\n")
        print(self.best_island)