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
    default=0.2,
    help="映像の差分比較を行う際の間隔(second)",
)

parser.add_argument(
    "--blind-spot",
    required=False,
    help="長方形でカメラの映像を上塗りし、物体検出の対象外部分を描画します。 (書式：rect_start_x,rect_start_y,rect_end_x,rect_end_y, example: 0,0,150,150)",
)

args = parser.parse_args()
#camera_id='2', diff_threshold='128'

def check_frame(frame):
    if args.blind_spot:
        rect_str = str(args.blind_spot).split(',')
        rects = []
        for val in rect_str:
            rects.append(int(val))
        rect = list(rects)
        if len(rect) != 4:
            print("--blind-spot は長さが4つではありません: length({})".format(len(rect)))
            return frame
        cv2.rectangle(frame, rect, (0,255,0), cv2.FILLED)
    return frame

capture = cv2.VideoCapture(int(args.camera_id))
if args.show:
    ret, frame = capture.read()
    frame = check_frame(frame)
    cv2.imshow("Waiting for this window to close",frame)
    cv2.waitKey(0)

ret, frame = capture.read()

while(True):
    im_before = frame
    time.sleep(float(args.sleep))
    print("")
    ret, frame = capture.read()
    frame = check_frame(frame)
    im_after = frame
    im_diff = im_before.astype(int) - im_after.astype(int)
    diff = im_diff.max()
    if args.verbose:
        print("diff:{}".format(diff))
    if diff >= int(args.diff_threshold):
        #Active
        print("{}: 動きを検知しました(diff:{})".format(datetime.datetime.now(),diff))

capture.release()
cv2.destroyAllWindows()