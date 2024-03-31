class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<string> operators = {"+", "-", "*", "/"};
        stack<int> stack;
        int n;
        for (string& s: tokens){
            if (find(operators.begin(), operators.end(), s) == operators.end()){
                n = stoi(s);
                stack.push(n);
            }
            else{
                int n2 = stack.top();
                stack.pop();
                int n1 = stack.top();
                stack.pop();
                if (s == "+") n = n1+n2;
                else if (s == "-") n = n1-n2;
                else if (s == "*") n = n1*n2;
                else if (s == "/") n = n1/n2;
                stack.push(n);
            }
        }
        return stack.top();
    }
};