#!/usr/bin/ruby -w


# https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/



def three_or_not(number)

    if number % 3 == 0
      number = (number/3);
    else
      number -=1;
      number = (number/3);
    end

    if number > 0
      print String(number) + "\n"
      three_or_not(number)
    end
end


# According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are,
# the only important thing is that the first and last letter be in the right place.
# The rest can be a total mess and you can still read it without a problem.
# This is because the human mind does not read every letter by itself, but the word as a whole.
# Such a condition is appropriately called Typoglycemia.


text = "According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are,
the only important thing is that the first and last letter be in the right place.
The rest can be a total mess and you can still read it without a problem.
This is because the human mind does not read every letter by itself, but the word as a whole.
Such a condition is appropriately called Typoglycemia."

def first_and_last(word)
  strip = word[1..word.length-2]
  return word.chars.first() + strip.split('').shuffle.join + word[-1]
end


for i in text.split(" ")
  print first_and_last(i) + " "
end









# 31337357
