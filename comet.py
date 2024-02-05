import pygame
import random

# cree une classe pour gerer cette comete 
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # charge l'image de la comete
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de commttes est de 0
        if len(self.comet_event.all_comets) == 0:
            # remmetre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre de nouveau les 2 monstres 
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity


        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()
            self.comet_event.game.score += 10

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                # remmetre la jauge au depart 
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False



        # verifier si la boule de feu touche le joueur 
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # subir 20 point de degats
            self.comet_event.game.player.damage(20)
