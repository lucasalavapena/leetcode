class MyHashSet {
public:
    vector<int> keys;

    MyHashSet() {
    }
    
    void add(int key) {
        if (!contains(key))
            keys.push_back(key);
    }
    
    void remove(int key) {
        for (auto k = keys.begin(); k < keys.end(); k++) {
            if (*k == key)
                keys.erase(k);
        }
    }
    
    bool contains(int key) {
        for (int k: keys) {
            if (k == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */