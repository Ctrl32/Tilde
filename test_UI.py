import UI
import UI_gb
import UI_resources
# here the ui is actually used

base_style = UI_resources.Style((255, 100, 0), text_color=(255, 255, 255))


root = UI.Node()
UI.root = root

mystack1 = UI.Stack(UI_gb.HORIZONTAL)
mystack2 = UI.Stack(UI_gb.VERTICAL)
mystack3 = UI.Stack(UI_gb.HORIZONTAL)

mypanel1 = UI.Panel(base_style, "abc")
mypanel2 = UI.Panel(UI_resources.Style((0, 100, 255)), "def")
mypanel3 = UI.Panel(UI_resources.Style((0, 255, 0)), "ghi")

mypanel4 = UI.Panel(UI_resources.Style((100, 100, 255)), "123")
mypanel5 = UI.Panel(UI_resources.Style((200, 0, 255)), "456")
mypanel6 = UI.Panel(UI_resources.Style((150, 255, 30)), "789")

mystack2.add_child(mypanel1)
mystack2.add_child(mypanel2)
mystack2.add_child(mypanel3)

mystack3.add_child(mypanel4)
mystack3.add_child(mypanel5)
mystack3.add_child(mypanel6)

mystack1.add_child(mystack2)
mystack1.add_child(mystack3)

root.add_child(mystack1)
