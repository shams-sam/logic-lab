import re, collections
# tokenise all the words and lowercase them
def words(text): return re.findall('[a-z]+', text.lower())
# dictionary with default value 1
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
# keeping the count of all the words in a big text file
NWORDS = train(words(file('big.txt').read()))
# all the alphabets for operations on the words
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# to operate edit distance one of deletes,transposes,replaces and inserts
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)
# expanding to edit distance 2
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)
# checking if the word passed exists in NWORDS
def known(words): return set(w for w in words if w in NWORDS)
# correcting the word or returning the original word itself if no match found
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)
