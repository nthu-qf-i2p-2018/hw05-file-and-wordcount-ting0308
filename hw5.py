import csv
import string

def main(filename):
    with open(filename) as f:
        lines = f.readlines()
        all_words = []
        for line in lines:
            words = line.split()
            for word in words:
                word = word.strip(string.punctuation)
                if word:
                    all_words.append(word)

#open in csv
        a = csv.writer(open("wordcount.csv", "w", newline=''), quoting = csv.QUOTE_ALL)
        a.writerow(['word', 'count'])
        for b in set(all_words):
            a.writerow([b, str(all_words.count(b))])

        
        asd = {}
        for b in set (all_words):
            c = all_words.count(b)
            asd.update({b, c})

#dump into json        
        import json
        json.dump(asd, open("wordcount.json", "w"))

#dump into pickle
        import pickle
        from collections import Counter
        counter = Counter(all_words)
        pickle.dump(counter, open("wordcount.pkl", "wb"))

if __name__ == '__main__':
    main("i_have_a_dream.txt")
    

