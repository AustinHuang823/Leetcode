/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* left = list1;
        ListNode* right = list1;
        dummy->next = list1;
        for (int i = 0; i <= b+1; i++){
            if (i == a-1) left = list1;
            if (i == b+1) right = list1;
            list1 = list1->next;
        }
        left->next = list2;
        ListNode* head = dummy->next;
        while (head->next != nullptr) head = head->next;
        head-> next = right;
        return dummy->next;
    }
};