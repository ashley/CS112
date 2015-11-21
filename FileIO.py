def main():
    f = open("bestOfTimes.txt","r") #open up a file
    dict = {}
    word = []
    for line in f:
        word.append(line.strip() + ' ')
        lyrics = ''.join(word)
     	#print(lyrics)
        lyrics = lyrics.split(' ')
    print(lyrics)
    
    n = 1
    if n == 1:
        for i in range(len(lyrics)):
            if lyrics[i] in dict:
                dict[lyrics[i]] += 1
            else:
                dict[lyrics[i]] = 1
            
        print(dict)
        strin = ""
	
	        
   	strin = "\n" + "These words appear more than twice: "
    m = 1
    if m == 1:
        for key in dict:
            if dict[key] > 2:
                strin += " "  + str(key)
        print("\n " + "Words appearing more than twice has been appended to lyrics text file")
        f = open("bestofTimes.txt","a")
        f.write(strin)
        f.close
main()
