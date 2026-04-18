from engine.core import Game
from scenes.level1 import Level1
from scenes.level2 import Level2

game = Game()

game.scene_manager.load_scene(Level1)

game.run()