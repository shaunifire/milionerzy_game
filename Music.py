import pygame
from pygame import mixer
#Ok, guys pierwszy raz coś takiego robię także poprawcie mnie jeśli coś jest bardzo złe.
#Jest to alpha więc nie jest doskonała, tylko przykładowa. :/

mixer.init()
pygame.init()


while True:
    print("Witamy w Milionerach!")
    pygame.mixer.music.load("Czołóweczka.wav")
    pygame.mixer.music.play(1)
    print("Wciśnij 'p' by zacząć!")
    print("Wciśnij 'q' by zakończyć")
    znak=input()
    if znak=='p':
        pygame.mixer.music.stop()
        while True:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Constant.wav")
            pygame.mixer.music.play(-1)
            print("Jeśli jesteś gotowy, wciśnij '1'")
            znak1=input()
            if znak1=='1':
                print("oto pytanie:")
            else:
                break
    elif znak=='q':
        break
