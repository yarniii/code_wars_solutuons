#Description:

#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with
#the same value next to each other and preserving the original order of elements.
#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

#Solution:

def unique_in_order(iterable):
    if iterable:
        temp=iterable[0]
        count=0
        new_mass=[temp]
        for i in iterable:
            if i==temp:
                count=count+1
            else:
                count=0
                new_mass.append(i)
                temp=i
        return new_mass
    else:
        return list(iterable)
