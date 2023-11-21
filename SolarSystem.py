import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, 
           "Sun",
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (255, 255, 255))

cv2.putText(img, 
           "Mercury",
            (50,400),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (170, 180, 200))

cv2.putText(img, 
           "Venus",
            (80,500),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (255, 255, 255))

cv2.putText(img, 
           "Earth",
            (110,600),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (255, 90, 240))

cv2.putText(img, 
           "Mars",
            (140,700),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (200, 255, 80))

cv2.putText(img, 
           "Jupiter",
            (170,800),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (100, 255, 100))

cv2.putText(img, 
           "Saturn",
            (2000,900),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (250, 300, 250))

cv2.putText(img, 
           "Uranus",(230,1000),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (235, 180, 250))

cv2.putText(img, 
           "Neptune",
            (260,1100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale = 0.5,
            color = (255, 95, 125))

cv2.imshow("Solar System",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)