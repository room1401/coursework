class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __repr__(self):
    record = self.name.center(30, '*') + '\n'
    for i in self.ledger:
      record += i['description'][:23].ljust(23) + f'{i["amount"]:.2f}'.rjust(
        7) + '\n'
    record += f'Total: {self.get_balance():.02f}'
    return record

  def deposit(self, amt, desc=''):
    self.ledger.append({'amount': amt, 'description': desc})

  def get_balance(self):
    balance = 0
    if not self.ledger:
      return balance
    for i in range(len(self.ledger)):
      balance += self.ledger[i]['amount']
    return balance

  def check_funds(self, amt):
    if amt > self.get_balance():
      return False
    return True

  def withdraw(self, amt, desc=''):
    if self.check_funds(amt):
      self.ledger.append({'amount': -amt, 'description': desc})
      return True
    return False

  def transfer(self, amt, cat):
    if self.withdraw(amt, f'Transfer to {cat.name}'):
      cat.deposit(amt, f'Transfer from {self.name}')
      return True
    return False

  def get_expenseR(self):
    ratio = 1 - self.get_balance() / self.ledger[0]['amount']
    return int(ratio * 10)


def create_spend_chart(request):

  def justify(strList):
    maxLen = len(max(strList, key=len))
    return [x.ljust(maxLen) for x in strList]

  def joinFlip(header, content):
    for item in content:
      for i in range(len(item)):
        header[i] += item[i].center(3)
    return header

  margin = 4
  title = 'Percentage spent by category'
  yAxis = [(str(x * 10) + '|').rjust(margin) for x in range(0, 11)]
  xAxis = ' ' * margin + '-' * (3 * len(request) + 1)

  bars = ['o' * (x.get_expenseR() + 1) for x in request]
  bars = justify(bars)
  chart = '\n'.join(joinFlip(yAxis, bars)[::-1])

  label = [x.name for x in request]
  label = justify(label)
  padding = [' ' * margin for x in range(len(label[0]))]
  vLabel = '\n'.join(joinFlip(padding, label))

  return '\n'.join([title, chart, xAxis, vLabel])
