from engine.game import Game
from game.scenes.level1 import Level1
from game.scenes.level2 import Level2

def start_game():
    game = Game()

    game.scene_manager.cache_scene('level1', Level1)
    game.scene_manager.cache_scene('level2', Level2)

    game.scene_manager.load_scene("level1")

    game.run()