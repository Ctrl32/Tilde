import pygame
import UI_gb
import UI_resources

ui_surf = pygame.Surface(UI_gb.ui_surf_size)

root = None

def update():
    global ui_surf
    ui_surf = pygame.Surface(UI_gb.ui_surf_size)
    root.size = UI_gb.ui_surf_size
    root.update()
    return ui_surf


class Node():
    def __init__(self, z_idx:int=None) -> None:
        #is the index in the ui elements list
        #gets set in the global update()
        self.z_idx = z_idx
        self.visible = True

        self.pos = [0, 0]
        self.size = list(UI_gb.ui_surf_size)
        self.children = []

    def update(self):
        for child in self.children:
            child.pos = self.pos
            child.size = self.size
            child.update()
    
    def add_child(self, child:object, idx:int=None):
        if idx == None:
            self.children.append(child)
            return
        self.children.insert(idx, child)

    def delete_child(self, child:object):
        self.children.remove(child)

class Stack(Node):
    def __init__(self, direction:tuple, z_idx: int=None) -> None:
        #direction cannot have negative integers

        self.direction = direction
        super().__init__(z_idx)

    def pack(self):

        if self.direction == UI_gb.HORIZONTAL:
            child_step = [self.size[0], 0]
            if len(self.children) != 0:
                child_step[0] = int(self.size[0]/len(self.children)) + 1

            child_size = (child_step[0], self.size[1])

        elif self.direction == UI_gb.VERTICAL:
            child_step = [0, self.size[1]]
            if len(self.children) != 0:
                child_step[1] = int(self.size[1]/len(self.children)) + 1

            child_size = (self.size[0], child_step[1])


        for i, child in enumerate(self.children):
            child.pos[0] = i*child_step[0] + self.pos[0]
            child.pos[1] = i*child_step[1] + self.pos[1]
            
            child.size = child_size


    def update(self):
        if self.visible:   
            self.pack()

            for child in self.children:
                child.update()

class Panel(Node):
    def __init__(self, style:UI_resources.Style, text:str="", z_idx: int=None) -> None:
        super().__init__(z_idx)
        self.style = style
        self.text = text

    def render(self):
        #draw background
        rect = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(ui_surf, self.style.color, rect)

        #draw text
        text_surf = self.style.font.render(self.text, True, self.style.text_color)

        text_offset = ((self.size[0]-text_surf.get_width()) * self.style.text_anchor[0], (self.size[1]-text_surf.get_height()) * self.style.text_anchor[1])
        ui_surf.blit(text_surf, (round(self.pos[0] + text_offset[0]), round(self.pos[1] + text_offset[1])))
        



    def update(self):
        if self.visible:
            self.render()

            for child in self.children:
                child.update()
