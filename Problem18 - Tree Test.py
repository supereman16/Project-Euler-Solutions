class Tree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def tree(rows, root):
    root.data = rows[0][1]
    
    return root

rows = [{1: '75'}, {1: '95', 2: '64'}, {1: '17', 2: '47', 3: '82'}, {1: '18', 2: '35', 3: '87', 4: '10'}, {1: '20', 2: '04', 3: '82', 4: '47', 5: '65'}, {1: '19', 2: '01', 3: '23', 4: '75', 5: '03', 6: '34'}, {1: '88', 2: '02', 3: '77', 4: '73', 5: '07', 6: '63', 7: '67'}, {1: '99', 2: '65', 3: '04', 4: '28', 5: '06', 6: '16', 7: '70', 8: '92'}, {1: '41', 2: '41', 3: '26', 4: '56', 5: '83', 6: '40', 7: '80', 8: '70', 9: '33'}, {1: '41', 2: '48', 3: '72', 4: '33', 5: '47', 6: '32', 7: '37', 8: '16', 9: '94', 10: '29'}, {1: '53', 2: '71', 3: '44', 4: '65', 5: '25', 6: '43', 7: '91', 8: '52', 9: '97', 10: '51', 11: '14'}, {1: '70', 2: '11', 3: '33', 4: '28', 5: '77', 6: '73', 7: '17', 8: '78', 9: '39', 10: '68', 11: '17', 12: '57'}, {1: '91', 2: '71', 3: '52', 4: '38', 5: '17', 6: '14', 7: '91', 8: '43', 9: '58', 10: '50', 11: '27', 12: '29', 13: '48'}, {1: '63', 2: '66', 3: '04', 4: '68', 5: '89', 6: '53', 7: '67', 8: '30', 9: '73', 10: '16', 11: '69', 12: '87', 13: '40', 14: '31'}, {1: '04', 2: '62', 3: '98', 4: '27', 5: '23', 6: '09', 7: '70', 8: '98', 9: '73', 10: '93', 11: '38', 12: '53', 13: '60', 14: '04', 15: '23'}]
root = Tree()
tree = tree(rows, root)
print(tree.data + " - " + tree.left.data + " - " + tree.right.data)
