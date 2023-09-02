from pickle import TRUE


text = input ("enter the taxt ---> ")

if ("make of lot of money "in text):
    spam = TRUE
elif("buy now "in text):
    spam = TRUE
elif("click  this  "in text):
    spam = TRUE
elif("sub now "in text):
    spam = TRUE
else :
    spam = False


if (spam):
    print("the is text is spam")
else :
    print("the is text is not spam")