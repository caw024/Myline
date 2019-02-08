from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
        A = y1 - y0
        B = x0 - x1
        m = -A/B

        x = x0
        y = y0

        #octant 1
        if (1 > m) & (m >= 0):
                d = 2*A + B
                while x <= x1:
                        plot(x,y)
                        if d>0:
                                y++
                                d+= 2*B
                x++
                d+=2*A
                                #octant 2
        else if m >= 1:
            d = 2*B + A
            while y<= y1:
                plot(x,y)
                if d<0:
                    x++
                    d+= 2*A
                    y++
                    d+=2*B
            
                    #octant 3 - not done
        else if (-1 < m) & (m < 0):
        d = 2*A + B
        while x <= x1:
            plot(x,y)
            if d>0:
            y++
                d+= 2*B
                x++
            d+=2*A
        
    #octant 4 - not done
    else if (-1 <= m):
    d = 2*A + B
    while x <= x1:
            plot(x,y)
            if d>0:
                y++
                d+= 2*B
                x++
                d+=2*A
