## ACTIVITY 2 Answer the following questions

1. Answer the following questions:
a. What is duck typing, as explained in the video?
    Duck typing is another way to achieve polymorphism besides inheritance. Objects can be treated as if they are a different type as long as they meet the minimum necessary attributes and methods required. So as long as an object resembles another, it could also be treated of that type.

b. What did the Car class need to have so it could work inside the same loop as Dog and
Cat, even if it does not inherit from the Animal class?
    The car class needed to have the speak() method, since the original horn() method from the car class didn't match the necessary requirement to display it in the for loop.

2. (Output is in the .py file)

3. How does the code in 2.2 demonstrate polymorphism?
    The code demonstrates polymorphism because the function start_trip() can accepts entirely different classes and call vehicle_move() without checking their type, as long as they all share the same move() method