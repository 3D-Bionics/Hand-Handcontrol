from CallableDict import CallableDict

# Animation Generators
# ---------------
# Define custom functions for generating custom animations at run-time.
# Must return an animation array i.e. [[1,2,3,4,5],[1,2,3,4,5]] 
# See schereSteinPapier for example

from random import randint
def schereSteinPapier() -> list:
    ssp_animation=[
        [100,100,0,0,100],
        [100,100,100,100,100],
        [0,0,0,0,0]
    ]

    ssp_options=[
        [100,100,0,0,100],
        [100,100,100,100,100],
        [0,0,0,0,0]
    ]

    ssp_animation.append(ssp_options[randint(0,2)])

    return ssp_animation



# List of predefined Hand Positions
# ---------------
# Feel free to add your own!
# You can even add functions (look underneath for example) for generating animations/positions at runtime

hand_positions = CallableDict(
    {
    'Open': [[0,0,0,0,0]],
    'Fist': [[100,100,100,100,100]],
    'F You': [[100,100,0,100,100]],
    'Metal': [[0,100,100,0,100]],
    'Three Finger Salute': [[100,0,0,0,100]],
    'Rainbow': [
        [60, 50, 40, 30, 20],
        [70, 60, 50, 40, 30],
        [80, 70, 60, 50, 40],
        [90, 80, 70, 60, 50],
        [100, 90, 80, 70, 60],
        [90, 100, 90, 80, 70],
        [80, 90, 100, 90, 80],
        [70, 80, 90, 100, 90],
        [60, 70, 80, 90, 100],
        [50, 60, 70, 80, 90],
        [40, 50, 60, 70, 80],
        [30, 40, 50, 60, 70],
        [20, 30, 40, 50, 60],
        [10, 20, 30, 40, 50],
        [0, 10, 20, 30, 40],
        [10, 0, 10, 20, 30],
        [20, 10, 0, 10, 20],
        [30, 20, 10, 0, 10],
        [40, 30, 20, 10, 0],
        [50, 40, 30, 20, 10]
    ],
    'Schere Stein Papier': schereSteinPapier
}
)