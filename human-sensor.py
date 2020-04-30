import cv2
import time
import argparse
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "--diff-threshold",
    required=False,
    default=128,
    help="Threshold for the camera to detect motion",
)
parser.add_argument(
    "--camera-id",
    required=False,
    default=0,
    help="Camera ID(numeric)",
)

args = parser.parse_args()
#camera_id='2', diff_threshold='128'

capture = cv2.VideoCapture(int(args.camera_id))
ret, frame = capture.read()
while(True):
    im_before = frame
    time.sleep(0.2)
    print("")
    ret, frame = capture.read()
    im_after = frame
    im_diff = im_before.astype(int) - im_after.astype(int)
    diff = im_diff.max()
    if diff >= int(args.diff_threshold):
        #Active
        print("動きを検知しました")
        
    """
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    """

capture.release()
cv2.destroyAllWindows()