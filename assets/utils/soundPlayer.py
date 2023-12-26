import pygame

pygame.mixer.init()


class SoundPlayer():
    def __init__(self) -> None:
        soundsDir = "./assets/sounds"
        self.sounds = {
            'beginning_sound': f"{soundsDir}/pacman_beginning.wav",
            'siren_sound': f"{soundsDir}/pacman_siren.mp3",
            'chomp_sound': f"{soundsDir}/pacman_chomp_new.wav",
            'eatFruit_sound': f"{soundsDir}/pacman_eatfruit.wav",
            'eatGhost_sound': f"{soundsDir}/pacman_eatghost.wav",
            'death_sound': f"{soundsDir}/pacman_death.wav",
            'intermission_sound': f"{soundsDir}/pacman_intermission.wav",
            'extraPac_sound': f"{soundsDir}/pacman_extrapac.wav",
        }

    def playSoundAtChannel(self, channel: int, s: str):
        sound = pygame.mixer.Sound(self.sounds[s])
        pygame.mixer.Channel(channel).play(sound, loops=-1)
        sound.set_volume(0.4)

    def playSound(self, sound: str):
        pygame.mixer.music.load(self.sounds[sound])
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()

    def takePauseForSomeTime(self, pauseTime=4_000):
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(pauseTime)
