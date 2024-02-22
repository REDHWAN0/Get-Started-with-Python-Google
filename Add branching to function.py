### YOUR CODE HERE ###
def send_email(num_visits, visits_email, visits_coupon):
    if num_visits >= visits_coupon:
        print('Send email with coupon.')
    elif num_visits >= visits_email:
        print('Send email only.')
    else:
        print('Not enough visits.')

print(send_email(num_visits=3, visits_email=5, visits_coupon=8))  # Should print 'Not enough visits.'
print(send_email(num_visits=5, visits_email=5, visits_coupon=8))   # Should print 'Send email only.'
print(send_email(num_visits=6, visits_email=5, visits_coupon=8))   # Should print 'Send email only.'
print(send_email(num_visits=8, visits_email=5, visits_coupon=8))   # Should print 'Send email with coupon.'
print(send_email(num_visits=10, visits_email=5, visits_coupon=8)) # Should print 'Send email with coupon.'