/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;

        Node* dummy = new Node(0);
        dummy->next = head;

        while (head != nullptr){
            Node* new_node = new Node(head->val);
            new_node->next = head->next;
            head->next = new_node;
            head = new_node->next;
        }

        head = dummy->next;
        while (head != nullptr){
            if (head->random != nullptr){
                head->next->random = head->random->next;
            }
            head = head->next->next;
        }
        
        Node* origin_head = dummy->next;
        head = dummy->next->next;
        dummy->next = head;
        while (head != nullptr) {
            origin_head->next = head->next;
            if (head->next != nullptr){
                head->next = head->next->next;
            }
            head = head->next;
            origin_head = origin_head->next;
        }

        return dummy->next;
    }
};