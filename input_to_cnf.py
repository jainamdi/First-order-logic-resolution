from itertools import islice
kbin = open('input.txt', 'r')
number_of_queries = int(kbin.readline().strip())
allqueries = []
#print("number of queries : ", number_of_queries)
for i in range(number_of_queries):
    oneq = kbin.readline().split()
    allqueries.append(oneq)
#print("all queries : ", allqueries)
number_of_kb_sentences = int(kbin.readline().strip())
#print("number of kb sentences = ", number_of_kb_sentences)
allkbsentences = []
for i in range(number_of_kb_sentences):
    #onekb = kbin.readline().split()
    allkbsentences.append(kbin.readline().split())
#print("all kb sentences : ", allkbsentences)

#for line in islice(kbin, 0, number_of_kb_sentences):
        #cnf = str(line.strip())
 #       allkbsentences.append(str(line.strip()))
        #print(cnf)
kbin.close()
#print("\nall kb sentences : ", allkbsentences)
#res = []
#res[:0] = allkbsentences
#print("srfnvljsn : ", str(res))
#def tostorequeries():

def convert_to_cnf():
    result_in_cnf = []
    for a_kb_sentence in allkbsentences:
        for operator in a_kb_sentence:
            if operator == "=>":
                result_in_cnf = to_eliminate_implication(a_kb_sentence)
                index = allkbsentences.index(a_kb_sentence)
                #print("index of atom : ", index)
                allkbsentences[index] = result_in_cnf
     #           print("unimply  : ", a_kb_sentence)
            #if operator == "&":
                #result_in_cnf = to_eliminate_and(a_kb_sentence)
                #print("un and : ", result_in_cnf)
    #for a_kb_sentence in allkbsentences:
     #   result_in_cnf = to_move_negation_in(a_kb_sentence)


def to_eliminate_implication(sentence):
    result = []
    pre_operator = ["~", "{"]
    operator = ["|"]
    post_operator = []
    for i in sentence:
        if i != "=>":
            pre_operator.append(i)
        else:
            break
    pre_operator.append("}")
    index_of_implication = sentence.index("=>")
    for i in range((index_of_implication+1), len(sentence)):
        post_operator.append(sentence[i])
    #print("pre_operator : ", pre_operator)
    #print("post_operator : ", post_operator)
    result = pre_operator + operator + post_operator
    result = to_move_negation_in(result)
    #print("re : ", result)
    return result

def to_move_negation_in(sentence):
    result = []
    index_of_and = 0
   # print("sentence : ", sentence)
#    index_of_outer_bracket = sentence.index("start_negating")
    for i in sentence:
        if i != "}":
            if i == "&":
                index_of_and = sentence.index(i)
                sentence[index_of_and] = "|"
            if i == "~":
                sentence.remove("~")
        else:
            break
    for i in sentence:
        if i != "}":
            if i == "{":
                sentence.remove("{")
    non_neg = ""
    nn = ""
    n = ""
    index_of_nn = 0
    index_of_n = 0

    for i in sentence:
        if i != "}":
            #print("i : ", i)
            if i[0] == "~":
                non_neg = list(i)
                #print("nn : ", non_neg)
                non_neg.remove("~")
                #print("after nn : ", non_neg)
                for j in range(len(non_neg)):
                    #print("j : ", j, non_neg[j])
                     nn = nn + non_neg[j]
                #print("non neg list element : ", nn)
                index_of_nn = sentence.index(i)
                sentence[index_of_nn] = nn
            else:
                if i[0] != "|":
                    n = "~" + i
                    index_of_n = sentence.index(i)
                    sentence[index_of_n] = n
        else:
            break
             #   neg = list(i)
              #  print("i : ", neg)
    index_of_outer_bracket = 0
    for i in sentence:
        if i == "}":
            sentence.remove("}")


#    index_of_outer_bracket = sentence.index("")
    #sentence.pop(index_of_outer_bracket)
    result = sentence
    #print("sentence  : ", result)
    return result
#                print("sn : ", i)
    #print("sentence : ", sentence)
            #if len(i) == 1:

convert_to_cnf()
print("\nfinal kb : ", allkbsentences)

j = []
l = []
#l1 = [1]

for a in allkbsentences:
    li = len(a)
    l1 = []
    for i in range(li):
        l1.append(1)
    inpu = iter(a)
    l = [list(islice(inpu, i)) for i in l1]
    #for b in a:
    #    l.append(b)
    j.append(l)
#print("b : ", j)
allkbsentences = j
print("list : ", allkbsentences)

for q in allqueries:
    result = []
    result = to_move_negation_in(q)
    print("result : ", result)



























"""
def to_eliminate_implication(sentence):
    #print("sentence : ", sentence)
    result = []
    index_of_implication = 0
    pre_operator = "~("
    operator = ""
    post_operator = "("
#    pre_operator, operator, post_operator = sentence
    for atom in sentence:
        if atom != "=>":
            #print("atom : ", atom)
            pre_operator = pre_operator + atom
        else:
            break
    pre_operator = pre_operator + ")"
    operator = "|"
    index_of_implication = sentence.index("=>")
    #print("index : ", index_of_implication)
    for i in range((index_of_implication + 1), len(sentence)):
        post_operator = post_operator + sentence[i]
    post_operator = post_operator + ")"

    to_move_negation_invard([pre_operator])
    to_move_negation_invard([post_operator])
    result.append(pre_operator)
    result.append(operator)
    result.append(post_operator)
    #print("result : ", result)
    return result
"""
"""
def to_move_negation_invard(sentence):
    #sentence = list(sentence)
    #print("sentence : ", sentence)
    rem = ""
    re = []
    x = 0    #index of operator
    for atom in sentence:
        #print("atom : ", atom)
        if atom[0] == "~":
            if atom[2] == "~":
                print("double neg atom : ", atom)
                for i in range(3, len(atom)):
                    if atom[i] == "&":
                        x = i
                        print("i : ", i)
                    rem = rem + atom[i]
                print("index of & : ", x)
                re = list(rem)
                re[x-3] = "|"
                print("rermaining atom : ", re)
                    #if atom[i] == ""
            else:
                continue
"""


"""
def to_eliminate_and(sentence):
    result = []
    pre_operator = ""
    operator = ""
    post_operator = ""
    for atom in sentence:
        if atom != "&":
            pre_operator = pre_operator + atom
        else:
            break
    #print("preoperator : ", pre_operator)
    index_of_and = sentence.index("&")
    for i in range((index_of_and + 1), len(sentence)):
        post_operator = post_operator + sentence[i]
    for i in post_operator:
        if i == "&":
            x = to_eliminate_and()
        else:
            break

    result.append([pre_operator])
    result.append([post_operator])

    return result
"""
