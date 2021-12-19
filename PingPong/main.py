# STEPS TO FOLLOW
#1  Create the app
#2   create the game
#3   build the game
#4   run the app


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

#NB: Latest Position = Current Velocity(direction and speed info) + Latst poaition, all in vector form
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


#build the game
class PongGame(Widget):
    pass

#Build the app
class PongApp(App):
    def build(self):
        return PongGame()

PongApp().run()
