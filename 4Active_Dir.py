
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Write a function that provides an efficient look up of whether the user is in a group. 

def is_user_in_group(user, group): 

    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    else:
        for group in group.groups:
            if is_user_in_group(user, group):
                return True
    return False                                

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
user1 = "user1"
parent2 = Group("parent2")
sub_child2 = Group("subchild2")

sub_child2.add_user(user1)

parent2.add_group(sub_child2)
parent2.add_user(sub_child2)
parent2.add_user(user1)

parent.add_group(parent2)


print(f"T1 : {user1} is in {parent2.name}: {is_user_in_group(user1, parent2)}")

print(f"T1 : {user1} is in {sub_child2.name}: {is_user_in_group(user1, sub_child2)}")

print(f"T1 : {sub_child2.name} is in {parent2.name}: {is_user_in_group(sub_child2.name, parent2)}")


print(f"T1 : {user1} is in {parent2.name}: {is_user_in_group(user1, parent2)}")

print(f"T1 : {sub_child2.name} is in {parent2.name}: {is_user_in_group(sub_child2.name, parent2)}") 


## Test Case 2

user2 = "user2"
group2 = Group("group2")

group2.add_user(user2)

parent.add_group(group2)

print(f"T2 : {user2} is in {group2.name}: {is_user_in_group(user2, group2)}")

print(f"T2 : {user2} is in {group2.name}: {is_user_in_group(user2, parent)}")

## Test Case 3
# 

user3 = "user3"
group3 = Group("group3")
subgroup3 = Group("subgroup3")

parent.add_group(group3)
group3.add_user(user3)

group3.add_group(subgroup3)
subgroup3.add_user(user3)

print(f"T3 : {user3} is in {parent.name}: {is_user_in_group(user3, parent)}") # True
print(f"T3 : {user3} is in {group3.name}: {is_user_in_group(user3, group3)}") # True
print(f"T3 : {user3} is in {subgroup3.name}: {is_user_in_group(user3, subgroup3)}") # True

##Test Case 4
#edge case - User non-existent in the group hierarchy

parent4 = Group("parent4")
child4 = Group("child4")
sub_child4 = Group("subchild4")

user4 = "subchild_user4"

sub_child4.add_user(user4)
parent4.add_group(child4)


print(f"T4 : {user4} is in {parent4.name}: {is_user_in_group(user4, parent4)}") # False

## Test Case 5

user5 = "user5"
group5 = Group("group5")

print(f"T5 : {user5} is in {group5.name}: {is_user_in_group(user5, group5)}") # False

## Test Case 6
# large range of users

def large_range():
    group6 = Group("group6")

    numbers_range = range(10000)

    for i in numbers_range:
        user6 = f"user_{i}"
        group6.add_user(user6)

    print(f"T6 : {user6} is in {group6.name}: {is_user_in_group(user6, group6)}")  # False

    # User outside the valid range
    try:
        invalid_user = f"user_{len(numbers_range) + 1}"
        group6.add_user(invalid_user)
        print(f"T6 : {invalid_user} is in {group6.name}: {is_user_in_group(invalid_user, group6)}")  # False
    except ValueError as e:
        print(f"T6 : {invalid_user} is outside the valid range: {e}")

large_range()   