from PIL import Image
import io
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    return saved_location
    #cropped_image.show()

def batch_crop(image, coordinates): 
    #Image.open(image).show()
    result = []
    final = []
    with Image.open(image) as img:
        width, height = img.size
    with open(coordinates) as f:
        #image = 'bathroom.jpeg'
        for i in f.readlines():
            tmp = i.split(" ")
            if float(tmp[0])*0.9 > 0 and float(tmp[1])*0.9 > 0:
                tmp[0] = float(tmp[0])*0.9
                tmp[1] = float(tmp[1])*0.9
            if float(tmp[2])*1.1 < width and float(tmp[3])*1.1 < height:
                tmp[2] = float(tmp[2])*1.1
                tmp[3] = float(tmp[3])*1.1
            try:
                result.append((float(tmp[0]), float(tmp[1]), float(tmp[2]), float(tmp[3])))
            except:pass
        for item in result:
            import uuid
            unique_filename = 'cropped_output/' + str(uuid.uuid4()) + '.jpg'
            final.append(crop(image, item, unique_filename))
    return final

#takes in image names
#ISSUE: only looks at 'file.txt' for coordinates
# but can take n number of image names
if __name__ == '__main__':
    import sys
    final = batch_crop(sys.argv[1], sys.argv[2])
    print final
    

    



