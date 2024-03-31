/*
A unique pointer is a smart pointer in C++ that provides exclusive ownership semantics to the dynamically 
allocated objects. It manages the lifetime of the object and automatically deallocates the object when the 
unique pointer goes out of scope or is deleted.

In other words, a unique pointer ensures that there is only one owner of the dynamically allocated object, 
and no other pointers can point to the same object. This helps to prevent memory leaks and dangling pointers.
*/

template<typename T>
// When the template is instantiated with a particular type, the compiler generates code that replaces all 
// occurrences of T with the specified type.

class UniquePtr {
public:
    // Constructor takes ownership of a raw pointer
    explicit UniquePtr(T* ptr = nullptr) : m_ptr(ptr) {}
    // constructor definition for a class template UniquePtr
    // explicit: an optional keyword, specifies that the constructor is not used for implicit conversions

    // Destructor deletes the owned pointer
    ~UniquePtr() {
        delete m_ptr;
    }

    // Copy constructor and copy assignment operator are deleted to enforce unique ownership
    UniquePtr(const UniquePtr&) = delete;
    UniquePtr& operator=(const UniquePtr&) = delete;
    /* When a class has a copy constructor and/or copy assignment operator that are not explicitly defined, 
    the C++ compiler generates a default implementation for them. The default implementation performs a 
    shallow copy of the object's data members, which means that it copies the values of the object's member
    variables to the new object.
    
    However, in the case of a UniquePtr, it owns a dynamically allocated object, which means that it has 
    exclusive ownership of the underlying resource. If a copy of the UniquePtr is made, both the original 
    object and the copy would be pointing to the same dynamically allocated object, which could lead to 
    undefined behavior if both objects try to delete the same resource.
    */


    // Move constructor and move assignment operator transfer ownership
    UniquePtr(UniquePtr&& other) : m_ptr(other.m_ptr) {
        other.m_ptr = nullptr;
    }
    // To transfer ownership of the dynamically allocated object from the other object to the current object,
    // and to prevent the other object from deleting the object when it goes out of scope.
    UniquePtr& operator=(UniquePtr&& other) {
        if (this != &other) { // to avoid self-assignment
            delete m_ptr;
            m_ptr = other.m_ptr;
            other.m_ptr = nullptr;
        }
        return *this;
    }
    // To transfer ownership of the dynamically allocated object from the other object to the current object.
    /*
    The reason why we need the move constructor and move assignment operator is to improve the performance 
    and efficiency of the UniquePtr class. When an object is moved, its resources are transferred to the 
    new object, rather than being copied. This can be much faster and more efficient than copying, especially
    when working with large objects or objects that are expensive to copy.
    */

    // Pointer dereferencing operator
    T& operator*() const {
        return *m_ptr;
    }
    // To access the value pointed to by the UniquePtr object.

    // Arrow operator for member access through the owned pointer
    T* operator->() const {
        return m_ptr;
    }
    // Provide a convenient way to access the members of the object pointed to by the UniquePtr


    // Explicit conversion to bool to check if the pointer is null
    explicit operator bool() const {
        return m_ptr != nullptr;
    }
    // Allow instances of UniquePtr to be used in boolean expressions. such as:
    // UniquePtr<int> uptr(new int(42));
    // if (uptr) {}

    // Release the owned pointer and return it
    T* release() {
        T* ptr = m_ptr;
        m_ptr = nullptr;
        return ptr;
    }
    // Provide a way to transfer ownership of the managed object to another part of the program

    // Reset the owned pointer to a new raw pointer
    void reset(T* ptr = nullptr) {
        delete m_ptr;
        m_ptr = ptr;
    }

private:
    T* m_ptr;
    //  Fundamental component of the UniquePtr class
};