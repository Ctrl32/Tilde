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
    def __init__(self, z_idx:int=None, min_size:tuple=(None, None), max_size:tuple=(None, None)) -> None:
        #is the index in the ui elements list
        #gets set in the global update()
        self.z_idx = z_idx
        self.visible = True

        self.pos = [0, 0]
        self.size = list(UI_gb.ui_surf_size)
        self.children = []

        self.min_size = min_size
        self.max_size = max_size

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
    def __init__(self, direction:tuple, z_idx: int=None, min_size:tuple=(None, None), max_size:tuple=(None, None)) -> None:
        #direction cannot have negative integers

        self.direction = direction
        super().__init__(z_idx, min_size, max_size)

    def pack(self):

        if self.direction == UI_gb.HORIZONTAL and len(self.children) != 0:
            child_size = [self.size[0]/len(self.children), self.size[1]]

            available_width = self.size[0]
            unconstrained_count = 0
            for child in self.children:
                constrained = False
                # Determine the child's size based on constraints
                if child.min_size[0] != None and child.max_size[0] != None:
                    child.size[0] = clip(child_size[0], child.min_size[0], child.max_size[0])
                    child.size[1] = child_size[1]
                    constrained = True
                elif child.max_size[0] !=  None:
                    child.size[0] = min(child_size[0], child.max_size[0])
                    child.size[1] = child_size[1]
                    constrained = True
                elif child.min_size[0] !=  None:
                    child.size[0] = max(child_size[0], child.min_size[0])
                    child.size[1] = child_size[1]
                    constrained = True
                else:
                    child.size = child_size
                    unconstrained_count += 1
                
                if constrained:
                    available_width -= child.size[0]

            unconstrained_size = available_width/unconstrained_count

            offset = 0
            for child in self.children:
                if child.min_size[0] == None and child.max_size[0] == None:
                    child.size[0] = unconstrained_size

                child.pos[0] = offset
                offset += child.size[0]
            

        elif self.direction == UI_gb.VERTICAL and len(self.children) != 0:
            child_size = [self.size[0], self.size[1]/len(self.children)]

            available_height = self.size[1]
            unconstrained_count = 0
            for child in self.children:
                constrained = False
                # Determine the child's size based on constraints
                if child.min_size[1] != None and child.max_size[1] != None:
                    child.size[1] = clip(child_size[1], child.min_size[1], child.max_size[1])
                    child.size[0] = child_size[0]
                    constrained = True
                elif child.max_size[1] !=  None:
                    child.size[1] = min(child_size[1], child.max_size[1])
                    child.size[0] = child_size[0]
                    constrained = True
                elif child.min_size[1] !=  None:
                    child.size[1] = max(child_size[1], child.min_size[1])
                    child.size[0] = child_size[0]
                    constrained = True
                else:
                    child.size = child_size
                    unconstrained_count += 1
                
                if constrained:
                    available_height -= child.size[1]

            unconstrained_size = available_height/unconstrained_count

            offset = 0
            for child in self.children:
                if child.min_size[1] == None and child.max_size[1] == None:
                    child.size[1] = unconstrained_size

                child.pos[1] = offset
                offset += child.size[1]

    def update(self):
        if self.visible:   
            self.pack()

            for child in self.children:
                child.update()

class Panel(Node):
    def __init__(self, style:UI_resources.Style, text:str="", z_idx: int=None, min_size:tuple=(None, None), max_size:tuple=(None, None)) -> None:
        super().__init__(z_idx)
        self.style = style
        self.text = text
        self.min_size = min_size
        self.max_size = max_size

    def render(self):
        #draw background
        rect_size = (int(self.size[0])+1, int(self.size[1])+1)
        rect = pygame.Rect(self.pos, rect_size)
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



def clip(value, lower, upper):
    if value < lower: return lower
    if value > upper: return upper
    return value