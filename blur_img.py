import cv2

def blur_img(img, ratio):
    small_img = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    save_img = cv2.resize(small_img, img.shape[:2][::-1], fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return save_img

img_path = 'C:/Users/pythonzamurai/giraffe.jpg'
img = cv2.imread(img_path, 1)
save_img = blur_img(img, 0.05)
cv2.imwrite(f'blur_giraffe.jpg', save_img)