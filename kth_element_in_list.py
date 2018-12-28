class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next

        if len(res) >= k and k > 0:
            return res[-k]
        return None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p1=head
        p2=head
        i=0
        while p1!=None:
            if i>=k:
                p2=p2.next
            p1=p1.next
            i+=1
        return p2 if i>=k and k>0 else None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #反转链表
        if head is None or head.next is None:
            return head
        pre=None #指向上一个节点
        while head:
            #先用temp保存当前节点的下一个节点信息
            temp=head.next
            #保存好next之后，便可以指向上一个节点
            head.next=pre
            #让pre,head指向下一个移动的节点
            pre=head
            head=temp
        # 寻找第K个元素的位置
        for i in range(1,k):
            pre=pre.next
        temp=pre
        return temp

if __name__=='__main__':
    solution=Solution()
    k=1
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p4=ListNode(4)
    p5=ListNode(5)
    p1.next=p2
    p2.next=p3
    p3.next=p4
    p4.next=p5

    ans=solution.FindKthToTail(p1, k)
    print(ans.val)