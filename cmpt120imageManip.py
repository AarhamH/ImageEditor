#Image Processing Manip
#Author: Aarham Haider
#Date: 11/10/21

import cmpt120imageProjHelper as picture

image=picture.getImage('project-photo.jpg')

#apply red filter
def applyRed(pixels):
  #input: pixels
  #output: pixels in with only red components

  height=len(pixels)
  width=len(pixels[0])

  #create new black image to apply pixels to new image
  canvas = picture.getBlackImage(width,height)

  for row in range (height):
    for col in range(width):
      pixel = pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #set b,g to 0 to only have red
      pixels[row][col]=[r,0,0]

      canvas[row][col]=pixels[row][col]

  return canvas

#apply blue filter
def applyBlue(pixels):
  #input: pixels
  #output: pixels in with only blue 

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(width,height)

  for row in range (height):
    for col in range(width):
      pixel = pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #set r,g to 0 to only have blue
      pixels[row][col]=[0,0,b]

      canvas[row][col]=pixels[row][col]


  return canvas

#apply green filter
def applyGreen(pixels):
  #input: pixels
  #output: pixels in with only green components

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(width,height)
  
  for row in range (height):
    for col in range(width):
      pixel = pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #set r,b to 0 to only have green
      pixels[row][col]=[0,g,0]

      canvas[row][col]=pixels[row][col]

  return canvas

#apply sepia filter
def applySepia(pixels):
  #input: pixels
  #output: pixels in with only r,g,b corresponding to sepia formula

  height=len(pixels)
  width=len(pixels[0])

  canvas=picture.getBlackImage(width,height)

  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r= pixel[0]
      g= pixel[1]
      b= pixel[2]

      #create sepia RGB values
      sepiaRed = (r*0.393 + g*0.769 + b*0.189)
      sepiaGreen = (r*0.349 + g*0.686 + b*0.168)
      sepiaBlue = (r*0.272 + g*0.534 + b*0.131)

      #determine sepia limits
      if sepiaRed > 255:
        sepiaRed = 255

      if sepiaGreen > 255:
        sepiaGreen = 255

      if sepiaBlue >255:
        sepiaBlue = 255

      pixels[row][col]=(sepiaRed,sepiaGreen,sepiaBlue)

      canvas[row][col]=pixels[row][col]

  return canvas

#scale values
def scaleUp(value):
  #input: arbitrary value; will be used for r,g,b values
  #output: modified/scaled value; will modify r,g,b values

  if value<64:
    value=value/(64*80)
  elif 64<= value <128:
    value=(value-64)/(128-64)*(160-80)+80
  else:
    value=(value-128)/(255-128)*(255-160)+160
      
  return value

def scaleDown(value):
  #input: arbitrary value; will be used for r,g,b values
  #output: modified/scaled value; will modify r,g,b values

  if value<64:
    value=value/(64*50)
  elif 64 <= value <128:
    value=(value-64)/(128-64) * (100-50) + 50
  else:
    value=(value-128)/(255-128) * (255-100) + 100
  return value

#warm filter
def applyWarm(pixels):
  #input: pixels
  #output: pixels with scaled up r, scaled down b

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(width,height)

  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #change r & b with scaled values
      warmR = scaleUp(r)
      warmB = scaleDown(b)

      pixels[row][col]=(warmR,g,warmB)

      canvas[row][col]=pixels[row][col]

  return canvas

#cold filter
def applyCold(pixels):
  #input: pixels
  #output: pixels with scaled down r, scaled up b

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(width,height)

  for row in range(height):
    for col in range(width):

      pixel = pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #change r & b with scaled values
      coldR = scaleDown(r)
      coldB = scaleUp(b)

      pixels[row][col]=[coldR,g,coldB]
    
      canvas[row][col]=pixels[row][col]

  return canvas


#rotate counterclockwise
def rotateImageLeft(pixels):
  #input: pixels
  #output: pixels with height and width reversed, rotates image counter-clockwise

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(height,width)
  
  for row in range(height):
    for col in range(width):

      #translate pixel to rotated black image
      canvas[width-1-col][row]=pixels[row][col]
  
  return canvas

#rotate clockwise
def rotateImageRight(pixels):
  #input: pixels
  #output: pixels with height and width reversed, rotates image clockwise

  height=len(pixels)
  width=len(pixels[0])

  canvas = picture.getBlackImage(height,width)

  for row in range(height):
    for col in range(width):

      #translate pixel to rotated black image
      canvas[col][height-1-row]=pixels[row][col]
  
  return canvas

#zoom image
def zoomImage(pixels):
  #input: pixels
  #output: pixels translated on doubled dimension black image, creating biggger image

  height=len(pixels)
  width=len(pixels[0])

  #create black image with *2 the dimensions
  canvas = picture.getBlackImage(width*2,height*2)

  for row in range(height):
    for col in range(width):

      pixel=pixels[row][col]

      #translate pixel to 2x2 canvas pixel
      canvas[2*row][2*col]=pixel
      canvas[2*row][2*col+1]=pixel
      canvas[2*row+1][2*col]=pixel
      canvas[2*row+1][2*col+1]=pixel

  
  return canvas

#half image
def halfImage(pixels):
  #input: pixels
  #output: pixels translated on halfed dimensions, creating smaller image

  height=len(pixels)
  width=len(pixels[0])

  #take away pixel if dimension is odd
  if height %2 != 0:
    height -=1

  if width %2 !=0:
    width -=1

  #create black image with half the dimension
  canvas = picture.getBlackImage(width//2,height//2)
  
  blankrow= len(canvas)
  blankcol= len(canvas[0])

  for row in range(blankrow):
    for col in range(blankcol):

      #determine pixels on the top left of the image
      p1 = pixels[row*2][col*2]
      p2 = pixels[row*2][col*2+1]
      p3 = pixels[row*2+1][col*2]
      p4 = pixels[row*2+1][col*2+1]

      #find average rgb based off of the pixel location and index
      averageR = (p1[0]+p2[0]+p3[0]+p4[0])/4
      averageG = (p1[1]+p2[1]+p3[1]+p4[1])/4
      averageB = (p1[2]+p2[2]+p3[2]+p4[2])/4


      #translate average rgb to black image
      canvas[row][col]=(averageR,averageG,averageB)

  return canvas

def fishBox(pixels):
  #input: pixels
  #output: a green box determined by hsv value of the pixels

  height=len(pixels)
  width=len(pixels[0])

  #create empty lists for length and width
  yellowListRow=[]
  yellowListCol=[]

  for row in range(height):
    for col in range(width):
      pixel=pixels[row][col]
      r=pixel[0]
      g=pixel[1]
      b=pixel[2]

      #use hsv function to convert rgb to tuple hsv
      hsv=picture.rgb_to_hsv(r,g,b)

      #save row/col in list if pixel is yellow
      if 53<=hsv[0]<=63 and 45<=hsv[1]<=55 and 90<=hsv[2]<=100:
        yellowListRow.append(row)
        yellowListCol.append(col)

  #find max/min rows
  for i in yellowListRow:
    maxRow=max(yellowListRow)
    minRow=min(yellowListRow)

  #find max/min columns
  for i in yellowListCol:
    maxCol=max(yellowListCol)
    minCol=min(yellowListCol)

  #draw box based on the dimensions of the box
  for row in pixels[minRow]:
    for col in range(minCol,maxCol):
      pixels[minRow][col]=[0,255,0]

  for row in pixels[maxRow]:
    for col in range(minCol,maxCol):
      pixels[maxRow][col]=[0,255,0]

  for row in range(minRow,maxRow):
    pixels[row][minCol]=[0,255,0]
    
  for row in range(minRow,maxRow):
    pixels[row][maxCol]=[0,255,0]


  return pixels

