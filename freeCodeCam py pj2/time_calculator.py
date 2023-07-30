def add_time(start, duration, dayWeek=None):

  def convert24(time):
    hour, minute = time.split()[0].split(':')
    hour = int(hour) + 12 if 'PM' in time else int(hour)
    return [hour, int(minute)]

  def convert12(hour, minute):
    hour += minute // 60
    dayPassed = hour // 24
    apm = 'PM' if hour % 24 > 12 else 'AM'
    hour = hour % 24 - 12 if hour % 24 > 12 else hour % 24
    hour = f'{hour:02d}' if hour == 0 else str(hour)
    minute %= 60
    minute = f'{minute:02d}' if minute < 10 else str(minute)
    return [hour + ':' + minute], dayPassed

  week = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Saturday'
  ]

  startHour, startMinute = convert24(start)
  newHour = startHour + int(duration.split(':')[0])
  newMinute = startMinute + int(duration.split(':')[1])
  newTime, nextDay = convert12(newHour, newMinute)

  if dayWeek:
    newDay = week[(week.index(dayWeek) + nextDay) % 7]
    newTime.append(', ' + newDay)

  if nextDay == 1:
    newTime.append('(next day)')
  elif nextDay > 1:
    newTime.append(f'({nextDay} days later)')

  return ' '.join(newTime)
