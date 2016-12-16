# This file imports code collected from elsewhere.
# This file isnt actually used, not enough time to implement

def spellchecker(string_in, compare_list):
    word1 = str.lower(string_in)
    for i in compare_list:
        word2 = i
        len_1 = len(word1)
        len_2 = len(word2)
        x = [[0]*(len_2+1) for _ in range(len_1+1)]

        for i in range(0, len_1+1):
            x[i][0] = i
        for j in range(0, len_2+1):
            x[0][j] = j
        for i in range(1, len_1+1):

            for j in range(1, len_2+1):

                if word1[i-1] == word2[j-1]:
                    x[i][j] = x[i-1][j-1]
                else:
                    x[i][j] = min(x[i][j-1], x[i-1][j], x[i-1][j-1])+1

        if 0 <= x[i][j] <= 3:
            return word2
