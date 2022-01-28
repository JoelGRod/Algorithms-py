"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The 
directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" 
and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right 
away is a needless effort. Since this is the wild west, with 
dreadfull weather and not much water, it's important to save yourself 
some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following 
(depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]

You can immediatly see that going "NORTH" and immediately "SOUTH" 
is not reasonable, better stay to the same place! So the task is 
to give to the man a simplified version of the plan. A better plan 
in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]

Other examples:

In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" 
is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate 
each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and 
"SOUTH" are not directly opposite but they become directly opposite 
after the reduction of "EAST" and "WEST" so the whole path is 
reducible to ["WEST", "WEST"].
"""

pos = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST"
}


def dirReduc(arr):
    dirs = []
    for dir in arr:
        dirs.append(dir)
        if len(dirs) > 1:
            if pos[dirs[len(dirs) - 1]] == dirs[len(dirs) - 2]:
                dirs = dirs[0:len(dirs) - 2]
    return dirs


def dirReduc_extra(arr):
    dir = " ".join(arr)
    dir2 = dir.replace(
        "NORTH SOUTH", '').replace(
        "SOUTH NORTH", '').replace(
        "EAST WEST", '').replace(
        "WEST EAST", '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


def dirReduc_extra_two(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)

    return arr
