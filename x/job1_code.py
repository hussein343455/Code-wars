import numpy as np
import cv2

#this method takes a frame a returns the cropet frame(images of the package)
def cropper(frame_x):
    cv2.rectangle(frame_x, (x_top_left, y_top_left), (x_bottom_right, y_bottom_right), (0, 255, 0), 3)
    cropped_frame = frame_x[y_top_left + 3:y_bottom_right - 3, x_top_left + 3:x_bottom_right - 3]
    return cropped_frame

#start capturing video
cap = cv2.VideoCapture("job 1/job_2_supplyline.mp4")

#capture the first frame and extract the position of the rectangle
#(in case the input images have a different shape)
ret, frame = cap.read()
H, W, D = frame.shape
x_top_left = int(W / 3.6)
y_top_left = int(H / 7.2)
x_bottom_right = int(W / 1.39)
y_bottom_right = int(H / 1.56)

#global variables
take_image=True
movement_detected=False
frame_number=0
frame_difference=np.array(3)

not_moveing avrg=
# start looping in the video frame by frame
while(True):
    #read the base frame and keep count of the total frame that have been read
    #base frame=which is the n'th frame of the video
    ret, base_frame = cap.read()
    frame_number = frame_number + 1

    #if the video ends break out of loop
    if base_frame is None:break

    #process a frame in every 20 frame
    if ret and frame_number%20==0:
        #sikep 20 frame
        #frame=which is the n'th+20 frame of the video
        for i in range(20):
            ret, frame = cap.read()
            frame_number = frame_number + 1
        # if the video ends break out of loop
        if frame is None:break
        #crop images
        frame_crop=cropper(frame)
        base_frame_crop=cropper( base_frame)

        #display cropped images
        cv2.imshow("frame",frame_crop)
        cv2.imshow("base_frame", base_frame_crop)

        #the old frame difference(to detect sudden movement)
        old_frame_difference= frame_difference

        #calculate the difference between frames to detect movement
        frame_difference = cv2.absdiff(base_frame_crop, frame_crop)
        print(np.average(frame_difference))
        if movement_detected:


        #if there was a movement and it stopped
        #(the 3 times frame difference should be smaller than old frame difference)
        if movement_detected and np.average(frame_difference)*3<np.average(old_frame_difference):
            take_image=True
            movement_detected=False
            print("take_image",np.average(frame_difference),np.average(old_frame_difference))
        # movement detected
        #(3 times the old frame difference should be bigger than frame difference)
        if np.average(frame_difference)>np.average(old_frame_difference)*3:
            movement_detected=True
            print("movement_detected",np.average(frame_difference),np.average(old_frame_difference))



    #when take_image is True a movement has occurred and stopped
    if take_image:
        name="job 1/test"+str(frame_number)+".jpg"
        cv2.imwrite(name, cropper(frame))
        take_image=False
    if cv2.waitKey(1) == ord('a'):
        break
    cv2.imshow("original", frame)
cv2.waitKey(0)
cv2.destoryAllWindows(0)

