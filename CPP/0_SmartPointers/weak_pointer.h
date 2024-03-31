template<typename T>
class WeakPtr {
public:
    WeakPtr() : ptr(nullptr), count(nullptr) {}

    WeakPtr(const SharedPtr<T>& sharedPtr) : ptr(sharedPtr.ptr), count(sharedPtr.count) {}

    WeakPtr(const WeakPtr<T>& other) : ptr(other.ptr), count(other.count) {}

    ~WeakPtr() {}

    WeakPtr<T>& operator=(const WeakPtr<T>& other) {
        ptr = other.ptr;
        count = other.count;
        return *this;
    }

    bool expired() const {
        return count ? *count == 0 : true;
    }

    SharedPtr<T> lock() const {
        if (expired()) {
            return SharedPtr<T>();
        }
        return SharedPtr<T>(*this);
    }

private:
    T* ptr;
    size_t* count;
};