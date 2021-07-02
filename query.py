import datetime

class Query:
  
  def __init__(self, name, short_name, type_name, type_id, asked_server, answered_from_server, question_time, response_time, responses, answered=True):
    self.name = name
    self.short_name = short_name
    self.type_name = type_name
    self.type_id = type_id
    self.asked_server = asked_server
    self.answered_from_server = answered_from_server
    self.question_time = datetime.datetime.fromtimestamp(int(question_time, 10) / 1e3)
    if response_time != '0':
      self.response_time = datetime.datetime.fromtimestamp(int(response_time, 10) / 1e3)
      self.answered = True
    else:
      self.response_time = 0
      self.answered = False
    self.responses = responses
  
  def __repr__(self):
    return f"Query('{self.name}', '{self.short_name}', '{self.type_name}', '{self.type_id}', '{self.asked_server}', '{self.answered_from_server}', '{self.question_time}', {self.response_time}, {self.responses}, {self.answered})"