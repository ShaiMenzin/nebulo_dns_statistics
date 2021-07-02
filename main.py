import os
import csv
import argparse

from query import Query
from statistics import count_queries


def get_command_line_arguments():
  """Gets the arguments passed from the command line using argparse

  Returns:
      Namespace: The arguments
  """
  parser = argparse.ArgumentParser(description="Extracts information from the Nebulo app's export functionality")

  parser.add_argument('in_file', help='The queries export csv from Nebulo')

  return parser.parse_args()


def read_queries(file):
  """Reads the queries from the given csv file and returns them in a list

  Args:
      file: The csv file exported from Nebulo to read from

  Returns:
      list: The queries
  """
  queries = []

  reader = csv.reader(file)
  # skip the first row
  next(reader)
  for row in reader:
    queries.append(Query(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
  
  return queries


def main():
  args = get_command_line_arguments()

  queries_file_name = args.in_file
  if not os.path.isfile(queries_file_name):
    raise Exception(f'{queries_file_name} is not a file!')
  
  queries = None
  with open(queries_file_name, 'r') as file:
    queries = read_queries(file)

  queries_count = count_queries(queries)

  print(queries_count)


if __name__ == "__main__":
  main()