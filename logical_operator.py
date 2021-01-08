# and
# or
# not

# declair variables
high_incomes = False
good_credits = True
students = False
massage1 = "Eligible"
massage2 = "Not eligible"

# and
if high_incomes and good_credits:
    print(massage1)
else:
    print(massage2)

# or
if high_incomes or good_credits:
    print(massage1)
else:
    print(massage2)

# not
if not students:
    print(massage1)
else:
    print(massage2)

# Making Condition with all Logical Operators
if (high_incomes or good_credits) and not students:
    print(massage1)
else:
    print(massage2)

# Short Circuit Evulution
if high_incomes or good_credits and not students:
    print(massage1)
else:
    print(massage2)
