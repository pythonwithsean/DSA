from pathlib import Path
import logging
import time

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")
# INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

# Part 1
# Objective: count number of times we hit a 0 on both turn or end of a turn
def part1():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        dial = 50
        sol = 0
        for rot in data:
            direction, amount = rot[0], int(rot[1:])
            if direction == "L":
              dial = (dial - amount) % 100
            else:
              dial = (dial + amount) % 100
            if dial == 0:
                sol += 1
        print("Part1",sol)

# Part 2
# Objective: count number of times we hit a 0 on both turn or end of a turn
def part2():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        dial = 50
        sol = 0
        for rot in data:
            direction, amount = rot[0], int(rot[1:])
            if direction == "L":
                # It is not the same as R so we can not do sol = (dial + amount // 100)
                if amount >= dial:
                  if dial == 0 and (dial + amount) // 100 > 0:
                    val = (dial + amount) // 100
                    sol += val
                  elif dial != 0:
                   val = max((dial + amount) // 100, 1)
                   print(dial, amount, val)
                   sol += val

                new = dial - amount
                if new < 0:
                    dial = (max(abs(new // 100),1) * 100) + new
                else:
                    dial = new
            else:
               new = dial + amount
               # we count amount of 0s we turn around on
               sol += new // 100
               if new > 99:
                   dial = new % 100
               else:
                   dial = new
        print("Part2",sol)

if __name__ == "__main__":
    t1 = time.perf_counter()
    part1()
    # part2()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)
