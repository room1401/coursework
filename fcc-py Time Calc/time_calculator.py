def add_time(start, duration, dayWeek=None):

  def convert12(hour: int, minute: int):
    hour += minute // 60
    day = hour // 24
    apm = 'PM' if hour % 24 >= 12 else 'AM'
    hour = hour % 12 if hour % 12 != 0 else 12
    return [str(hour) + f':{minute%60:02} ' + apm], day

  week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
          'Thursday', 'Friday', 'Saturday']

  startH, startM = [int(x) for x in start.split()[0].split(':')]
  if ('PM' in start and startH < 12): startH += 12
  newHour = startH + int(duration.split(':')[0])
  newMinute = startM + int(duration.split(':')[1])
  newTime, dayPassed = convert12(newHour, newMinute)

  if dayWeek:
    newDay = week[(week.index(dayWeek.capitalize()) + dayPassed) % 7]
    newTime.append(f', {newDay}')

  if dayPassed == 1:
    newTime.append(' (next day)')
  elif dayPassed > 1:
    newTime.append(f' ({dayPassed} days later)')

  return ''.join(newTime)
