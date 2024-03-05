import kivy
from kivymd.app import App

from kivy.uix.pagelayout import PageLayout

from kivy.uix.button import Button


from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')

class PageLayout(PageLayout):
    def __init__(self):


        super(PageLayout, self).__init__()

        btn1 = Button(text = 'Page 1', background_color = (0, 1, .5))
        btn2 = Button(text = 'Page 2', background_color = (1, 1, .5))
        btn3 = Button(text = 'Page 3', background_color = (0, .5, .5))
        btn4 = Button(text = 'Page 4', background_color = (0, .5, 1))

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)

class Page_LayoutApp(App):


    def build(self):
        return PageLayout()
    
    if __name__ == '__main__':
        Page_LayoutApp().run()
