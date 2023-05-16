x=1
def setup(): 
    size (800,800)
    background (1)
def draw (): 
    strokeWeight (0)
    frameRate (10)
    global x
    fill(0,0,210)
    ellipse (random(10,790),x,5,5)
    x=x+2
    fill (150)
    ellipse (100,100,100,100)
    fill (190)
    ellipse (110,110,40,40)
    ellipse (90,90,25,25)
    fill (0,200,0)
    rect (0,700,800,100)
