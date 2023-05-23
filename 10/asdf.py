from collections import defaultdict
from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        default_letters = defaultdict(int)


        # это счетчик сколько и каких букв нам надо найти подряд
        for s in s1:
            default_letters[s] += 1
        

        letters = default_letters.copy()
        start = 0

        for i, s in enumerate(s2):

            # Если буква в есть в первом слове, вычитаем ее из счетчика
            if s in letters:
                letters[s] -= 1

                # Если мы добавили в скользящее окно лишнюю букву, надо укоротить окно до момента пока не удалим из окна самую левую такую же букву
                while(letters[s] < 0 and start <= i):
                    letters[s2[start]] += 1
                    start += 1
            else:
                # Если мы встретили букву, которой нет в слове, мы заново строим первоначальный счетчик и скользящее окно начинаем строить снова со след символа
                start = i + 1
                letters = default_letters.copy()
            
            # Проверяем длину окна
            if i - start + 1 == len(s1):
                return True
        
        return False



sol = Solution()


