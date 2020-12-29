import collections
INT_MAX = 2147483647
# HARDIK GANDHI
# BT17CSE030

# class defination of BST basically node
class BST: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 

#helper function to print tree in inorder travesal
'''
def inorder_traversal(root):
    if root: 
        print(root.val)
        inorder_traversal(root.left)  
        inorder_traversal(root.right)
'''

# helper functions for searching of word in BST

def search_LevelOrder(root,word): 
    ht = height(root) 
    for i in range(1, ht+1):
        if found==0: 
            search_GivenLevel(root, i, word, i) 
    if found==0:
        print(word + " is not present in the document, try different word")
    

def search_GivenLevel(root , level, word, h1): 
    global found
    if root is None: 
        return
    if level == 1 and found==0: 
        if(root.val==word):
            print("Word found at Depth " + str(h1))
            found=1
    elif level > 1 and found==0: 
        search_GivenLevel(root.left , level-1, word, h1) 
        search_GivenLevel(root.right , level-1, word, h1) 


# helper functions to print nodes in level order
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
        print("\n")
  
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.val,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 


# Computes the height of the tree  
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger tree 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1


def insert_bst(root, node): 
    if root is None: 
        root = node

    elif root.val == "-1":
        root.val = node.val

    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert_bst(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert_bst(root.left, node)

    return root


def build_bst(cost, terms, start, end, root, tree):
    '''Building the tree'''
    if start == end:
        root = insert_bst(root, BST(terms[start]))

    else:
        parent = tree[start][end]
        root = insert_bst(root, BST(terms[parent]))
        if start <= parent-1:
            build_bst(cost, terms, start, parent-1, root, tree)

        if end >= parent+1:
            build_bst(cost, terms, parent+1, end, root, tree)


# A Dynamic Programming function calculating minimum cost of BST
def optimalSearchTree(keys, freq, n): 

    cost = [[0 for x in range(n)] 
            for y in range(n)] 

    tree = [[0 for x in range(n)] 
            for y in range(n)] 

    # For a single key, cost is equal to 
    # frequency of the key 
    for i in range(0,n): 
        cost[i][i] = freq[i] 
        tree[i][i] = i

    # Now we need to consider chains of length 2, 3,...L in chain length for BST. 
    for L in range(2, n + 1): 
    
        # i is row number in cost 
        for i in range(0,n - L + 2): 
            
            # Get column number j from row number i and chain length L 
            j = i + L - 1
            if i >= n or j >= n: 
                break
            cost[i][j] = INT_MAX 
            
            # Try making all keys in interval keys[i..j] as root 
            for r in range(i, j + 1): 
                
                # c = cost when keys[r] becomes root of this subtree 
                c = 0
                if (r > i): 
                    c += cost[i][r - 1] 
                if (r < j): 
                    c += cost[r + 1][j] 
                c += sum(freq, i, j) 
                if (c < cost[i][j]): 
                    cost[i][j] = c 
                    tree[i][j] = r 

    
    root = BST("-1")
    build_bst(cost, keys, 0, n-1, root,tree)
    return (cost[0][n - 1], root)


# A utility function to get sum of array elements freq[i] to freq[j] 
def sum(freq, i, j): 
    s = 0
    for k in range(i, j + 1): 
        s += freq[k] 
    return s 
    

# Driver Main Code 
if __name__ == '__main__': 
    freq = [] 
    terms= []
    dict={}
    # open the input file and create a dictinory of word and frequency
    with open('in.txt','r') as f:
        for line in f:
            for word in line.split():
                if word in dict.keys():
                    dict[word]=dict[word]+1
                else:
                        dict[word]=1

    # Dictionary sorted word wise (lexicographically)
    collection_Sorted = collections.OrderedDict(sorted(dict.items()))
    print(collection_Sorted)
    keys_sorted = sorted(dict, key=dict.get, reverse=True)
    
    for i in collection_Sorted:
        print(i,collection_Sorted[i])
        terms.append(i)
        freq.append(collection_Sorted[i])

    n = len(keys_sorted) 
    print("\nNumber of unique terms are " + str(n) )
    (c, root) = optimalSearchTree(terms, freq, n)
    print("\nCost of Optimal BST is " + str(c)) 

    print("\nLevel Order Traversal of BST - ")
    print("******************************************************************************************************")
    printLevelOrder(root)
    print("******************************************************************************************************")
    
    global found

    while word!="exit":
        found=0
        word = input("Enter the word to search in tree. Enter 'exit' to end : ") 
        if word!="exit":
            search_LevelOrder(root, word)