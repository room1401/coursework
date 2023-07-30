def add_time(start, duration, dayWeek=None):

  def convert24(time):
    hour, minute = time.split()[0].split(':')
    hour = int(hour)
    if ('PM' in time and hour < 12):
      hour += 12
    return hour, int(minute)

  def convert12(hour, minute):
    hour += minute // 60
    day = hour // 24
    apm = 'PM' if hour % 24 >= 12 else 'AM'
    if hour % 24 > 12: hour %= 12
    elif hour == 0: hour = 12
    else: hour %= 24
    minute %= 60
    minute = f'{minute:02d}' if minute < 10 else str(minute)
    return [str(hour) + ':' + minute + ' ' + apm], day

  week = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Saturday'
  ]

  startHour, startMinute = convert24(start)
  newHour = startHour + int(duration.split(':')[0])
  newMinute = startMinute + int(duration.split(':')[1])
  newTime, dayPassed = convert12(newHour, newMinute)

  if dayWeek:
    newDay = week[(week.index(dayWeek.capitalize()) + dayPassed) % 7]
    newTime.append(', ' + newDay)

  if dayPassed == 1:
    newTime.append(' (next day)')
  elif dayPassed > 1:
    newTime.append(f' ({dayPassed} days later)')

  return ''.join(newTime)
