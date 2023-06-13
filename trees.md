# Trees

![Image of a binary search tree](images/first_tree.png)

# Nature and syntax of trees
Trees are a data structure similar to linked lists in that they are made up of nodes, each with a different value, and in that each node is linked to one or more other nodes. 

A tree will always begin with a root node which forms what can be described as the top of the tree. From there, the root can have one or more children. Once a tree reaches the 'bottom', or in other words, if a node doesn't have any children, it is referred to as a 'leaf' 

Here is python syntax for the tree pictured above
``` python
import anytree

#Creating a root node
root = anytree.Node("root")

#Creating interior nodes
three = anytree.Node("3",parent=root)
ten = anytree.Node("10",parent=root)
fourteen = anytree.Node("14",parent=ten)

one = anytree.Node("1",parent=three)
six = anytree.Node("6",parent=three)

#Creating leaf nodes
four = anytree.Node("4",parent=six)
seven = anytree.Node("7",parent=six)
thirteen = anytree.Node("13",parent=fourteen)
```
# Types of trees
There are a few different types of trees. One of the more common examples is called a binary tree, where each non-leaf nodes can have up to two child nodes. Generally in a binary tree, any left child of a node will have a lesser value than it's parent node, while any right child will have a higher value than it's parent node. 

## Add examples of operations with trees
When working with sorted binary trees, most operations  have an effiency of O(log n), including searching for an item within a tree, finding the height of a tree, and even removing or inserting new nodes into the tree. Depending on the implementation of a tree's forming, the operation to find a tree's size can be O(1),or O(n) and checking if a tree is empty is also O(1)

``` python
#Continuing to use the tree created in the previous bit of code

def search_tree(root,value):
    #If the value being searched for is less than the current subtree's root
    if value < root.name:
        search_tree(root.children[0],value)
    #If the value is higher
    elif value > root.name:
        search_tree(root.children[1],value
    #If you've found the value being looked for in the current subtree's root
    else:
        return root
```

Trees have a variety of uses and practical applications. Those range from spelling correction algorithms to even compression of files using what are called huffman trees. Even storing data can be a good idea with trees. 

# Huffman Trees
One common error involving trees is made when forming huffman trees. These are trees used in compressing text files. The error can be made in not understanding and not knowing how to organize for the building of a huffman tree, but the steps are simple. First, place all established nodes in order of value, from smallest to largest. This list of nodes is often called a 'priority queue'. Next, begin by forming a subtree with the two lowest-value nodes with a parent node with the sum of those two nodes' values as its own value. Next, place that parent node back into that priority queue, maintaining the order of node values from smallest to largest. Repeat those steps until you've reached only two nodes left in the priority queue, which will form the children of the root of the huffman tree. 

 See the code below used for creating a huffman tree:

```python
import anytree

#priority queue created just as an example

priority_queue = [anytree.Node("A",value=5),anytree.Node(7),anytree.Node(8),anytree.Node(15),anytree.Node(17),anytree.Node(20),anytree.Node(41)]

def form_sub_tree(priority_queue):
    first_node = priority_queue[0]
    second_node = priority_queue[1]
    new_root_value = first_node.name + second_node.name
    new_root = anytree.Node(name=new_root_value,children=[first_node,second_node])

    if len(priority_queue) == 2:
        return new_root
    else:
        insert_to_priority_queue(priority_queue,new_root)
        return form_sub_tree(priority_queue)

def insert_to_priority_queue(priority_queue,new_root):
    priority_queue.pop(0)
    priority_queue.pop(0)

    for node in range(len(priority_queue)-1,-1,-1):
        #if the node is the last in the list. 
        if node == len(priority_queue)-1:
            if new_root.name >= priority_queue[node].name:
                priority_queue.append(new_root)
                break
        #If the node is the first in the list
        elif node == 0:
            if new_root.name < priority_queue[node].name:
                priority_queue.insert(0,new_root)
            else:
                priority_queue.insert(1,new_root)
        #Anywhere else in the list
        else:
            if new_root.name >= priority_queue[node].name:
                priority_queue.insert(node+1,new_root)
                break
```

After creating a huffman tree for a piece of text, you then need to encode each character. To do so, begin at the root, and start  moving down the tree. Each time you go left, assign a zero to the link between nodes, and each time you move to a right child node, assign a 1. See the image below to see this visualized:

![A huffman tree with encoded links between nodes](images/huffman_tree_encoding.png)

Next, encode each leaf node by retrieving each digit that is passed in order to reach a leaf node. For example, in the image above, the character U would be encoded as 1101. 

The following implmentation, as with many uses of and methods involved with trees, uses a programming concept called recursion. In this case, the code below will check, starting from the very top of the tree, if each root has one or two child nodes or not. If it does, it calls the same function for each child it has as the root of a new 'subtree'. If not, it will then add the encoded bit string for that node's character into a dictionary to be used later for encoding and break out of recursion.

See the code below for this implementation:
```python
#Declare a dictionary to store all characters and their encoded values
encode_dict = {}
def create_encode_dict(root,total_characters,encode_dict,current_code=""):
    #If the current root does have children
    if root.children != ():
        create_encode_dict(root.children[0],total_characters,encode_dict,current_code + "0")
        create_encode_dict(root.children[1],
        total_characters,encode_dict,current_code + "1")

    #If the current node doesn't have children, it must be a leaf, and thus, a character, so store the current bitstring in the encoding dictionary.
    else:
        encode_dict[root.name] = current_code
        if len(encode_dict) == total_characters:
            return

#Display encoding dictionary
for char in encode_dict:
    print(f"{char}:{encode_dict.get(char)}")
```

Finally, we need to encode our piece of text using this encoded dictionary. 
```python
def encode_text(text,encode_dict):
    encoded_text = "" #Establishing a string to store the new encoded text
    for char in text:
        #Adding each encoded character's bit string to the string storing the encoded piece of text
        encoded_text += encode_dict.get(char) 

    return encoded_text
```

To see all of this in action, along with exactly how to create a priority queue out of a piece of text:
```python

string = "My name is Jacob and I love pizza"

#This is just a quick function to sort a dictionary by it's values
def sort_dictionary(dictionary):
    sorted_values = sorted(dictionary.values())
    sorted_dict = {}
    for value in sorted_values:
        for key in dictionary.keys():
            if dictionary.get(key) == value:
                sorted_dict[key] = value
                dictionary.pop(key)
                break

    return sorted_dict

def create_priority_queue(string):
    #This portion simply counts the amount of times each character in a string appears in that string
    frequency_dictionary = {}
    for char in string:
        if char == " ":
            char = "sp"

        if char in frequency_dictionary.keys():
            frequency_dictionary[char] += 1
        else:
            frequency_dictionary[char] = 1

    #Sort the dictionary by amount of times each character appears in the text that will be encoded.
    frequency_dictionary = sort_dictionary(frequency_dictionary)

    priority_queue = []
    for element in frequency_dict:
        new_node = anytree.Node(name=element,value=frequency_dict.get(element))
        priority_queue.append(new_node)

    return priority_queue

priority_queue = create_prioority_queue(string)
amount_of_characters = len(priority_queue)
#Next, use the form subtree function to create your huffman tree. 
huffman_tree_root = form_sub_tree(priority_queue)

encode_dict = create_encode_dict(huffman_tree_root,amount_of_characters,encode_dict={})
#Lastly, form and display the encoded text
print(encode_text(string,encode_dict))
```
# Your turn!
Now that you've learned a bit more about trees, it's your turn to create a solution. 
Open the attachment below and complete the defined function for decoding a piece of encoded text given the decoded text itself and the huffman tree used to encode it. 

[Trees Problem File](trees_problem.py)

Once you're done, or if you need help, check out the solution below

[Trees Solution File](trees_problem_solution.py)

### [Back to welcome page](introduction.md)