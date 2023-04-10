import pygame
import sys
import os

IMAGE = input('Enter your file: ')

class Game(object):
    def __init__(self):
        self.run = True
        self.img = pygame.image.load(IMAGE)
        self.rects = []
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.init_rect_pos = (0,0)
        
    def draw(self):
        #draw image
        self.screen.fill((0,0,0))
        self.screen.blit(self.img,(0,0))

        #draw rects
        for rect in self.rects:
            pygame.draw.rect(self.screen, (0,0,0), rect, 1)
            
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mousedown(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouseup(event)
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if len(self.rects) >= 1:
                        self.rects.pop()
                if event.key == pygame.K_o:
                    self.create_images()

    def handle_mousedown(self,event):
        print(event)
        self.init_rect_pos = event.pos

    def handle_mouseup(self,event):
        print(event)
        w = event.pos[0] - self.init_rect_pos[0]
        h = event.pos[1] - self.init_rect_pos[1]
        self.rects.append(pygame.Rect(self.init_rect_pos, (w,h)))

    def handle_quit(self):
        self.run = False

    def main(self):   
        while self.run:
            self.draw()
            self.handle_events()
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def create_images(self):
        N = len(self.rects)
        print("initating image creation")
        if N == 0:
            print("not enough rects")
            return False

        options = []
        for n in range(1, 2**N):
            #for d in range(0,N):
            bin_str_n = str(bin(n))[2:]
            needed_zeros = N - len(bin_str_n)

            for i in range(0,needed_zeros):
                bin_str_n = "0" + bin_str_n

            options.append(list(bin_str_n))

        dirname = IMAGE[:3]

        print(os.path.basename(os.getcwd()))
        if not os.path.isdir(str(os.chdir(os.path.dirname(os.path.abspath(__file__))+"//"+dirname))) and os.path.basename(os.getcwd()) != "img":
            os.mkdir(dirname)
        os.chdir(os.path.dirname(os.path.abspath(__file__))+"//"+dirname)
            
        surfs = []
        for i in range(0,len(options)):
            surf = pygame.Surface((self.w,self.h))
            surf.blit(self.img,(0,0))

            for j in range(0,len(options[i])):
                if options[i][j] == "1":
                    pygame.draw.rect(surf,(0,0,0),self.rects[j],0)

            surfs.append(surf)

            label = 0
            for surf in surfs:
                pygame.image.save(surf, dirname + "_" + str(label) + ".png")
                label += 1

        print("done")
        return True
    
    def get_nth_digit_of_binary_number(n,d):
        bn = bin(n)
        return False
            
pygame.init()
g = Game()
g.main()



