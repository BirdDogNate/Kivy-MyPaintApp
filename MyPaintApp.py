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

        self.cols = 2
        self.padding = 3, 3, 3, 3
        self.spacing = 3, 3
        self.border = 20, 20
        self.add_widget(ColorSwatch(RED))
        self.add_widget(ColorSwatch(BLUE))
        self.add_widget(ColorSwatch(GREEN))
        self.add_widget(ColorSwatch(BLACK))
        #self.add_widget(ColorSwatch(WHITE))

class SideBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self.resize, 0)
        self.resize()

    def resize(self, *args):
        with self.canvas.before:
            Color(*BEIGE)
            Rectangle(pos=self.pos, size=self.size)

class MyPaintWidget(FloatLayout):
    color = BLACK

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.resize, 0)

    def resize(self, *args):
        with self.canvas.before:
            Color(*WHITE)
            Rectangle(pos=self.pos, size=self.size)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            d = 1.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

class MyPaintApp(App):
                    
    def build(self):
       parent = FloatLayout()

       self.painter = MyPaintWidget()

       bar = SideBar(orientation='vertical', pos=(0,0), size_hint=(None, 1), width=100)

       clearbtn = Button(text='clear', size_hint=(1, None), height=100)
       clearbtn.bind(on_release=self.clear_canvas)

       bar.add_widget(ColorGrid())
       bar.add_widget(clearbtn)
       parent.add_widget(self.painter)
       parent.add_widget(bar)

       Window.bind(on_resize=bar.resize)
       Window.bind(on_resize=self.painter.resize)
       return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

     
if __name__ == '__main__':
    MyPaintApp().run()
