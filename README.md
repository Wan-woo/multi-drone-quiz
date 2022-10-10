# multi-drone-quiz
same method as "Distance Transforms of Sampled Functions"

## Setup
Package dependency: numpy 1.23.3
Run with command:
```
python main.py
```

## Structure
├── Readme.md                   // help
├── result.py                   // result
├── main.py                     
│   ├── main()
│   ├── class ESDF
│   │   ├── __init__()
│   │   ├── esdf_one_dimensional()
│   │   ├── esdf_multi_dimensional()

## Method
* Read row by row to compute esdf distance on one dimension
* Construct parabolas: for origin obstacle input (x,y), compute (x,abs(y-row)**2), f(x) = abs(y-row)**2. For every x, there could only be one exact minimal f. Discard all the points with same x but bigger f
* Use core formula to compute the lower parabola and memorize every intersection point in z, every according parabola in v
* After the z and v are done, compute for every grid the minimal distance
* Scan all the rows, and initialize f every time

