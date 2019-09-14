import cv2,numpy as np

class eyes:

    def __init__(self,frame,shape):
        frame_h, frame_w, frame_c = frame.shape

        #watermark = frame[229:475, 343:662]
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)

        #taking ROI from image
        watermark = frame[shape[43][1]:shape[46][1], shape[43][0]:shape[46][0]]

        #splitting the image in r,g,b,a
        r,g,b,a=cv2.split(watermark)

        # changing color to green
        r, g, b, a = cv2.split(watermark)
        comb1 = np.dstack([r, b, g, a])

        watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)

        overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')

        watermark_h, watermark_w, watermark_c = watermark.shape
        frame_h, frame_w, frame_c = frame.shape
        watermark_h,watermark_w,watermark_c=watermark.shape
        self.watermark=watermark
        self.watermark_h = watermark_h

        self.watermark_c = watermark_c
        self.watermark_w = watermark_w
        self.frame_h=frame_h
        self.frame_w=frame_w
        self.frame=frame
        self.overlay=overlay
        self.comb1=comb1

    def transform_color(self,shape):
        #   left_roi=image[shape[37][1]:shape[47][1],shape[37][0]:shape[40][0]]
        for i in range(0, self.frame_h):
            for j in range(0, self.frame_w):
                if i in range(shape[37][1], shape[47][1]) and j in range(shape[37][0], shape[40][0]):
                    pass
                else:
                    self.overlay[i, j] = self.frame[i, j]


        for i in range(0, self.watermark_h):
            for j in range(0, self.watermark_w):
                self.overlay[i + shape[37][1], j + shape[37][0]] = self.comb1[i, j]
                self.overlay[i + shape[43][1], j + shape[43][0]] = self.comb1[i, j]

        cv2.addWeighted(self.overlay, 1.25, self.frame, 1.0, 0, self.frame)
        return self.overlay

