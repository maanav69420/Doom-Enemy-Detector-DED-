import os
import cv2 as cv

def extract_frame(vid , img_name ,start_frame , end_frame , dest_folder):
    cam = cv.VideoCapture(vid)
    cam.set(cv.CAP_PROP_POS_FRAMES , start_frame)

    current_frame = start_frame
    while True:
        ref, frame = cam.read()

        current_img_name = f"{img_name } frame{current_frame}.png"
        print("Creating ..." + current_img_name)
        frame_filename = os.path.join(dest_folder, current_img_name)
        cv.imwrite(frame_filename , frame)

        if current_frame == end_frame:
            break
        current_frame += 1


    cam.release()
    cv.destroyAllWindows()

def frame_count(vid):
    cam = cv.VideoCapture(vid)
    length = int(cam.get(cv.CAP_PROP_FRAME_COUNT))
    print("Number of frames in '" + str(vid) + "' = " + str (length))


#|==================[video + image name]==================|
video = 'doom videos/doom e1m5 hurt me plenty.mp4'
img_name = f"e1m5 "
#|==================[duration]==================|
start_frame = 500
end_frame = 1500
#|==================[destination]==================|
dest_folder = 'Doom-Enemy-Detector-DED-/Doom 1 episode 1/mission5'

#|==================[function call]==================|
extract_frame(video , img_name ,start_frame , end_frame , dest_folder)
# frame_count(video)
