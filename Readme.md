# About This
A package created for the purpose of the generation of random maps/images. Utilizes numpys for image storage and openCV for visualization. Built around a Canvas class that adds functionality for "drawing" to a numpy. 
## Included modules
Includes 4 modules: drawHelper, dataGen, pathfinding, and pynputHelper. drawHelper is the main module containing the Canvas class with contain important drawing functions, saving functions, and visualization. dataGen allows for the random generation of canvases utilizing drawHelper. pathfinding implements an a* algorithm for finding an optimal path between a source point and a destination point. pynputHelper includes a few helper functions that allow for an abstracted usage of pynput handling initialization etc. 
## Important functions to start
Initialize a Canvas object - Canvas(width, height, color_channels, pixel_to_point_ratio) Note: Currently pixel_to_point_ratio is incomplete and recommended to be set to one.  
Generate a random Canvas - randomizer(canvas: dh.Canvas,
    object_size = 1, 
    allow_intersection = False,
    choices: list = [1,2,3,4,5], 
    weights = [0.1,0.2,0.3,0.2,0.1],
    ratio_rangeA = 0.1,
    ratio_rangeB = 1.0,
    circle_size_rangeA = 1/12, 
    circle_size_rangeB = 1/6,
    margin_start_widthC = 1/9,
    margin_end_widthC = 8/9,
    margin_start_heightC = 1/9,
    margin_end_heightC = 8/9,
    margin_start_widthR = 1/9,
    margin_end_widthR = 5/9,
    margin_start_heightR = 1/9,
    margin_end_heightR = 5/9,
    add_rangeAW = 1/12, 
    add_rangeBW = 1/3, 
    add_rangeAH = 1/12, 
    add_rangeBH = 1/3)  
Utilize A* algorithm - a_star_algorithm(canvas: dh.Canvas, src, dest)
## Optimizations
I had two important optimizations in my map generation algorithm. First, I utilized a method that I first got inspired from by tetris. In tetris, many versions will use a "bag" method where pieces are randomly selected from a set and only resets after all the pieces have been used. This helps stop the same piece from being constantly repeated without stopping the "random" feel of the game. I used this idea with my random map gen, because I wanted to give users the option to stop shapes from intersecting. I have a "bag" that contains all the possible points in the canvas. Everytime a shape is generated those points are "taken" out of the bag meaning it doesn't need to do a brute force scan of the entire canvas checking to see if a point is covered twice. This increases memory by a minor amount (a few kilobytes), but improves speed by an estimated 33%(4hrs -> 3hrs). The second optimization was when checking for "walled off" sections. This is when a section is completely surrounded by shapes meaning that it is cut off from the rest of the canvas. Rather then brute forcing a complete pixel search I utilized an A* algorithm with random seeding to check, helping improve both memory and speed of the program. There's one more minor optimization which is the utilization of .savez_compressed though it is a more userside option. 
# Contact Me
Email - dmginquires@gmail.com
