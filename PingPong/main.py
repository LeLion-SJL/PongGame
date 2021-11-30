# STEPS TO FOLLOW
#1  Create the app
#2   create the game
#3   build the game
#4   run the app


from kivy.app import App
from kivy.uix.widget import Widget

#build the game
class PongGame(Widget):
    pass

#Build the app
class PongApp(App):
    def build(self):
        return PongGame()

PongApp().run()
