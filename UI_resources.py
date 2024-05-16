import UI_gb

class Style():
    def __init__(self, color:tuple, hover_color:tuple=UI_gb.UNDEFINED_COLOR, clicked_color:tuple=UI_gb.UNDEFINED_COLOR, text_color:tuple=UI_gb.UNDEFINED_COLOR, text_anchor:tuple=(0.5, 0.5), font=UI_gb.DEFAULT_FONT) -> None:
        self.color = color
        self.hover_color = hover_color
        self.clicked_color = clicked_color

        self.text_color = text_color
        self.text_anchor = text_anchor
        self.font = font