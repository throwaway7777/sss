from PIL import Image, ImageDraw, ImageColor
import hashlib, math

#config
bitGlitterVersion = 1.0

class ColorSet:
    def __init__(self, name, description, bitLength, colorDictionary, defaultSet = False):
        self.name = name
        self.description = description
        self.bitLength = bitLength
        self.colorDictionary = colorDictionary
        self.defaultSet = defaultSet

oneBitColorSet = ColorSet("1 bit",
                          "Two colors, black and white.  While it has the lowest density of one bit of data per pixel, it has the highest reliability.",
                          1,
                          {'0':'rgb(0,0,0)', '1':'rgb(255,255,255)'},
                          True)

twoBitColorSet = ColorSet("2 bit",
                          "Four colors.",
                          2,
                          {'00':'rgb(0,0,0)', '01':'rgb(255,0,0)', '10':'rgb(0,255,0)', '11':'rgb(0,0,255)', },
                          True)

threeBitColorSet = ColorSet("3 bit",
                            "Eight colors.",
                            3,
                            {'000':'rgb(0,0,0)', '001':'rgb(255,0,0)', '010':'rgb(255,255,0)', '011':'rgb(0,255,0)',
                             '100':'rgb(0,255,255)', '101':'rgb(0,0,255)', '110':'rgb(255,0,255)', '111':'rgb(255,255,255)'},
                            True)

fourBitColorSet = ColorSet("4 bit",
                           "Sixteen colors.",
                           4,
                           {'0000':'rgb(0,0,0)', '0001':'rgb(128,128,128)', '0010':'rgb(192,192,192)', '0011':'rgb(128,0,0)',
                            '0100': 'rgb(255,0,0)', '0101':'rgb(128,128,0)', '0110':'rgb(255,255,0)', '0111':'rgb(0,255,0)',
                            '1000': 'rgb(0,128,128)', '1001':'rgb(0,128,0)', '1010':'rgb(0,0,128)', '1011':'rgb(0,0,255)',
                            '1100': 'rgb(0,255,255)', '1101':'rgb(128,0,128)', '1110':'rgb(255,0,255)', '1111':'rgb(255,255,255)'},
                           True)

fiveBitColorSet = ColorSet("5 bit",
                           "Thirty-two colors.",
                           5,
                           {'00000':'rgb(0,0,0)', '00001':'rgb(0,255,0)', '00010':'rgb(255,0,0)', '00011':'rgb(0,0,255)',
                            '00100': 'rgb(0,255,255)', '00101':'rgb(255,0,255)', '00110':'rgb(255,255,0)', '00111':'rgb(255,255,255)',
                            '01000': 'rgb(128,0,0)', '01001':'rgb(0,0,128)', '01010':'rgb(255,0,128)', '01011':'rgb(128,0,255)',
                            '01100': 'rgb(0,128,0)', '01101':'rgb(255,128,0)', '01110':'rgb(255,128,255)', '01111':'rgb(0,128,255)',
                            '10000': 'rgb(128,255,0)', '10001':'rgb(255,255,128)', '10010':'rgb(128,255,255)', '10011':'rgb(0,255,128)',
                            '10100': 'rgb(124,0,157)', '10101':'rgb(155,246,96)', '10110':'rgb(23,164,108)', '10111':'rgb(244,114,140)',
                            '11000': 'rgb(117,66,54)', '11001':'rgb(194,0,210)', '11010':'rgb(54,243,71)', '11011':'rgb(177,4,102)',
                            '11100': 'rgb(117,214,181)', '11101':'rgb(149,154,136)', '11110':'rgb(150,109,0)', '11111':'rgb(218,169,66)'},
                           True)

sixBitColorSet = ColorSet("6 bit",
                          "Sixty-four colors.",
                          6,
                          {'000000': 'rgb(0,0,0)', '000001': 'rgb(0,0,85)', '000010': 'rgb(0,0,170)', '000011': 'rgb(0,0,255)',
                           '000100': 'rgb(0,85,0)', '000101': 'rgb(0,85,85)', '000110': 'rgb(0,85,170)', '000111': 'rgb(0,85,255)',
                           '001000': 'rgb(0,170,0)', '001001': 'rgb(0,170,85)', '001010': 'rgb(0,170,170)', '001011': 'rgb(0,170,255)',
                           '001100': 'rgb(0,255,0)', '001101': 'rgb(0,255,85)', '001110': 'rgb(0,255,170)', '001111': 'rgb(0,255,255)',
                           '010000': 'rgb(85,0,0)', '010001': 'rgb(85,0,85)', '010010': 'rgb(85,0,170)', '010011': 'rgb(85,0,255)',
                           '010100': 'rgb(85,85,0)', '010101': 'rgb(85,85,85)', '010110': 'rgb(85,85,170)', '010111': 'rgb(85,85,255)',
                           '011000': 'rgb(85,170,0)', '011001': 'rgb(85,170,85)', '011010': 'rgb(85,170,170)', '011011': 'rgb(85,170,255)',
                           '011100': 'rgb(85,255,0)', '011101': 'rgb(85,255,85)', '011110': 'rgb(85,255,170)', '011111': 'rgb(85,255,255)',
                           '100000': 'rgb(170,0,0)', '100001': 'rgb(170,0,85)', '100010': 'rgb(170,0,170)', '100011': 'rgb(170,0,255)',
                           '100100': 'rgb(170,85,0)', '100101': 'rgb(170,85,85)', '100110': 'rgb(170,85,170)', '100111': 'rgb(170,85,255)',
                           '101000': 'rgb(170,170,0)', '101001': 'rgb(170,170,85)', '101010': 'rgb(170,170,170)', '101011': 'rgb(170,170,255)',
                           '101100': 'rgb(170,255,0)', '101101': 'rgb(170,255,85)', '101110': 'rgb(170,255,170)', '101111': 'rgb(170,255,255)',
                           '110000': 'rgb(255,0,0)', '110001': 'rgb(255,0,85)', '110010': 'rgb(255,0,170)', '110011': 'rgb(255,0,255)',
                           '110100': 'rgb(255,85,0)', '110101': 'rgb(255,85,85)', '110110': 'rgb(255,85,170)', '110111': 'rgb(255,85,255)',
                           '111000': 'rgb(255,170,0)', '111001': 'rgb(255,170,85)', '111010': 'rgb(255,170,170)', '111011': 'rgb(255,170,255)',
                           '111100': 'rgb(255,255,0)', '111101': 'rgb(255,255,85)', '111110': 'rgb(255,255,170)', '111111': 'rgb(255,255,255)'},
                          True)

colorSetDictionary = {1:oneBitColorSet, 2:twoBitColorSet, 3:threeBitColorSet, 4:fourBitColorSet,
                      5:fiveBitColorSet, 6:sixBitColorSet}

data = str(input("Please input the text you'd like to write:\n"))

filesize = len(data)

rawData = ''.join(format(ord(i),'b').zfill(8) for i in data)

streamName = str(input("Please enter the stream name:\n"))
streamDesc = str(input("Please enter the stream description:\n"))

compressionSatisfied = False

while compressionSatisfied == False:
    isCompressionEnabled = input("Enable compression? (y/n):\n")
    if isCompressionEnabled == "y":
        compression = True
        compressionSatisfied = True
    elif isCompressionEnabled =="n":
        compression = False
        compressionSatisfied == True

cryptoSatisfied = False

while cryptoSatisfied == False:
    isCryptoEnabled = input("Enable encryption? (y/n):\n")
    if isCryptoEnabled == "y":
        encryption = True
        cryptoSatisfied = True
    elif isCryptoEnabled =="n":
        encryption = False
        cryptoSatisfied == True



chosenSet = int(input("What bitlength do you want?\n"))

activeColorSet = colorSetDictionary[chosenSet]

print("You have chosen the {} default colorset.  {}".format(activeColorSet.name, activeColorSet.description))

while len(rawData) % activeColorSet.bitLength != 0:
    rawData = "0" + rawData

squaresNeeded = len(rawData) / activeColorSet.bitLength

print("Great.  This stream will require {} pixels/squares with this color set.".format(squaresNeeded))

satisfied = False

while satisfied == False:
    pixelWidth = int(input("How many pixels wide would you like this to be?\n"))
    blockHoriz = int(input("How many blocks wide should it be?\n"))
    blockVert = int(input("How many blocks tall should it be?\n"))

    totalFrames = math.ceil(squaresNeeded / (blockHoriz * blockVert))

    print("{} x {} blocks {} pixels wide will have a resolution of {} x {}."
          "\nThis frame fits {} blocks, and since this project requires {} blocks, {} frames will be needed.".format
          (blockHoriz, blockVert, pixelWidth, blockHoriz * pixelWidth, blockVert * pixelWidth,
           blockHoriz * blockVert, squaresNeeded, totalFrames))
    confirmation = input("Type 'yes' if this is good with you.  Otherwise, press enter and you'll be able to change parameters!\n")
    if confirmation == "yes":
        satisfied = True

print("begin render! :)")

#haslib

def createHeader(name, desc, filesize, crypto, compress, ):
    pass


#eventually add file directory argument
def makeCalibrationCheckerBox(pixWidth, horizontal, vertical):
    image = Image.new('RGB', (pixWidth * horizontal, pixWidth * vertical), 'black')
    draw = ImageDraw.Draw(image)
    drawFirstVert = True
    for i in range(vertical):
        drawBox = 2
        if drawFirstVert == False:
            drawBox += 1
        for j in range (horizontal):
            if drawBox % 2 == 0:
                draw.rectangle((j * pixWidth, i * pixWidth, pixWidth * (j + 1), pixWidth * (i + 1)),
                               fill='rgb(255,0,255)')
            else:
                draw.rectangle((j * pixWidth, i * pixWidth, pixWidth * (j + 1), pixWidth * (i + 1)),
                               fill='rgb(0,0,0)')
            drawBox += 1
        drawFirstVert = not drawFirstVert

    image.save(str("Calibrator.png"), 'png')

makeCalibrationCheckerBox(pixelWidth, blockHoriz, blockVert)


#convert data to colors

colorList = []

while len(rawData) > 0:
    dataChunk = rawData[0:activeColorSet.bitLength]
    currentCreatedPixel = activeColorSet.colorDictionary[dataChunk]
    colorList.append(currentCreatedPixel)
    rawData = rawData[activeColorSet.bitLength:]

#write data to frames

for h in range(totalFrames):
    im = Image.new('RGB', (pixelWidth * blockHoriz, pixelWidth * blockVert), 'white')
    draw = ImageDraw.Draw(im)
    for i in range(blockVert):
        for j in range (blockHoriz):
            if len(colorList) == 0:
                break
            activeColor = colorList[0]
            colorList = colorList[1:]
            draw.rectangle((j * pixelWidth, i * pixelWidth, pixelWidth * (j + 1), pixelWidth * (i + 1)),
                           fill=activeColor)
    fileName = "test" + "_" + str(h + 1) + ".png"
    im.save(str(fileName), 'png')

print("Done!")