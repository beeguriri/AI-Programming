from util import *
from algoritms import BruteForce, BranchAndBound, ApproxMST, LocalSearch, GA

ALGO_INFO = [
    {
        "name": "Brute Force",
        "name_coords": (0, 0),  # 이름 위치
        "displacement": (0, FONT_HEIGHT),
        "length_coords": (0, HEIGHT),
        "depends": -1,
        "sim": BruteForce.BruteForceSolver,
    },
    {
        "name": "Branch and Bound",
        "name_coords": (WIDTH, 0),  # 이름 위치
        "displacement": (WIDTH, FONT_HEIGHT),
        "length_coords": (WIDTH, HEIGHT),
        "depends": -1,
        "sim": BranchAndBound.BranchAndBoundSolver,
    },
    {
        "name": "Approximation using MST",
        "name_coords": (2 * WIDTH, 0),  # 이름 위치
        "displacement": (2 * WIDTH, FONT_HEIGHT),
        "length_coords": (2 * WIDTH, HEIGHT),
        "depends": -1,
        "sim": ApproxMST.ApproxMSTSolver,
    },
    {
        "name": "Genetic Algorithm",
        "name_coords": (3 * WIDTH, 0),  # 이름 위치
        "displacement": (3 * WIDTH, FONT_HEIGHT),
        "length_coords": (3 * WIDTH, HEIGHT),
        "depends": -1,
        "sim": GA.GASolver,
    },    
    {
        "name": "Local Search on MST Solution, degree 2",
        "name_coords": (0, HEIGHT + FONT_HEIGHT),  # 이름 위치
        "displacement": (0, HEIGHT + 2 * FONT_HEIGHT),
        "length_coords": (0, HEIGHT * 2 + FONT_HEIGHT * 2),
        "sim": LocalSearch.LocalSearchSolver,
        "depends": 3,
    },
    {
        "name": "Local Search on MST Solution, degree 3",
        "name_coords": (WIDTH, HEIGHT + FONT_HEIGHT),  # 이름 위치
        "displacement": (WIDTH, HEIGHT + 2 * FONT_HEIGHT),
        "length_coords": (WIDTH, HEIGHT * 2 + FONT_HEIGHT * 2),
        "sim": LocalSearch.LocalSearchSolver,
        "depends": 3,
    }
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (2 * WIDTH, 0, 2 * WIDTH, WINDOW_HEIGHT),
    (3 * WIDTH, 0, 3 * WIDTH, WINDOW_HEIGHT),
]
