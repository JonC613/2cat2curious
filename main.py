def on_overlap_tile(sprite, location):
    game.game_over(False)
    game.set_game_over_effect(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
    game.set_game_over_effect(True, effects.smiles)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile2)

def on_a_pressed():
    if playerCat.vy == 0:
        playerCat.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

playerCat: Sprite = None
scene.set_background_color(9)
playerCat = sprites.create(img("""
        e e e . . . . e e e . . . . 
            c d d c . . c d d c . . . . 
            c b d d f f d d b c . . . . 
            c 3 b d d b d b 3 c . . . . 
            f b 3 d d d d 3 b f . . . . 
            e d d d d d d d d e . . . . 
            e d f d d d d f d e . b f b 
            f d d f d d f d d f . f d f 
            f b d d b b d d 2 f . f d f 
            . f 2 2 2 2 2 2 b b f f d f 
            . f b d d d d d d b b d b f 
            . f d d d d d b d d f f f . 
            . f d f f f d f f d f . . . 
            . f f . . f f . . f f . . .
    """),
    SpriteKind.player)
controller.move_sprite(playerCat, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
playerCat.ay = 350
scene.camera_follow_sprite(playerCat)