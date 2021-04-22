def add_time(start, duration, day_of_week=None):

  srt = start.split()
  srthm = srt[0].split(":")
  srth = int(srthm[0])
  srtm = int(srthm[1])
  part = srt[1]

  drt = duration.split(":")
  drth = int(drt[0])
  drtm = int(drt[1])

  raw_ntm = srtm + drtm
  ntm = raw_ntm % 60
  extra_nth = (raw_ntm - ntm) // 60

  raw_nth = srth + drth + extra_nth
  nth = raw_nth % 12
  extra_parts = (raw_nth-nth) // 12
  part_change = extra_parts % 2
  extra_days = ((raw_nth-nth) // 24)
  days_passed = ""

  if part_change == 0:
    time_of_day = part
    if extra_days == 0:
      days_passed = ""
    elif extra_days == 1:
      days_passed = " (next day)"
    elif extra_days > 1:
      days_passed = "(" + str(extra_days) +" days later)"
  else:
    if part == "AM":
      time_of_day = "PM"
      if extra_days == 0:
        days_passed = ""
      elif extra_days == 1:
        days_passed = " (next day)"
      elif extra_days > 1:
        days_passed = "(" + str(extra_days) +" days later)"
    if part == "PM":
      time_of_day = "AM"
      if extra_days == 0:
        days_passed = " (next day)"
      elif extra_days == 1:
        days_passed = " (2 days later)"
      elif extra_days > 1:
        days_passed = " (" + str(extra_days + 1) +" days later)"

  days = ""
  week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  if day_of_week != None:
    j = week.index(day_of_week.lower())
    if time_of_day == "AM" and nth == 0:
      j_elapsed = j + extra_days + 1
      new_j = j_elapsed % 7
      days = ", " + week[new_j].capitalize()
    elif part == "AM" and extra_parts < 12:
      j_elapsed = j + extra_days
      new_j = j_elapsed % 7
      days = ", " + week[new_j].capitalize()
    elif part == "PM" and extra_parts >= 12:
      j_elapsed = j + extra_days + 1
      new_j = j_elapsed % 7
      days = ", " + week[new_j].capitalize()
    elif part == "PM" and extra_parts < 12:
      j_elapsed = j + extra_days
      new_j = j_elapsed % 7
      days = ", " + week[new_j].capitalize()
  else:
    days = ""

  hour = str(nth)
  minutes = str(ntm)
  if time_of_day == "PM" and hour == "0":
    hour = "12"
  if time_of_day == "AM" and hour == "0":
    hour = "12"

  new_time = hour + ":" + minutes.zfill(2) +" " + time_of_day + days + days_passed

  return new_time
