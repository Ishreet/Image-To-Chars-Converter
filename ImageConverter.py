from PIL import Image
import sys

def convertToChars(image):
    chars = ""
    width, height = image.size
    scale = 1
    widen = 2

    # Convert image to rgb map
    rgbImage = image.convert("RGB")

    # Loop through values and exchange them with ascii characters
    for y in range(0, height, scale):
        for x in range(0, width, scale):
            r, g, b = rgbImage.getpixel((x,y))
            average = (r + g + b)/3

            # Conditional to determine which character to switch
            if average > 225:
                chars += " " * widen
            elif average > 200:
                chars += "." * widen
            elif average > 175:
                chars += ":" * widen
            elif average > 150:
                chars += "-" * widen
            elif average > 125:
                chars += "=" * widen
            elif average > 100:
                chars += "+" * widen
            elif average > 75:
                chars += "*" * widen
            elif average > 50:
                chars += "#" * widen
            elif average > 25:
                chars += "%" * widen
            elif average > 0:
                chars += "@" * widen
        chars += "\n"
    return chars

def main():
    # Ask user for image to convert
    f = input("Enter image: ")

    # Try to load image
    try:
        image = Image.open(f)
        image.load()
    except:
        print("File not found.")
        quit()

    # Convert image into ascii characters
    chars = convertToChars(image)

    try:
        with open((f[:f.find(".")] + ".txt"), "w") as charsFile:
            charsFile.write("%s" % chars)
    except:
        print("Problem writing to file")
        quit()

    print(chars)

if __name__ == '__main__':
    main()



