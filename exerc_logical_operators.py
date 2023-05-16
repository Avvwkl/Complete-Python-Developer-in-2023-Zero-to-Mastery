is_magician = False
is_expert = True

# check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print('You are a master magician')

# check if magician but NOT expert: "at least you're getting here"
elif is_magician and not is_expert:
    print('At least you\'re getting here')


# if you're NOT a magician: "You need magic powers"
elif not is_magician:
    print('You need magic powers')

