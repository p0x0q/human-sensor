import cv2
import time
import argparse
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--camera-id",
    required=True,
    help="Camera ID(numeric, example: 0)",
)

parser.add_argument(
    "--diff-threshold",
    required=False,
    default=128,
    help="Threshold for the camera to detect motion",
)

parser.add_argument(
    "--show",
    required=False,
    help="show a Camera",
    action='store_true'
)

args = parser.parse_args()
#camera_id='2', diff_threshold='128'

capture = cv2.VideoCapture(int(args.camera_id))
ret, frame = capture.read()

if args.show:
    while(True):
        ret, frame = capture.read()
        cv2.imshow("Waiting for this window to close",frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

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

capture.release()
cv2.destroyAllWindows()