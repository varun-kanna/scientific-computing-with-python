def add_time(start, duration, day=""):
  if day:
    day = day.lower().title()
  split = start.split(" ")
  time = split[0]
  time_of_day = split[1]
  
  splitted_times = time.split(":")
  first_time = int(splitted_times[0]) # 11
  second_time = int(splitted_times[1]) # 30

  duration_split = duration.split(":")
  first_duration_time = int(duration_split[0])
  second_duration_time = int(duration_split[1])
   
  days = 0 

  # If the first hours are between 12 and 24 hours
  if ((first_time + first_duration_time >= 12) and (first_time + first_duration_time <= 24)) :
    first_time += first_duration_time
    total = (first_time)
    first_time = int(first_time % 12) 

    if time_of_day == "AM":
      time_of_day = "PM"
    else:
      days += 1
      time_of_day = "AM"
  elif(first_time + first_duration_time < 12) :
    first_time += first_duration_time
  
  # For managing the minutes 
  if second_time + second_duration_time > 60:
    second_time += second_duration_time
    total = (second_time)
    second_time = int(total % 60) 
    first_time += 1
    if first_time + first_duration_time >= 12 and total > 60:
      if time_of_day == "AM":
        time_of_day = "PM"
      else:
        days += 1
        time_of_day = "AM"
  else:
    second_time += second_duration_time
    
  if first_time + first_duration_time > 24:
    while first_duration_time >= 24:
      days += 1
      first_duration_time -= 24
    while first_time >= 24:
      days += 1
      first_time -= 24
    
    if (first_time + first_duration_time > 12) and (first_time + first_duration_time < 24) :
      first_time += first_duration_time
      total = (first_time)
      first_time = int(first_time % 12) 
  
      if time_of_day == "AM":
        time_of_day = "PM"
      else:
        days += 1
        time_of_day = "AM"
    else:
      first_time += first_duration_time

  if days > 1 and day:
    return f"{first_time}:{second_time:02d} {time_of_day}, {inc_days(day,days)} ({days} days later)"
  if days > 1 and not day:
    return f"{first_time}:{second_time:02d} {time_of_day} ({days} days later)" 
  if days == 1 and not day:
    return f"{first_time}:{second_time:02d} {time_of_day} (next day)"  
  if days == 1 and day:
    return f"{first_time}:{second_time:02d} {time_of_day}, {inc_days(day,days)} (next day)"  
  if not day:
    return f"{first_time}:{second_time:02d} {time_of_day}"  
  if day:
    return f"{first_time}:{second_time:02d} {time_of_day}, {day.title()}" 

def inc_days(current_day, num_days):
  days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  current_index = days_list.index(current_day)
  new_index = (current_index + num_days ) % 7
  return days_list[new_index]