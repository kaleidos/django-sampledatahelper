import math
import random
            
class ImgSimple(object):
    def generate(self, sd, im, width, height):
        draw = ImageDraw.Draw(im)
        draw.rectangle([0,0,width,height], fill= "rgb(%d,%d,%d)"%(1+sd.int(255),1+sd.int(255),1+sd.int(255)))
        draw.text((0, 0), sd.word(), font=sd.ttf_font)
        im.rotate(45)
        return im

class ImgPlasma(object):
    def generate(self, sd, im, width, height):
        # image size
        roughness = random.randint(2, 5)
        self.im = im
        self.im.putpixel((0,0),random.randint(0, 255))
        self.im.putpixel((width-1,0),random.randint(0, 255))
        self.im.putpixel((width-1,height-1),random.randint(0, 255))
        self.im.putpixel((0,height-1),random.randint(0, 255))
        self.subdivide(0,0,width-1,height-1)
        return self.im
        
    def adjust(self, xa, ya, x, y, xb, yb):
        if(self.im.getpixel((x,y)) == 0):
          d=math.fabs(xa-xb) + math.fabs(ya-yb)
          v=(self.im.getpixel((xa,ya)) + self.im.getpixel((xb,yb)))/2.0 \
             + (random.random()-0.5) * d * roughness
          c=int(math.fabs(v) % 256)
          self.im.putpixel((x,y), c)
    
    def subdivide(self, x1, y1, x2, y2):
        if(not((x2-x1 < 2.0) and (y2-y1 < 2.0))):
            x=int((x1 + x2)/2.0)
            y=int((y1 + y2)/2.0)
            self.adjust(x1,y1,x,y1,x2,y1)
            self.adjust(x2,y1,x2,y,x2,y2)
            self.adjust(x1,y2,x,y2,x2,y2)
            self.adjust(x1,y1,x1,y,x1,y2)
            if(self.im.getpixel((x,y)) == 0):
                v=int((self.im.getpixel((x1,y1)) + self.im.getpixel((x2,y1)) \
                   + self.im.getpixel((x2,y2)) + self.im.getpixel((x1,y2)))/4.0)
                self.im.putpixel((x,y),v)
    
            self.subdivide(x1,y1,x,y)
            self.subdivide(x,y1,x2,y)
            self.subdivide(x,y,x2,y2)
            self.subdivide(x1,y,x,y2)


class ImgMandelbrot(object):
    def generate(self, sd, im, width, height):
        xa = sd.float(-2, 2)
        xb = sd.float(-2, 2)
        ya = sd.float(-2, 2)
        yb = sd.float(-2, 2)
        maxIt = 20 # max iterations allowed
        
        for y in range(height):
            zy = y * (yb - ya) / (height - 1)  + ya
            for x in range(width):
                zx = x * (xb - xa) / (width - 1)  + xa
                z = zx + zy * 1j
                c = z
                for i in range(maxIt):
                    if abs(z) > 2.0: break 
                    z = z * z + c
                im.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
        return im
