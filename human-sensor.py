import cv2
import time
import argparse
import datetime
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
    help="show a camera",
    action='store_true'
)
parser.add_argument(
    "--verbose",
    required=False,
    help="enable verbose mode(show diff)",
    action='store_true'
)

parser.add_argument(
    "--sleep",
    required=False,
    default=0.2
    help="sleep time(example: 1 = 1 second)",
)

args = parser.parse_args()
#camera_id='2', diff_threshold='128'

capture = cv2.VideoCapture(int(args.camera_id))
if args.show:
    ret, frame = capture.read()
    cv2.imshow("Waiting for this window to close",frame)
    cv2.waitKey(0)


ret, frame = capture.read()

while(True):
    im_before = frame
    time.sleep(args.sleep)
    print("")
    ret, frame = capture.read()
    im_after = frame
    im_diff = im_before.astype(int) - im_after.astype(int)
    diff = im_diff.max()
    if args.verbose:
        print("diff:{}".format(diff))
    if diff >= int(args.diff_threshold):
        #Active
        print("{}: 動きを検知しました".format(datetime.datetime.now()))

capture.release()
cv2.destroyAllWindows()