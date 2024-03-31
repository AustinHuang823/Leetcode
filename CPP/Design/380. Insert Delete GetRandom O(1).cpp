class RandomizedSet {
private:
    unordered_map<int, int> elements_map;
    vector<int> elements;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (elements_map.find(val) != elements_map.end()) return false;
        elements_map[val] = elements.size();
        elements.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (elements_map.find(val) == elements_map.end()) return false;
        int last_idx = elements.size()-1;
        int last_num = elements[last_idx];
        int index_to_remove = elements_map[val];
        elements_map[last_num] = index_to_remove;
        elements_map.erase(val);

        swap(elements[index_to_remove], elements[last_idx]);
        elements.pop_back();

        return true;
    }
    
    int getRandom() {
        int index = rand() % elements.size();
        return elements[index];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */