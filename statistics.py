from collections import Counter


def count_queries(queries):
  """Counts how many queries appeared and how many times

  Args:
      queries (list(Query)): The queries
  
  Returns:
      dict: A count for how many times each query appeared
  """

  names_counter = Counter([q.name for q in queries])

  return names_counter