#include <iostream>
extern "C"{
    void calculateCoords(float *x,float *y,float *z){
        *x = *x*100;
        *y = *y*100;
        *z = *z*100;
        return;
    };
}