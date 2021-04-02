if pygame.sprite.collide_rect(player, ball):
        ball.collide(player.speed)