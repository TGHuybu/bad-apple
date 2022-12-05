# bad-apple
 Play 'Bad Apple' on terminal, a simple solution.
 
## Idea:
 The idea revolves around the task of converting an image to ASCII characters. So for a video, we just have to go through the video frame by frame, converting each picture to ASCII then print it on the screen.
 
 The detail is as follows:
 - Extract a frame from the video
 - Convert frame to a grey scale image
 - Convert image to ASCII by using average brightness mapping of each cropped zone corresponding to the desired output resolution (https://www.geeksforgeeks.org/converting-image-ascii-image-python/)
 - Output the frame (or save it for later use without having to load the video again)
 - Repeat until the video ends (no more frame to convert)
