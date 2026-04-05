import PyDraw.drawHelper as dh
import PyDraw.pynputHelper as ph
import PyDraw.dataGen as dg
import PyDraw.pathfinding as pf
import cv2


canvas = dh.Canvas(128,72)
array_of_data = dg.collector(canvas, 2, object_size= 4, choices= [2,3,4,5,6])

poop = cv2.resize(array_of_data[0], None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Img", poop)
cv2.waitKey(0)
