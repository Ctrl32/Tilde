import UI
import UI_gb
from UI_resources import Style
# here the ui is actually used

base_style = Style((255, 100, 0), text_color=(255, 255, 255))


root = UI.Node()
UI.root = root

panel0 = UI.Panel(Style((255, 0, 0)), max_size=(None, None), min_size=(100, 100))
panel1 = UI.Panel(Style((0, 255, 0)))
panel2 = UI.Panel(Style((0, 0, 255)))

stack0 = UI.Stack(UI_gb.VERTICAL)

stack0.add_child(panel0)
stack0.add_child(panel1)
stack0.add_child(panel2)


root.add_child(stack0)
