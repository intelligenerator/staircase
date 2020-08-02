from typing import List


# Replace pass with your solution
def ways_up(n: int, step_sizes: List[int] = [1, 2]) -> int:
    """Return the number of ways to get up the stairs

    Calculate the number of paths up the stairs, where:
        - `n` is the size of the staircase, i.e. the number of stairs
        - `step_sizes` is a list containing the step sizes you are allowed to
           take

    Examples
    --------
    >>> ways_up(1)
    1

    >>> ways_up(5)
    8

    >>> ways_up(5, step_sizes=[1, 3, 5])
    5
    """
    steps = 0
    for step in step_sizes:
        if step > n:
            continue
        elif step == n:
            steps += 1
        else:
            steps += ways_up(n-step, step_sizes)

    return steps
