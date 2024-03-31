/*
Constructor rule 5, also known as the move constructor, is a special constructor that is used to transfer 
the ownership of resources from one object to another, without creating a copy. It is typically used to 
improve the performance of code that involves the transfer of large objects or data structures.
*/
#include <iostream>
#include <string>

class MyString {
public:
    // Default constructor
    MyString() : data(nullptr), size(0) {}

    // Constructor that takes a string
    MyString(const std::string& str) : data(new char[str.size()]), size(str.size()) {
        std::copy(str.begin(), str.end(), data);
    }

    // Move constructor
    MyString(MyString&& other) : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }

    // Destructor
    ~MyString() {
        delete[] data;
    }

    // Copy constructor
    MyString(const MyString& other) : data(new char[other.size]), size(other.size) {
        std::copy(other.data, other.data + size, data);
    }

    // Assignment operator
    MyString& operator=(const MyString& other) {
        if (this != &other) {
            delete[] data;
            data = new char[other.size];
            size = other.size;
            std::copy(other.data, other.data + size, data);
        }
        return *this;
    }

    // Move assignment operator
    MyString& operator=(MyString&& other) {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }

    // Function to print the string
    void print() const {
        if (data != nullptr) {
            std::cout << data << std::endl;
        } else {
            std::cout << "Empty" << std::endl;
        }
    }

private:
    char* data;
    std::size_t size;
};

int main() {
    MyString s1("Hello");
    MyString s2(std::move(s1)); // move constructor
    s2.print(); // prints "Hello"
    s1.print(); // prints "Empty"

    MyString s3("World");
    s2 = std::move(s3); // move assignment operator
    s2.print(); // prints "World"
    s3.print(); // prints "Empty"

    return 0;
}