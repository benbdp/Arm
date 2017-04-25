import numpy as np
import glob,os,cv2

def format_pos(org_path,new_path):
    try:
        num = 1
        images = glob.glob(os.path.join(org_path, '*.jpg'))
        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, dst = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
            dilation = cv2.dilate(dst, np.ones((5, 5), np.uint8), 1)
            im, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            newcontours = []
            for i in contours:
                area = cv2.contourArea(i)
                if area > 100:  # run test to ensure small contours are eliminated
                    newcontours.append(i)
            x, y, w, h = cv2.boundingRect(newcontours[0])
            crop_img = img[y: y + h, x: x + w]
            h, w = crop_img.shape[:2]
            ratio = h / w
            newh = int(50 * ratio)
            resized_image = cv2.resize(crop_img, (50, newh))
            cv2.imwrite(new_path + "apple" + str(num) + ".jpg", resized_image)
            num += 1
    except Exception as e:  # Raise exception if error
        print(str(e))

if __name__ == "__main__":
    org_path = "/Users/Benjamin/PycharmProjects/Arm/apples/"  # where to find images to format
    new_path = "/Users/Benjamin/PycharmProjects/Arm/resized_apples/"  # where to save resized images
    format_pos(org_path,new_path) # call function