# How many Crorepati
# All those who have money more than or equal to 1 crore are known as Crorepati.
# All those who have money money greater than or equal to 1 lakh,
# those are called Lakhpati. Rest of the people are called Dilwale.

kitna_paisa_hai = [3000, 600000, 324990909,
 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
crorepathi=0
lakhpathi=0
dilwale=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        crorepathi+=1
    elif kitna_paisa_hai[i]>=100000:
        lakhpathi+=1
    else:
        dilwale+=1
    i=i+1
print("No.ofcrorepathi:",crorepathi)
print("No.oflakhpathi:",lakhpathi)
print("No.of dilwale:",dilwale)