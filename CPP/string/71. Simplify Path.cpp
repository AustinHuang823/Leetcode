class Solution {
public:
    string simplifyPath(string path) {
        queue<string> s;
        // vector<string> s;
        vector<string> res;
        string temp;
        path += '/';
        for (char& c: path){
            if (c == '/'){
                if (!temp.empty()){
                    s.push(temp);
                    // s.push_back(temp);
                    temp = "";
                }
            }
            else temp += c;
        }
        // for (auto& c: s){
        //     cout << c << endl;
        // }
        string op;
        while (!s.empty()){
            op = s.front();
            cout << op << endl;
            s.pop();
            if (op == ".") continue;
            if (op == ".."){
                if (res.empty()) continue;
                res.pop_back();
            }
            else res.push_back(op);
        }

        string paths;
        for (auto& path: res){
            paths += "/";
            paths += path;
        }
        return !paths.empty() ? paths: "/";
    }
};