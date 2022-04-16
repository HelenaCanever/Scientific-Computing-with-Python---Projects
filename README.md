# Scientific Computing with Python - Projects :snake:

These projects are part of the "Scientific Computing with Python" curriculum on FreeCodeCamp. Descriptions of the projects and examples are taken from 
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects

## Project 1: Arithmetic formatter ✏️

The aim is to create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

### Example:

Input:
```
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

```
Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```  

## Project 2 : Time calculator  🗓️

The goal is to write a function named ```add_time``` that takes in two required parameters and one optional parameter:
- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive

**Without the use of python libraries** , the function adds the duration time to the start time and return the result.
- If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time.
- If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

### Example:
```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## Project 3 : Budget App 💲 

The first aim is to create a ```Category``` class than instintiates objects based on different budget categories like _food_, _clothing_, and _entertainment_. The class should have an instance variable called ```ledger``` that is a list. The class should also contain the following methods:
- A ```deposit``` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
- A ```withdraw``` method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
- A ```get_balance``` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A ```transfer``` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
- A ```check_funds``` method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display, for instance:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
The second aim is to create a ```create_spend_chart``` function that takes a list of categories as an argument. It should return a string that is a bar chart of the percentange of the total spending spent by each category.

For instance:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Project 4 : Polygon Area Calculator 📐

The aim is to create a ```Rectangle``` class and a ```Square``` class. The ```Square``` class should be a subclass of Rectangle and inherit methods and attributes.

### Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:
- ```set_width```
- ```set_height```
- ```get_area```: Returns area (width * height)
- ```get_perimeter```: Returns perimeter (2 * width + 2 * height)
- ```get_diagonal```: Returns diagonal ((width ** 2 + height ** 2) ** .5)
- ```get_picture```: Returns a string that represents the shape using lines of "*".  If the width or height is larger than 50, this should return the string: "Too big for picture".
- ```get_amount_inside```: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
- Additionally, if an instance of a Rectangle is represented as a string, it should look like: ```Rectangle(width=5, height=10)```

### Square class
The ```Square``` class should be a subclass of ```Rectangle```. When a ```Square``` object is created, a single side length is passed in. The ```__init__``` method should store the side length in both the width and height attributes from the ```Rectangle``` class.
The ```Square``` class should be able to access the ```Rectangle``` class methods but should also contain a set_side method. If an instance of a ```Square``` is represented as a string, it should look like: ```Square(side=9)```
Additionally, the set_width and set_height methods on the Square class should set both the width and height.

### Examples:
Input:
```
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
Output:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## Project 5 : Probability Calculator :game_die:

The goal is to write a program to perform a large number of experiments to estimate an approximate probability.Specifically, the program determines the approximate probability of drawing certain balls randomly from a hat.

First, a ```Hat``` class is created that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 
A hat will always be created with at least one ball. Contents are turned into a list of strings containing one item for each ball in the hat. For example, if the hat is ```{"red": 2, "blue": 1}```, contents are be ```["red", "red", "blue"]```.

The ```Hat``` class has a ```draw``` method that accepts an argument indicating the number of balls to draw from the hat. This method removes balls at random from contents and returns those balls as a list of strings. The balls does not go back into the hat during the draw. If the number of balls to draw exceeds the available quantity, the method returns all the balls.

Second, I create an ```experiment``` function that accepts the following arguments:
- ```hat```: A ```hat``` object.
- ```expected_balls```: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
- ```num_balls_drawn```: The number of balls to draw out of the hat in each experiment.
- ```num_experiments```: The number of experiments to perform.
The experiment function returns a probability.

### Example:
```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

