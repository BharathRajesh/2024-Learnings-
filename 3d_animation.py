from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

ground = Entity(
    model='plane',
    texture='grass',
    collider='box',  # I've changed collider to 'box' assuming you want a simple collision box
    scale=(100, 1, 100)
)

app.run()
