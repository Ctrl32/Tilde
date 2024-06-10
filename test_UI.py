import UI
import UI_gb
from UI_resources import Style
# here the ui is actually used

base_style = Style((255, 100, 0), text_color=(255, 255, 255))


root = UI.Node()
UI.root = root

main_stack = UI.Stack(UI_gb.HORIZONTAL)

hpanel0 = UI.Panel(Style((255, 0, 0)), min_size=(100, 100))
hpanel1 = UI.Panel(Style((0, 255, 0)))
hpanel2 = UI.Panel(Style((0, 0, 255)))

hstack = UI.Stack(UI_gb.HORIZONTAL)
hstack.add_child(hpanel0)
hstack.add_child(hpanel1)
hstack.add_child(hpanel2)

vpanel0 = UI.Panel(Style((255, 0, 0)), max_size=(100, 100), min_size=(100, 100))
vpanel1 = UI.Panel(Style((0, 255, 0)))
vpanel2 = UI.Panel(Style((0, 0, 255)))

vstack = UI.Stack(UI_gb.VERTICAL)
vstack.add_child(vpanel0)
vstack.add_child(vpanel1)
vstack.add_child(vpanel2)



main_stack.add_child(vstack)
main_stack.add_child(hstack)



root.add_child(main_stack)
