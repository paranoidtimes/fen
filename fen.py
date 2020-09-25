#!/usr/bin/python3

import sys
from PIL import Image, ImageDraw

position = sys.argv[1]
rows = position.split("/")
active = sys.argv[2]

board = Image.new("RGBA", (352, 352))
board.paste((188,143,143), (0,0,352,352))


turn = { 'w' : "WHITE",
         'b' : "BLACK",
}

images = { 'p' : Image.open('images/bpawn.png'),
           'k' : Image.open('images/bking.png'),
           'r' : Image.open('images/brook.png'),
           'q' : Image.open('images/bqueen.png'),
           'n' : Image.open('images/bknight.png'),
           'b' : Image.open('images/bbishop.png'),
           'P' : Image.open('images/wpawn.png'),
           'K' : Image.open('images/wking.png'),
           'R' : Image.open('images/wrook.png'),
           'Q' : Image.open('images/wqueen.png'),
           'N' : Image.open('images/wknight.png'),
           'B' : Image.open('images/wbishop.png'),
}

def square_color():
    if square_color.counter % 2 == 1:
        color = 205,133,63 # brown
    else:
        color = 255,255,255
    if square_color.tracker % 8 == 0:
        square_color.tracker = 0
        square_color.counter += 1
    square_color.counter += 1
    square_color.tracker += 1
    return color

square_color.counter = 0
square_color.tracker = 1

rank = 0
for row in rows:
    ypixel = rank * 39 + 20
    squares = list(row)
    x = 0
    for square in squares:
        xpixel = x * 39 + 20
        if square.isdigit():
            for y in range(0, int(square)):
                board.paste(square_color(), (xpixel,ypixel,xpixel + 39,ypixel + 39))
                x += 1
                xpixel = x * 39 + 20
        else:
            board.paste(square_color(), (xpixel,ypixel,xpixel + 39,ypixel + 39))
            board.paste(images[square], (xpixel,ypixel), mask=images[square])
            x += 1
    rank += 1

draw = ImageDraw.Draw(board)
draw.ellipse((331, 331, 351, 351), fill = turn[active], outline ='gray')
board.save('board.png')
