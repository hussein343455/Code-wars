# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
# Your objective is to determine the length of the loop.
# For example in the following picture the tail's size is 3 and the loop size is 11.
# Note: do NOT mutate the nodes!

# Use the `next' attribute to get the following node
# node.next


def loop_size(node):
    no=set()
    no2=set()
    head=node
    x=node
    while node:
        if (node in no):
            x=node
            break
        no.add(node)
        node=node.next
    while head:
        if (x in no2):
            return len(no)-len(no2)+1
        no2.add(head)
        head=head.next
