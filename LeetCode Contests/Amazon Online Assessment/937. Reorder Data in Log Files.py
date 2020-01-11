'''
937. Reorder Data in Log Files
'''


class Solution:
    def reorderLogFiles_opt(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)

    def reorderLogFiles(self, logs):
        logs_words = []

        for x in logs:
            logs_words.append(x.split())

        digit_logs = []
        letter_logs = []

        for x in logs_words:
            if x[-1].isdigit():
                digit_logs.append(x)
            else:
                letter_logs.append(x)

        def f(log):
            return (log[1:], log[0])

        letter_logs.sort(key= f)

        res = []
        for x in letter_logs:
            res.append(' '.join(x))

        for x in digit_logs:
            res.append(' '.join(x))

        return res


sol = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


print(sol.reorderLogFiles_opt(logs))
