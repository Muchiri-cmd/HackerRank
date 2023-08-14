def minion_game(s):
    p1_score=0#player1 Scoreboard(Stuart)
    p2_score=0#player 2 scoreboard(Kevin)
    
    vowels='AEIOU'
    for i in range(len(s)):
        if s[i] not in vowels:#string pointer not on vowel letter
            """len(string[i:])gets total length of substring(equal total rem nos of permutation).
            Took to long to compile.Not optimal.changed to len(s)-i"""
            #len(s)-1=returns remaining substr equal to...
            p1_score+=len(s)-1#add to player_score_board
        else:
            p2_score+=len(s)-1
    
    #determine winner        
    if p1_score>p2_score:
        print('Stuart',p1_score)
    elif p2_score>p1_score:
        print('Kevin',p2_score)
    else:
        print('Draw')
            
if __name__ == '__main__':
    s = input()
    minion_game(s)