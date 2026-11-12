class Solution:
    def isPalindrome(self, s: str) -> bool:
        # obtain clean palindrome
        clean_string = ""

        # 
        # traverse s
        for char in s:
            if char.isalnum():
                clean_string += char.lower()

        
        return clean_string == clean_string[::-1]