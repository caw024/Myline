from display import *
#eq of line is Ax+By+C=0

def draw_line( x0, y0, x1, y1, screen, color):
   A = y1 - y0 #change in y
   B = x0 - x1 #negative change in x
   x = x0
   y = y0
   if B==0:
      while y <= y1:
         plot(screen,color,x,y)
         y+=1
   else:
      m = -1.0*A/B #slope  #octant 1
      if ((1 > m) & (m >= 0)):
         d = 2*A + B
         while x <= x1:
            plot(screen,color,x,y)
            if d>0: #above line
               y+=1
               d+= 2*B
            x+=1
            d+=2*A             #octant 2
      elif m >= 1:
         d = 2*B + A
         while y<= y1:
            plot(screen, color,x,y)
            if d<0:
               x+=1
               d+=2*A
            y+=1
            d+=2*B
            #octant 8 - not done     
      elif ((-1 < m) & (m < 0)):
         d = 2*A-B
         while x <= x1:
            plot(screen,color,x,y)
            if d<=0:
               y-=1
               d-=2*B
            x+=1
            d+=2*A  #octant 7 - not done
      else:
         d = A - 2*B
         while y >= y1:
            plot(screen, color,x,y)
            if d>0:
               x+=1
               d+=2*A
            y-=1
            d-=2*B

pass
