import cv2
import os

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0

while True:

	# Take each frame
	_, frame = cap.read()

	cv2.imshow('res', frame)
	k = cv2.waitKey(5)
	if k == 32:
		cv2.imwrite('testimage'+str(count)+'.png', frame)
		count += 1
	elif k != -1:
		break

cap.release()
cv2.destroyAllWindows()