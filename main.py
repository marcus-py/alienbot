# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", 'nope', 'no chance', 'never')
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? ",
        "Does every human look like you? ",
        "Who are you? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.* (\d+)',
                        'unsure_response_intent': r''
                        }

  # Define .greet() below:
  def greet(self):
    self.name = input('What is your name, human? ')
    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ")
    will_help = will_help.lower()
    if will_help in self.negative_responses:
      return 'Okay, have a nice Earth day! '
      return
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    if not reply:
      return False
    for command in self.exit_commands:
      if command in reply:
        print('Okay, have a nice Earth day! ')
        return True
    return False

  # Define .chat() next:
  def chat(self):
    reply = None
    while not self.make_exit(reply):
      reply = input(random.choice(self.random_questions)).lower()
      response = self.match_reply(reply)
      if not response:
        pass
      else:
        print(response)
      
     
  # Define .match_reply() below:
  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
        intent = key
        regex_pattern = value
        found_match = re.match(regex_pattern, reply)
        if found_match and intent == 'describe_planet_intent':
          return self.describe_planet_intent()
        elif found_match and intent == 'answer_why_intent':
          return self.answer_why_intent()
        elif found_match and intent == 'cubed_intent':
          number = found_match.groups()[0]
          return self.cubed_intent(number)
        else:
          return self.no_match_intent()
          

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = ('My planet is a utopia of diverse organisms and species. ', 'I am from Opidipus, the capital of the Wayward Galaxies. ')
    random_response = random.choice(responses)
    return random_response
  
  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = ('I come in peace. ', 'I am here to collect data on your planet and its inhabitants. ', 'I heard the coffee is good. ')
    random_response = random.choice(responses)
    return random_response
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number * number * number
    return f"{number} cubed is {cubed_number}."

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = ('Please tell me more. ', 'Tell me more! ', 'Why do you say that? ', 'I see. How about another question? ', 'Interesting. Can you tell me more? ', 'I see. ', 'Why? ')
    random_response = random.choice(responses)
    return random_response

# Create an instance of AlienBot below:
alien = AlienBot()

alien.greet()
