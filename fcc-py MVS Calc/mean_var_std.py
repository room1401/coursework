import numpy as np


def calculate(lst):

  if len(lst) != 9:
    raise ValueError("List must contain nine numbers.")

  lst = np.array(lst).reshape(3, 3)
  calculations = {}

  calculations['mean'] = [
    list(lst.mean(axis=0)),
    list(lst.mean(axis=1)),
    lst.mean()
  ]
  calculations['variance'] = [
    list(lst.var(axis=0)),
    list(lst.var(axis=1)),
    lst.var()
  ]
  calculations['standard deviation'] = [
    list(lst.std(axis=0)),
    list(lst.std(axis=1)),
    lst.std()
  ]
  calculations['max'] = [
    list(np.nanmax(lst, axis=0)),
    list(np.nanmax(lst, axis=1)),
    np.nanmax(lst)
  ]
  calculations['min'] = [
    list(np.nanmin(lst, axis=0)),
    list(np.nanmin(lst, axis=1)),
    np.nanmin(lst)
  ]
  calculations['sum'] = [
    list(lst.sum(axis=0)),
    list(lst.sum(axis=1)),
    lst.sum()
  ]

  return calculations
