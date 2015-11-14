#!/usr/bin/ruby -w

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



# 31337357
puts "Mash numbers and we'll do some business";
number = gets;
number = Integer(number);
three_or_not(number)
