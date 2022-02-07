# Evenly-Divide-Challenge
Scheduler function to divide inputs evenly so that each account runs once every 15 minutes

# Summary
The main problem is we need to divide those account ids evenly into 15 groups of account ids and making sure that additional accounts over time are also included in the next run.

My initial thought was we can just divide account ids into groups by remainder of division by 15 - the interval.

This way we can easily resolve the scale issue and can perfectly divide them evenly.

The code implements that idea.

# How to run

## Dependencies
Any environment with Python 3.x installed works.

```sh
pip3 install scheduler
```

## Run

```sh
python schedule.py
```
