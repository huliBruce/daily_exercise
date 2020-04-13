class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


t = ListNode(3)
t1 = ListNode(2)

t2 = ListNode(0)

t3 = ListNode(-4)


t.next = t1
t1.next = t2
t2.next = t3
t3.next = t2


class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		start = head
		start2 = head
		while start is not None and start2 is not None:
			start = start.next
			if start2.next is None:
				return False
			start2 = start2.next.next

			if start == start2:
				return True

		return False
			


s = Solution()
r = s.hasCycle(t)
print(r)
