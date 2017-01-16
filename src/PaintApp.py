#!/usr/bin/env/python

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line, Rectangle

from colors import *

class ColorSwatch(Button):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.background_color = color
        self.background_normal = ''

    def on_press(self):
        MyPaintWidget.color = self.background_color

class ColorGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(ColorSwatch(RED))
        self.add_widget(ColorSwatch(BLUE))
        self.add_widget(ColorSwatch(GREEN))
        self.add_widget(ColorSwatch(BLACK))
        self.add_widget(ColorSwatch(WHITE))
        self.add_widget(ColorSwatch(BEIGE))

class SideBar(BoxLayout):
    pass

class MyPaintWidget(FloatLayout):
    color = BLACK
    draw_enabled = True

    def on_touch_move(self, touch):
        if touch.x > 100 and self.draw_enabled == True:
            touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_down(self, touch):
        if touch.x > 100:
            self.draw_enabled = True
            with self.canvas:
                Color(*self.color)
                d = 1.
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
        else:
            self.draw_enabled = False

class Main(FloatLayout):
    pass

class PaintApp(App):
                    
    def build(self):
        return Main()


     
if __name__ == '__main__':
    PaintApp().run()
