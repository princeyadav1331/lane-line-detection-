Capture("test_video.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=10,maxLineGap=5)
    averaged_lines = average_slope_intercept(frame,lines)
    line_image = display_lines(frame,averaged_lines)
    combo_image = cv2.addWeighted(frame,0.8,line_image,1,1)    # Imposing the line_image on the original image

    cv2.imshow('Result',combo_image)
    cv2.waitKey(1)
