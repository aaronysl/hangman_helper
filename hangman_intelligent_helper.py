from collections import Counter
import re

class HangmanHelper:

    @staticmethod
    def find_words_contains_x(x, word_list, target_len):
        """find possible target words if contains correctly guessed letters. """
        res = {}
        if len(x)==0: # return length-matched words if first try
            for w in word_list:
                if len(w)==target_len:
                    res[w]=1
            return res.keys()
        else:
            for w in word_list:
                for k, v in x.items():
                    if k >= len(w):
                        continue
                    if w[k] == v:
                        res[w] = res.get(w, 0) + 1
            max_value = max(res.values())
        res_words = [k for k, v in res.items() if v >= max_value and len(k) == target_len]
        return res_words

    @staticmethod
    def find_most_appear_letter(words_list, correct_dict):
        """find most probable letter if it has the most occurrences among all letters. """
        c = Counter(''.join(words_list))
        next_letter_tuple = c.most_common()
        for t in next_letter_tuple:
            if t[0] not in correct_dict.values():
                next_letter = t[0]
                break
        return next_letter

    def guess_next_letter(self, pattern, used_letters, word_list):
        target_len = len(pattern)
        if len(used_letters) == target_len: # if guessed chances reaches limit, return None
            return None

        # ***********  find correctly guessed letters  ***********
        alphabet_pattern = r'[a-z]+'
        correct_group = re.finditer(alphabet_pattern,pattern)
        correct_dict = {}
        for l in correct_group:
            correct_dict[l.span()[0]]=l.group()

        target_words = self.find_words_contains_x(correct_dict,word_list,target_len)
        next_letter = self.find_most_appear_letter(target_words,correct_dict)
        return next_letter


