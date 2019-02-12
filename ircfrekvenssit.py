import sys
import re
fileName = sys.argv[1]

with open(fileName,"r") as filu:
    rivit = filu.readlines()
    frequencies = {}
    predecessors = {}
    prepreds = {}
    for rivi in rivit:
        rivi = re.sub(r'[0-9][0-9]:[0-9][0-9]\s<.*>\s',r'',rivi).strip()
        if re.match(r'^--- Day changed',rivi) or re.match(r'.*?\s-!-\s',rivi):
            continue
        else:
            rivi = rivi.replace("\n","")
            pre = ''
            prepre = ''
            for sana in rivi.split(" "):
                sana = sana.lower().replace("\"","").replace(",","")
                if not sana in frequencies:
                    frequencies[sana] = 1
                else:
                    frequencies[sana] += 1
                if pre:
                    if not pre in predecessors:
                        predecessors[pre] = set() 
                    predecessors[pre].add(sana)
                    if prepre:
                        if not prepre in prepreds:
                            prepreds[prepre] = set()
                        prepreds[prepre].add(sana)
                    prepre = pre
                
                pre = sana

    #for key in sorted(frequencies,key=lambda x: frequencies[x]):
    #    print(key,frequencies[key])

    print("Unique words:",len(frequencies))

    print("Predecessors length:",len(predecessors))

    #print("PREDECESSORS:")
    #for key in sorted(predecessors,key=lambda x: len(predecessors[x])):
    #    print(key,"->")
    #    print("------------------------------------------------------")
    #    print(predecessors[key])
    #    print("------------------------------------------------------")
    #    print()

    import random
    preKeys = [x for x in predecessors.keys()]
    random.shuffle(preKeys)
    #for i in range(0,50):
    #    tulostetut = []
    #    key = preKeys[i]
    #    pre = key
    #    if len(predecessors[pre]) > 0:
    #        print(pre,end=" ")
    #        nextKeys = list(predecessors[pre])
    #        random.shuffle(nextKeys)
    #        nextKey = nextKeys[0]
    #        while nextKey in predecessors and len(predecessors[nextKey]) > 0 and nextKey not in tulostetut:
    #            pre = nextKey
    #            print(pre,end=" ")
    #            tulostetut.append(pre)
    #            if len(predecessors[pre]) > 0:
    #                nextKeys = list(predecessors[pre])
    #                random.shuffle(nextKeys)
    #                nextKey = nextKeys[0]
    #            else:
    #                break
    #        print()
    #        print("---")
            
    lauseita = 0
    i = 0
    while lauseita < 20:

        tulostetut = set()
        lause = ""

        firstKey = preKeys[i]
        i += 1
        nextValues = list(predecessors[firstKey])
        random.shuffle(nextValues)
        valid = ''
        key = ''
        for value in nextValues:
            if value in prepreds:
                valid = value

        if not valid:
            continue
        else:
            lause += " " + valid
            key = valid

        jatketaan = True
        while jatketaan:
            nextValues = list(predecessors[key])
            if nextValues:
                random.shuffle(nextValues)
                valid = ''
                for value in nextValues:
                    if value in prepreds:
                        valid = value

                if not valid:
                    jatketaan = False
                    break
                else:
                    lause += " " + valid
                    key = valid
                    eroteltu = lause.strip().split(" ") 
                    if len(eroteltu) > 50:
                        jatketaan = False
            else:
                jatketaan = False

        eroteltu = lause.strip().split(" ") 
        if len(eroteltu) > 10 and len(eroteltu) < 15:
            print(lause)
            print()
            lauseita += 1
        


        
