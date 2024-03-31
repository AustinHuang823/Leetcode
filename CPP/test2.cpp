/*
If a class defines a destructor, copy constructor, or copy assignment operator, it should define all three. 
This is because the default implementations provided by the compiler may not be appropriate for all 
situations, particularly when the class has dynamically allocated resources that need to be managed properly.

The copy constructor is used to create a new object that is a copy of an existing object. It takes a 
reference to another object of the same type, and creates a new object with the same data members as the 
original. If a class does not define its own copy constructor, the compiler will provide a default 
implementation that performs a shallow copy of the data members. This means that if the class has pointers
or other dynamically allocated resources, the copy constructor will not create a true copy of the object, 
but rather a new object that points to the same resources as the original.
*/
#include <iostream>

class Example {
public:
    int* data;
    int size;
    
    // Default constructor
    Example() : data(nullptr), size(0) {}
    
    // Destructor
    ~Example() {
        delete[] data;
    }
    
    // Copy constructor (shallow copy)
    Example(const Example& other) {
        size = other.size;
        data = other.data;
    }
    
    // Function to allocate memory and initialize data
    void allocateData(int n) {
        size = n;
        data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = i;
        }
    }
};

class Example2 {
public:
    int* data;
    int size;
    
    // Default constructor
    Example2() : data(nullptr), size(0) {}
    
    // Copy constructor (deep copy)
    Example2(const Example2& other) : data(new int[other.size]), size(other.size) {
        for (int i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
    }
    
    // Destructor
    ~Example2() {
        delete[] data;
    }
    
    // Copy assignment operator (deep copy)
    Example2& operator=(const Example2& other) {
        if (this != &other) {
            delete[] data;
            data = new int[other.size];
            size = other.size;
            for (int i = 0; i < size; i++) {
                data[i] = other.data[i];
            }
        }
        return *this;
    }

    // Function to allocate memory and initialize data
    void allocateData(int n) {
        size = n;
        data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = i;
        }
    }
};

int main() {
    // Create an object of Example
    Example a;
    a.allocateData(5);
    
    // Create a copy of a using the copy constructor
    Example b(a);
    
    // Change a's data
    a.data[0] = 10;
    
    // Print b's data
    for (int i = 0; i < b.size; i++) {
        std::cout << b.data[i] << " "; // prints 10 1 2 3 4
    }

    // Create an object of Example2
    Example2 a2;
    a2.allocateData(5);
    
    // Create a deepcopy of a using the copy constructor
    Example2 b2(a2);
    
    // Change a's data
    a2.data[0] = 10;
    
    // Print b's data
    for (int i = 0; i < b2.size; i++) {
        std::cout << b2.data[i] << " "; // prints 0 1 2 3 4
    }

    return 0;
}