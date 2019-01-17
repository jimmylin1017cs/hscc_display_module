# hscc_display_module

## Step

### 
- receive frame data from [darknet](https://github.com/pjreddie/darknet)
- receive bounding box data from [darknet](https://github.com/pjreddie/darknet)
- receive beacon position from our server
- run fusion algorithm to match person name
- draw bounding box on the frame with person name
- mjpeg stream (http)

## Source of Code

- function in `image.cpp` copy from [darknet](https://github.com/pjreddie/darknet)
    - image.c
    - blas.c
    - image_opencv.cpp
- structure in `image.cpp` copy from [darknet](https://github.com/pjreddie/darknet)
    - darknet.h


## Reference

### Darknet

![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

