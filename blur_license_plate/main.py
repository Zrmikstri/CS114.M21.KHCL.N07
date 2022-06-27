import cv2
import pandas as pd
import argparse


def detect(input_vid_path):
    cap = cv2.VideoCapture(input_vid_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fps = round(fps)
    print(f'FPS: {fps}\t {int(width)}x{int(height)}')
    count = 0

    df = pd.read_csv('/content/output.csv')
    df = df.dropna()

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter('/content/output.avi', fourcc, 29.0, (int(width), int(height)), True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        count += 1
        for i in range(len(df[df.Frame == count])):
            x = int(df[df.Frame == count]['X'].iloc[i])
            y = int(df[df.Frame == count]['Y'].iloc[i])
            w = int(df[df.Frame == count]['Width'].iloc[i])
            h = int(df[df.Frame == count]['Height'].iloc[i])
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # blur_img = cv2.blur(frame[y: y + h, x: x + w], (int(w)//4, int(h)//4), 0)
            frame[y: y + h, x: x + w] = (0, 255, 0)
        # cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    print('Done')
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_vid_path', type=str, required=True,
                        help='input video path')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    detect(args.input_vid_path)
