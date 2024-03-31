#include <cstddef>

template<typename T>
class SharedPtr {
public:
    // Initialize SharedPtr
    SharedPtr() : ptr(nullptr), count(nullptr) {}
    SharedPtr(T* p) : ptr(p), count(new size_t(1)) {}
    // {} indicates that no additional initialization is needed for the object.

    SharedPtr(const SharedPtr<T>& other) : ptr(other.ptr), count(other.count) {
        if (count) {
            ++(*count);
        }
    }

    ~SharedPtr() {
        release();
    }

    SharedPtr<T>& operator=(const SharedPtr<T>& other) {
        if (this != &other) {
            release();
            ptr = other.ptr;
            count = other.count;
            if (count) {
                ++(*count);
            }
        }
        return *this;
    }

    T& operator*() const {
        return *ptr;
    }

    T* operator->() const {
        return ptr;
    }

    size_t use_count() const {
        return count ? *count : 0;
    }

    bool unique() const {
        return use_count() == 1;
    }

    void reset() {
        release();
        ptr = nullptr;
        count = nullptr;
    }

    void reset(T* p) {
        release();
        ptr = p;
        count = new size_t(1);
    }

    T* get() const {
        return ptr;
    }

private:
    T* ptr;
    size_t* count;

    void release() {
        if (count) {
            --(*count);
            if (*count == 0) {
                delete ptr;
                delete count;
            }
            ptr = nullptr;
            count = nullptr;
        }
    }
};