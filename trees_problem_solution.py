import anytree

def form_sub_tree(priority_queue,original_length):
    first_node = priority_queue[0]
    second_node = priority_queue[1]
    new_root_value = first_node.value + second_node.value
    new_root = anytree.Node(name=str(new_root_value),children=[first_node,second_node],value=new_root_value)

    if len(priority_queue) == 2:
        return new_root
    else:
        insert_to_priority_queue(priority_queue,new_root)
        return form_sub_tree(priority_queue,original_length)

def create_dictionary(string):
    frequency_dict = {}
    for char in string:

        if char == "\n":
            char = "New Line"
        if char == " ":
            char = "SP"

        if char not in frequency_dict.keys():
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1

    return frequency_dict

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

def create_priority_queue(frequency_dict):
    priority_queue = []
    for element in frequency_dict:
        new_node = anytree.Node(name=element,value=frequency_dict.get(element))
        priority_queue.append(new_node)

    return priority_queue
        

def insert_to_priority_queue(priority_queue,new_root):
    priority_queue.pop(0)
    priority_queue.pop(0)

    for node in range(len(priority_queue)-1,-1,-1):
        #if the node is the last in the list. 
        if node == len(priority_queue)-1:
            if new_root.value >= priority_queue[node].value:
                priority_queue.append(new_root)
                break
        #If the node is the first in the list
        elif node == 0:
            if new_root.value < priority_queue[node].value:
                priority_queue.insert(0,new_root)
            else:
                priority_queue.insert(1,new_root)
        #Anywhere else in the list
        else:
            if new_root.value >= priority_queue[node].value:
                priority_queue.insert(node+1,new_root)
                break

def get_encode_dict(root,total_characters):
    encode_dict = {}
    create_encode_dict(root,total_characters,encode_dict)
    return encode_dict

def create_encode_dict(root,total_characters,encode_dict,current_code=""):
    if root.children != ():
        create_encode_dict(root.children[0],total_characters,encode_dict,current_code + "0")
        create_encode_dict(root.children[1],total_characters,encode_dict,current_code + "1")
    else:
        encode_dict[root.name] = current_code
        if len(encode_dict) == total_characters:
            return

def encode_text_from_dict(string,encode_dict):
    encoded_string = ""
    for letter in string:
        if letter == " ":
            letter = "SP"
        if letter == "\n":
            letter = "New Line"
        encoded_string += encode_dict.get(letter)

    return encoded_string

def encode_text(string):
    frequency_dict = create_dictionary(string)
    frequency_dict = sort_dictionary(frequency_dict)
    
    priority_queue = create_priority_queue(frequency_dict)

    huffman_tree = form_sub_tree(priority_queue,len(frequency_dict))
    print(anytree.RenderTree(huffman_tree, style=anytree.AsciiStyle()))

    encode_dict = get_encode_dict(huffman_tree,len(priority_queue))
    print(encode_dict)
    #Encoding the text using the encode_dict and place the encode dict at the beginning of the file for later decoding
    encoded_text = encode_text_from_dict(string,encode_dict)

    return encoded_text,huffman_tree,len(string)



def decode_text(encoded_text,huffman_tree,total_characters):
    #First form the decoding dictionary using the huffman tree
    decode_dict = get_decode_dict(huffman_tree,total_characters)
    
    #Then use the decoding dictionary to decode the text
    decoded_string = ""
    while True:
        current_test = ""
        for char in range(len(encoded_text)):
            current_test += encoded_text[char]
            if current_test in decode_dict.keys():
                decoded_string += decode_dict.get(current_test)

                encoded_text = encoded_text[char+1:]
                break
            
        if len(encoded_text) == 0:
            break
    return decoded_string

def create_decode_dict(encode_dict):
    decode_dict = {}
    for key in encode_dict:
        decode_dict[encode_dict.get(key)] = key

    return decode_dict

def get_decode_dict(root,total_characters):
    decode_dict = {}
    create_decode_dict(root,total_characters,decode_dict)
    return decode_dict

def create_decode_dict(root,total_characters,decode_dict,current_code=""):
    #If a root does have children, call this function again on each child node
    if root.children != ():
        create_decode_dict(root.children[0],total_characters,decode_dict,current_code+"0")
        create_decode_dict(root.children[1],total_characters,decode_dict,current_code+"1")
    #If not, this is a leaf node, so add it's value to the decode dictionary
    else:
        name = root.name
        if root.name == "SP":
            name = " "
        elif name == "New Line":
            name = "\n"
        decode_dict[current_code] = name
        #If you've already got all the different leters decoded, just close the function call. 
        if len(decode_dict) == total_characters:
            return 

encoded_text,huffman_tree, original_length = encode_text("Testing time. Let's see how this text looks after using huffman encoding")

assert decode_text(encoded_text,huffman_tree,original_length) == "Testing time. Let's see how this text looks after using huffman encoding"

print("Test Successful")

