import os
import pygame
import platform

opsys = platform.system()

sounds_folder = "sounds"

pygame.mixer.init()
music = pygame.mixer.music

playing = ""
idx = -1
paused = False

volume_step = 1

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def get_sounds():
	return os.listdir(sounds_folder)

def get_name_idx(idx):
	return get_sounds()[clamp(idx, 0, len(get_sounds()) - 1)]

def set_playing(name):
	playing = name
	music.load(f"{sounds_folder}/{name}")
	music.play()

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
			idx = clamp(idx + 1, 0, len(get_sounds()) - 1)
			set_playing(get_name_idx(idx))
			clear()
			print(get_name_idx(idx))
		elif dec == 2:
			idx = clamp(idx - 1, 0, len(get_sounds()) - 1)
			set_playing(get_name_idx(idx))
			clear()
			print(get_name_idx(idx))
		elif dec == 3:
			paused = not paused

			if paused:
				music.pause()
				clear()
				print(get_name_idx(idx))
			else:
				music.unpause()
				clear()
				print(get_name_idx(idx))
