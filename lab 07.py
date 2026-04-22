# Crystel Hilton
# Lab 07

# Creating Sets
#1Create an empty list and confirm its type and the number of items in it
def print_spaced(s):
    for ch in s:
        print(ch, end=" ")
print_spaced("Python")
print("\n")

#2 Make a set from the string 'Mississippi'. How many unique character are there? 
def print_indexed(s):
    for i in range(len(s)):
        print(i, s[i])
print_indexed("Hello")
print()

#Set Comprehension
#3Create a set of all the even number between 0 and 20 using set comprehension. 
def sum_digits(s):
    total = 0
    for ch in s:
        total += int(ch)
    return total

num = "456701"
print("Sum:", sum_digits(num))
print()

#4 -Use comprehension to build a set of the first letters of the words: ['apple', 'banana', 'avacado', 
#'cherry']
def count_upper(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    return count

print(count_upper("Mary Had A Little Lamb."))
print()

# LISTS 

#5 Build a set of vowels from the word 'encyclopedia'
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total

print(sum_list([3, 10, -4, 7, 8]))
print()

# ---------- 6 ----------
def count_positive(lst):
    count = 0
    for x in lst:
        if x > 0:
            count += 1
    return count

print(count_positive([5, 12, 0, 7, -5, 9, -1, 3]))
print()

# ---------- 7 ----------
def smallest(lst):
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

print(smallest([5, 2, 11, 6, 20, 7, 14]))
print()

# ---------- 8 ----------
def print_with_index(lst):
    for i in range(len(lst)):
        print(i, ":", lst[i])

print_with_index([80, 92, 77])
print()

# ---------- 9 ----------
def square_list(lst):
    result = []
    for x in lst:
        result.append(x*x)
    return result

print(square_list([1, 2, 3, 4]))
print()

# ---------- 10 ----------
def print_items(lst):
    for x in lst:
        print(x, end=" ")
    print()

print_items(['Python', 'is', 'fun', 100, '!.'])
print()

# ---------- 11 ----------
def print_squares(lst):
    for x in lst:
        print(x*x, end=" ")
    print()

print_squares([5, 2, 11, 6, 20, 7, 14])
print()

# ---------- 12 ----------
def even_list(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

print(even_list([5, 2, 11, 6, 20, 7, 14]))
print()

# ---------- 13 ----------
def find_word(lst, word):
    for w in lst:
        if w == word:
            return True
    return False

lst = ['Mary', 'had', 'a', 'little', 'lamb']
print(find_word(lst, "had"))
print(find_word(lst, "dog"))
print()

# ---------- 14 ----------
def sum_lists(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

print(sum_lists([1,2,3], [10,20,30]))
print()

# ---------- TUPLES ----------

# ---------- 15 ----------
def print_tuple(t):
    for x in t:
        print(x)

print_tuple(('red','green','blue','yellow'))
print()

# ---------- 16 ----------
def sum_tuple(t):
    total = 0
    for x in t:
        total += x
    return total

print(sum_tuple((3,5,7,9,12,10)))
print()

# ---------- 17 ----------
def tuple_index(t):
    for i in range(len(t)):
        print(i, t[i])

tuple_index((10,20,30))
print()

# ---------- 18 ----------
def unpack_pairs(t):
    for (x, y) in t:
        print("x =", x, "y =", y)

unpack_pairs(((1,2),(3,4),(5,6)))
print()

# ---------- 19 ----------
def count_greater(t, num):
    count = 0
    for x in t:
        if x > num:
            count += 1
    return count

print(count_greater((5,12,7,18,2,30), 10))
print()

# ---------- SET ----------

# ---------- 20 ----------
def print_set(s):
    for x in s:
        print(x, end=" ")
    print()

print_set({'Mary','had','a','little','lamb'})
print()

# ---------- 21 ----------
def print_set_index(s):
    for i, x in enumerate(s):
        print(i, x)

print_set_index({'Mary','had','a','little','lamb'})
print()

# ---------- DICTIONARY ----------

# ---------- 22 ----------
def print_keys(d):
    for k in d:
        print(k, end=" ")
    print()

print_keys({'name':'Alice','age':30,'city':'NY'})
print()

# ---------- 23 ----------
def print_keys_lines(d):
    for k in d:
        print(k)

print_keys_lines({'name':'Alice','age':30,'city':'NY'})
print()

# ---------- 24 ----------
def print_values(d):
    for v in d.values():
        print(v)

print_values({'name':'Alice','age':25,'city':'Toronto'})
print()

# ---------- 25 ----------
def print_pairs(d):
    for k, v in d.items():
        print(k, ":", v)

print_pairs({'name':'Alice','age':25,'city':'Toronto'})
print()

# ---------- 26 ----------
def sorted_dict(d):
    for k in sorted(d):
        print(k, "->", d[k])

sorted_dict({'name':'Alice','age':25,'city':'Toronto'})
print()

# ---------- 27 ----------
def passing_students(d):
    count = 0
    for v in d.values():
        if v > 50:
            count += 1
    return count

print(passing_students({'Amy':85,'James':42,'Hina':77,'Leo':55}))
print()

# ---------- 28 ----------
def dict_keys_list(d):
    result = []
    for k in d:
        result.append(k)
    return result

print(dict_keys_list({'name':'Alice','age':30,'city':'NY'}))
print()

# ---------- 29 ----------
def sum_values(d):
    total = 0
    for v in d.values():
        total += v
    return total

print(sum_values({'apple':10,'banana':6,'mango':3}))
print()

# ---------- 30 ----------
def key_value_strings(d):
    result = []
    for k, v in d.items():
        result.append(f"{k}: {v}")
    return result

print(key_value_strings({'name':'Alice','age':25}))
print()

# ---------- 31 ----------
def max_key(d):
    max_k = list(d.keys())[0]
    for k in d:
        if d[k] > d[max_k]:
            max_k = k
    return max_k

print(max_key({'Jan':1200,'Feb':900,'Mar':1500}))
print()

# ---------- 32 ----------
def group_by_length(lst):
    result = {}
    for word in lst:
        l = len(word)
        if l not in result:
            result[l] = []
        result[l].append(word)
    return result

print(group_by_length(['hi','cat','dog','apple','sun']))
print()

# ---------- 33 ----------
def char_count(s):
    result = {}
    for ch in s:
        if ch != " ":
            result[ch] = result.get(ch, 0) + 1
    return result

print(char_count("Narendra is evil!"))
print()

# ---------- 34 ----------
def longest_word(s):
    words = s.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print(longest_word("Narendra is the most evil instructor at Centennial"))