# 程式邏輯

'''
1. 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，
   但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，
   請用一個函數來將學生的成績修正。
'''
def fix_score(score_list: list) -> list:
    for idx in range(len(score_list)):
        score_list[idx] = 10 * (score_list[idx] % 10) + int(score_list[idx] / 10)
    return score_list

'''
2. 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，
   請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
'''
def count_letter(text: str):
    text = text.replace(' ','')
    text = sorted([i.upper() for i in text])
    dic = {}
    for i in text:
        if dic.get(i) != None:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.items():
        print(i[0], i[1])

'''
3. QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），
   凡報到3的人退出圈子。請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?
'''
def find_last(n: int):
    last = 0
    for i in range(1, n+1):
        if i % 3 != 0:
            last += 1
    return last

if __name__ == '__main__':
    fix_score([35, 46, 57, 91, 29]) # 1
    count_letter("Hello welcome to Cathay 60th year anniversary") # 2
    find_last(8) # 3

