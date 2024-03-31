class MyStack {
private:
queue<int> q1;
queue<int> q2;

public:
    MyStack() {
        
    }
    
    void push(int x) {
        if (!q2.empty()) q2.push(x);
        else q1.push(x);
    }
    
    int pop() {
        while (!q2.empty()){
            int i = q2.front();
            q2.pop();
            if (q2.empty()) return i;
            q1.push(i);
        }

        while (!q1.empty()){
            int i = q1.front();
            q1.pop();
            if (q1.empty()) return i;
            q2.push(i);
        }
        return 0;
    }
    
    int top() {
        while (!q2.empty()){
            int i = q2.front();
            q2.pop();
            q1.push(i);
            if (q2.empty()) return i;
        }

        while (!q1.empty()){
            int i = q1.front();
            q1.pop();
            q2.push(i);
            if (q1.empty()) return i;
        }
        return 0;
    }
    
    bool empty() {
        if (q1.empty() && q2.empty()) return true;
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */