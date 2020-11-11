# import required libraries 
import cv2
import sys
import os

TGREEN =  '\033[32m' # Green Text
ENDC = '\033[m' # reset to the defaults

print(TGREEN +  """\


_________ _______  _______  _______  _______    _______  _______  _______ _________ _______  _______  _______ 
\__   __/(       )(  ___  )(  ____ \(  ____ \  (  ____ )(  ____ \(  ____ \\__   __// ___   )(  ____ \(  ____ )
   ) (   | () () || (   ) || (    \/| (    \/  | (    )|| (    \/| (    \/   ) (   \/   )  || (    \/| (    )|
   | |   | || || || (___) || |      | (__      | (____)|| (__    | (_____    | |       /   )| (__    | (____)|
   | |   | |(_)| ||  ___  || | ____ |  __)     |     __)|  __)   (_____  )   | |      /   / |  __)   |     __)
   | |   | |   | || (   ) || | \_  )| (        | (\ (   | (            ) |   | |     /   /  | (      | (\ (   
___) (___| )   ( || )   ( || (___) || (____/\  | ) \ \__| (____/\/\____) |___) (___ /   (_/\| (____/\| ) \ \__
\_______/|/     \||/     \|(_______)(_______/  |/   \__/(_______/\_______)\_______/(_______/(_______/|/   \__/
                                                                                                              
  """ , ENDC)

def scaleImages(filepath):
    
    # Get the path of the file 
    # filepath = os.path.join(path, file)
    
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    
    if img is not None:

        #print ("\nSize before if" + str(os.path.getsize(filepath)))
        if (os.path.getsize(filepath) > 1000000) :

            print ("\nSize > 1M = " + filepath + "\n" + str(os.path.getsize(filepath)))
            scale_percent = 50 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(filepath, img)
            print ("After Resize = " + filepath + "\n" + str(os.path.getsize(filepath)))
    
    return
  
  
# Define a main function 
def main(): 
  
    # if location wasn't passed as parameter 
    # uses current location
    if (len(sys.argv)>1): 
        cwd = str(sys.argv[1])
            
    else:
        cwd = os.getcwd()

    formats = ('.jpg', '.jpeg') 

    # looping through all the files 
    # in a current directory 
    # and subdirectories
    for subdir, dirs, files in os.walk(cwd):
        for file in files:
            filepath = subdir + os.sep + file

            if os.path.splitext(file)[1].lower() in formats:
                scaleImages(filepath)


# Driver code 
if __name__ == "__main__": 
    main() 