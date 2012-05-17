import math
from PIL import Image, ImageDraw
            
class ImgSimple(object):
    def generate(self, sd, width, height):
        im = Image.new("RGBA", (width, height))
        bg = Image.new("RGBA", (width, height), (1+sd.int(254),1+sd.int(254),1+sd.int(254), 255))
        draw = ImageDraw.Draw(im)
        draw.text((sd.int(width/2), sd.int(height/2)), sd.word(), font=sd.ttf_font, fill="rgb(%d,%d,%d)" % (1+sd.int(255),1+sd.int(255),1+sd.int(255)))
        im = im.rotate(-sd.int(90))
        bg.paste(im, (0,0), im)
        return bg

class ImgPlasma(object):
    def generate(self, sd, width, height):
        self.sd = sd
        im = Image.new("L", (width, height))
        bg = Image.new("RGBA", (width, height), (1+sd.int(254),1+sd.int(254),1+sd.int(254), 255))
        # image size
        self.roughness = sd.int(2, 5)

        self.im = im
        self.im.putpixel((0,0), sd.int(255))
        self.im.putpixel((width-1,0), sd.int(255))
        self.im.putpixel((width-1,height-1), sd.int(255))
        self.im.putpixel((0,height-1), sd.int(255))
        self.subdivide(0,0,width-1,height-1)
        self.im = self.im.convert("RGBA")
        return Image.blend(self.im, bg, 0.5)
        
    def adjust(self, xa, ya, x, y, xb, yb):
        if(self.im.getpixel((x,y)) == 0):
          d=math.fabs(xa-xb) + math.fabs(ya-yb)
          v=(self.im.getpixel((xa,ya)) + self.im.getpixel((xb,yb)))/2.0 \
             + (self.sd.float(0, 1)-0.5) * d * self.roughness
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
    def generate(self, sd, width, height):
        im = Image.new("RGBA", (width, height))

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

class ImgIFS(object):
    def generate(self, sd, width, height):
        im = Image.new("RGBA", (width, height))
        bg = Image.new("RGBA", (width, height), (1+sd.int(254),1+sd.int(254),1+sd.int(254), 255))
        mats = []
        ### Fractint IFS definition of Fern
        mats.append([[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
                    [0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
                    [0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
                    [-0.15,0.28,0.26,0.24,0.0,0.44,0.07]])
        ### Fractint IFS definition of Dragon
        mats.append([[0.824074, 0.281482, -0.212346,  0.864198, -1.882290, -0.110607, 0.787473],
                    [0.088272, 0.520988, -0.463889, -0.377778,  0.785360,  8.095795, 0.212527]])
        ### Levy C curve
        mats.append([[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
                    [0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5]])

        # Levy Dragon
        mats.append([[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
                    [-0.5, -0.5, 0.5, -0.5, 1.0, 0.0, 0.5]])

        mat = sd.choice(mats)

        # image size
        imgx = width
        imgy = height
        
        m = len(mat)
        # find the xmin, xmax, ymin, ymax
        x = mat[0][4]
        y = mat[0][5] 
        #
        xa = x
        xb = x
        ya = y
        yb = y
        # 
        for k in range(imgx * imgy):
            p=sd.float(0, 1)
            psum = 0.0
            for i in range(m):
                psum += mat[i][6]
                if p <= psum:
                    break
            x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4] 
            y  = x * mat[i][2] + y * mat[i][3] + mat[i][5] 
            x = x0 
            #
            if x < xa:
                xa = x
            if x > xb:
                xb = x
            if y < ya:
                ya = y
            if y > yb:
                yb = y
        
        # drawing
        x=0.0
        y=0.0 
        colour = (sd.int(255), sd.int(255), sd.int(255))
        for k in range(imgx * imgy):
            p=sd.float(0, 1)
            psum = 0.0
            for i in range(m):
                psum += mat[i][6]
                if p <= psum:
                    break
            x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4] 
            y  = x * mat[i][2] + y * mat[i][3] + mat[i][5] 
            x = x0 
            jx = int((x - xa) / (xb - xa) * (imgx - 1)) 
            jy = (imgy - 1) - int((y - ya) / (yb - ya) * (imgy - 1))
            if jx >= 0 and jx < width and jy >= 0 and jy < height:
                im.putpixel((jx, jy), colour) 
        im = im.rotate(sd.int(360))
        bg.paste(im, (0,0), im)
        return bg

if __name__ == '__main__':
    from sampledatahelper import SampleDataHelper
    sd = SampleDataHelper()
    width = 640
    height = 480
    algorithms = {
            'simple': ImgSimple,
            'plasma': ImgPlasma,
            'mandelbrot': ImgMandelbrot,
            'ifs': ImgIFS,
    }
    for key, value in algorithms.iteritems():
        generator = value()
        im = generator.generate(sd, width, height)
        im.save("%s.png" % key)
