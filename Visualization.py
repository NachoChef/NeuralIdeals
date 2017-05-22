from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

class VisualizeWidget():
    def __init__(self, **kwargs):
        super(VisualizeWidget, self).__init__()
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 1)
            Ellipse(pos=(10,10), size=(20))

class MyDisp(App):
    def build(self):
        return VisualizeWidget

if __name__ == '__main__':
    MyDisp.run()