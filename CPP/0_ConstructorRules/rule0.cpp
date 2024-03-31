/*
Rule 0 states that if a class doesn't define any constructors, the compiler will provide a default 
constructor.

A default constructor is a constructor that takes no arguments, and it is used to create objects of the 
class that have their data members initialized to their default values. If a class does not have a user-
defined constructor, the compiler generates a default constructor for it, which performs no initialization 
for non-static data members.
*/
#include <iostream>
class Example {
public:
    int a;
    double b;
};

class Example2 {
public:
    int a;
    double b;
    
    Example2() : a(10), b(3.14) {} // constructor to initialize member variables
};

int main(){
    Example myExample; // create an object of Example using the default constructor
    std::cout << myExample.a << std::endl; // prints initial value of int
    std::cout << myExample.b << std::endl; // prints initial value of double

    Example2 myExample2; // create an object of Example using the default constructor
    std::cout << myExample2.a << std::endl; // prints initial value of int
    std::cout << myExample2.b << std::endl; // prints initial value of double
}