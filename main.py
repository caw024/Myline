from display import *
from draw import *

screen = new_screen()

'''
#O1
color = [ 0, 255, 0 ]
draw_line(0,0,200,100,screen,color)


#O2
color = [ 255, 0, 0 ]
draw_line(50,0,150,200,screen,color)


#O8
color = [ 0, 255, 0 ]
draw_line(0,95,200,90,screen,color)


#O7
color = [ 0, 255, 255 ]
draw_line(45,120,60,62,screen,color)


'''

n = 500
while (n >= 0):
    color = [n % 255, (-1 * n) % 255, 255]
    draw_line(0,n,500-n,0,screen,color)
    n-=2




display(screen)
save_extension(screen, 'img.png')
