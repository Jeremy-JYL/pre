PC = python3 ../../pre.py
CC = cc

all: mandel hanoi

mandel: mandel.c
	$(CC) mandel.c -o mandel

mandel.c:
	$(PC) mandel.b.p mandel.c

hanoi: hanoi.c
	$(CC) hanoi.c -o hanoi

hanoi.c:
	$(PC) hanoi.b.p hanoi.c
