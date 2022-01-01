from PIL import Image

class colors:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

scale="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.k+i*width//cx "

with Image.open("unicorn.jpg") as im:
    px = im.load()
    height = im.height
    width = im.width
    cx=50
    cy=50

    for i in range(cx):
        for j in range(cy):
            sum=0
            for k in range(width//cx):
                for l in range(height//cy):
                    p=px[ k+i*width//cx,l+j*height//cy]
                    sum+= (p[0]+p[1]+p[2])//3
            #print((p[0]+p[1]+p[2])//3,end=' ')
            #print(sum//(30*30), end=" ")
            print(scale[sum//(cx*cy)*len(scale)//255],end=' ')
        print('')




print(colors.orange,'test',colors.yellow,'et ici?')
