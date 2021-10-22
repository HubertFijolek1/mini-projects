sentence = "skaerf nohtyp lla ot olleh"

# correct_sentence = []
# for i in sentence.split(" "):
#     correct_sentence.append(i[::-1])
# correct_sentence.reverse()
# correct_sentence=" ".join(correct_sentence)

# print(correct_sentence)

list1 = []
correct_sentence=[i[::-1] for i in sentence.split(" ") ]
correct_sentence.reverse()
print(correct_sentence)
