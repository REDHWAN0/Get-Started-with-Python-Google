### YOUR CODE HERE ###
def send_email(num_visits, visits_email):
  """Sends a marketing email if the customer has visited the theater enough times.

  Args:
    num_visits: The number of times the customer has visited the theater.
    visits_email: The minimum number of visits the customer must have made for them to receive a marketing email.

  Returns:
    A string indicating whether or not to send the email.
  """

  if num_visits >= visits_email:
    return 'Send email.'
  else:
    return 'Not enough visits.'


if __name__ == '__main__':
  print(send_email(num_visits=3, visits_email=5))
  print(send_email(num_visits=5, visits_email=5))

  print(send_email(num_visits=3, visits_email=5))  # Should print 'Not enough visits.'
  print(send_email(num_visits=5, visits_email=5))  # Should print 'Send email.'
  print(send_email(num_visits=15, visits_email=10))  # Should print 'Send email.'