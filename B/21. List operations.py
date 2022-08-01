# List items are indexed and you can access them by referring to the index number:

sequence_list = ["DNA", "RNA", "Protein"]
print(sequence_list[0])
#output: DNA

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
sequence_list = ["DNA", "RNA", "Protein"]
print(sequence_list[-2])
# output: RNA

# NOTE that negative indexing starts at -1, while normal, positive indexing starts at 0.
# Similar to strings, you can use a range for indexing:
sequence_list = ["DNA", "RNA", "Protein", "3'UTR", "5'UTR", "ORF", "lnRNA"]
print(sequence_list[2:5])
print(sequence_list[:2])
print(sequence_list[3:])
print(sequence_list[-2:-4])
# outputs:
# ['Protein', "3'UTR", "5'UTR"]
# ['DNA', 'RNA']
# ["3'UTR", "5'UTR", 'ORF', 'lnRNA']
# [] 
