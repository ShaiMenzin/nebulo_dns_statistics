from collections import Counter


class QueryStatistics:
  def __init__(self, name, times, num_answered):
    self.name = name
    self.times = times
    self.num_answered = num_answered


def general_statistics(queries):
  """Counts how many queries appeared and how many times

  Args:
    queries (list(Query)): The queries

  Returns:
    dict: A count for how many times each query appeared
  """

  data = {}
  for q in queries:
    if q.name in data:
      data[q.name].times += 1
      data[q.name].num_answered += 1 if q.answered else 0
    else:
      data[q.name] = QueryStatistics(q.name, 1, 1 if q.answered else 0)

  return data.values()
