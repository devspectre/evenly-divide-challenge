# Evenly-Divide-Challenge
Scheduler function to divide inputs evenly so that each account runs once every 15 minutes

# Summary(Narrative)

## Scheduling account every 15 minutes (`get_account_ids_to_run_every_x_minutes`)
The main problem is we need to divide those account ids evenly into 15 groups of account ids and making sure that additional accounts over time are also included in the next run.

Initial thought was we can just divide account ids into groups by remainder of division by 15 - the interval.

This way we can easily resolve the scale issue and can perfectly divide them evenly with additional accounts over time.

## Scheduling account every x hours (`get_account_ids_to_run_every_x_hours`)
The principle is as same as 'every 15 minutes' solution.

We just have more buckets which means we can run less accounts every minute.

For example, if we want to sync accounts every 3 hours, then we just need to run an account once every 3 * 60 minutes, which means we can have 180 groups.



The code implements that idea.

# How to run

## Dependencies
Any environment with Python 3.x installed.


## Run

```sh
python schedule.py
```
