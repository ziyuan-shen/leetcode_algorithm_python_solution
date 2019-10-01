class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_unique = []
        for i in range(len(emails)):
            email = ''
            index = 0
            for j in range(len(emails[i])):
                if emails[i][j] == '@':
                    email += emails[i][j:]
                    break
                elif emails[i][j] == '.' or index == 1:
                    continue
                elif emails[i][j] == '+':
                    index = 1
                    continue
                else:
                    email += emails[i][j]
            if email not in emails_unique:
                emails_unique.append(email)
        return len(emails_unique)
