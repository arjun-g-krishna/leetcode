struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
	
    int i,j;
    struct ListNode* ptr = head;
    for(i=0; ptr != NULL; ptr = ptr->next, i++);
    if(i == n)
        return head->next; 
    ptr = head;
    for(j = 0; j < i-n; j++){
        if(j == i-n-1){
            ptr->next = ptr->next->next;
        }
        ptr = ptr->next;
    }
    
    return head;
}