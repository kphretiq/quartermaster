# quartermaster

Calculate fiscal quarter and day for gregorian calendar.
    If you want fiscal weeks, I feel your pain.
## Installation:

```python
pip install quartermaster
```

## Usage:
```python
# assuming today's date is 2017-9-2
>>> from quartermaster import Quartermaster
>>> qm = Quartermaster()
>>> qm.quarter
3
>>> qm.day
245
>>>

# a "now" in the past or future may be provided in iso date format ...
>>> qm = Quartermaster(now="1966-06-18")
>>> qm.quarter
2
>>> qm.day
169
>>> 

# ... or as a datetime object
>>> now = datetime.date(1968, 10, 18)
>>> qm = Quartermaster(now=now)
>>> qm.quarter
3
>>> qm.day
245
>>> 

# With a fiscal year that runs October 1 - September 1
>>> now = datetime.date(2017, 1, 1)
>>> qm = Quartermaster(fismonth=10, fisday=1, now=now)
>>> qm.quarter
2
>>> qm.day
93
>>>

```
