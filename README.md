# ENPM 661 - Project 2

## Dependencies

* python3 interpreter
* Python packages - numpy, time, matplotlib, copy, math, collections, queue

## Execution

* **Dijkstra's Solver** 
    
    - To execute the program for this problem, navigate to the submission folder and use the following commands
        ```
        cd <path_to_submission>/code/
        python3 dijkstras_Abhijay_Singh.py
        ```

    - Once you run the program, enter the start and goal states in the format shown below:
    ```
    Enter start state:  50 50
    Enter goal state:  100 100
    ```

    - Each line of input should be in the format `x y` where `x` and `y` are the x and y coordinates of the point respectively.
    
    - To increase the speed of the animation, change the value of `step_size` in the `visualizer.plot()` function in the `dijkstras_Abhijay_Singh.py` file (line **34**).

## Results
* **Dijkstra's Solver** 
    
    - The outputs is as shown below:
    ```
    Enter start state (x, y) : 0 0
    Enter end state (x, y) : 599 249

    Starting search...

    Found path in 5.237769603729248 seconds.
    Distance from state to goal :  705.1999999999978
    ```

## Help
For any assistance with executing the programs or questions related to them, please reach out to me at abhijay@umd.edu.
