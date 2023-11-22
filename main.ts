scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.gameOver(false)
    game.setGameOverEffect(false, effects.melt)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.smiles)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (playerCat.vy == 0) {
        playerCat.vy = -150
    }
})
let playerCat: Sprite = null
scene.setBackgroundColor(9)
playerCat = sprites.create(assets.image`myImage`, SpriteKind.Player)
controller.moveSprite(playerCat, 100, 0)
tiles.setCurrentTilemap(tilemap`level1`)
playerCat.ay = 350
scene.cameraFollowSprite(playerCat)
