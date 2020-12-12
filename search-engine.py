import time
def matchingWords(sentenceList, query):
    count = []
    for sentence in sentenceList:
        count.append(sentence.lower().count(query.lower()))
    return count

if __name__ == "__main__":
    sentences = ["Python is Python Python cool", "python is good", "python is not python snake"]
    query = input("Enter your query : ")
    counts = matchingWords(sentences, query)
    searchedSentences = [sentence for sentence in sorted(zip(counts, sentences), reverse=True) if sentence[0] != 0]
    print(f"{len(searchedSentences)} results found!")
    for item, value in searchedSentences:
        print(f"\"{value}\" is found {item} times")