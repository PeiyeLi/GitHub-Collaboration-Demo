tree_height = 5
for i in range(tree_height):
    # Print spaces to center the stars
    print(' ' * (tree_height - i - 1) + '*' * (2 * i + 1))
for j in range(2):
    print(' ' * (tree_height - 1) + '*')