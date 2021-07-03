import os
import csv
import argparse

import xlsxwriter

from query import Query
from statistics import general_statistics


def get_command_line_arguments():
  """Gets the arguments passed from the command line using argparse

  Returns:
      Namespace: The arguments
  """
  parser = argparse.ArgumentParser(description="Extracts information from the Nebulo app's export functionality")

  parser.add_argument('in_file', help='The queries export csv from Nebulo')
  parser.add_argument('out_file', default='./out/out.xlsx', help='The path to put the excel output file in')

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
  output_file_name = args.out_file

  if not os.path.isfile(queries_file_name):
    raise Exception(f'{queries_file_name} is not a file!')
  
  queries = None
  with open(queries_file_name, 'r') as file:
    queries = read_queries(file)

  data = general_statistics(queries)

  # export
  workbook = xlsxwriter.Workbook(output_file_name)
  worksheet = workbook.add_worksheet('Count')

  headers = ['Name', 'Times', 'Times Answered']
  worksheet.write_row(0, 0, headers)

  worksheet.write_column(1, 0, [i.name for i in data])
  worksheet.write_column(1, 1, [i.times for i in data])
  worksheet.write_column(1, 2, [i.num_answered for i in data])

  worksheet.autofilter(0, 0, len(data), len(headers) - 1)

  workbook.close()


if __name__ == "__main__":
  main()