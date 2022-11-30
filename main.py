# Import all modules
import os
import pygame
import platform

#// Some variables
opsys = platform.system()

sounds_folder = "sounds"

pygame.mixer.init()
music = pygame.mixer.music

playing = ""
idx = -1
paused = False
#//

# Clamp function (very useful)
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#// Functions relationated with sounds
def get_sounds():
	return os.listdir(sounds_folder)

def get_name_idx(idx):
	return get_sounds()[clamp(idx, 0, len(get_sounds()) - 1)]

def set_playing(name):
	playing = name
	music.load(f"{sounds_folder}/{name}")
	music.play()
#//

# Clear function, with the platform module i can make this project compatible with Windows and Linux
def clear():
	if opsys == "Windows":
		os.system("cls")
	if opsys == "Linux":
		os.system("clear")

clear()

if __name__ == "__main__":
	while True:
		dec = int(input())

		if dec == 1:
			# Code for going to the next sound
			idx = clamp(idx + 1, 0, len(get_sounds()) - 1)
			set_playing(get_name_idx(idx))
			clear()
			print(get_name_idx(idx))
		elif dec == 2:
			# Code for going to the previous sound
			idx = clamp(idx - 1, 0, len(get_sounds()) - 1)
			set_playing(get_name_idx(idx))
			clear()
			print(get_name_idx(idx))
		elif dec == 3:
			# Code for the pause/unpause command
			paused = not paused

			if paused:
				music.pause()
				clear()
				print(get_name_idx(idx))
			else:
				music.unpause()
				clear()
				print(get_name_idx(idx))
