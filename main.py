def longestPalindrome(string):
  result = ""
  resultLen = 0
  for i in range(len(string)):
    # for odd lengthed palindromes.
    left, right = i, i
    while left >= 0 and right < len(string) and string[left] == string[right]:
      if(right - left + 1) > resultLen:
        result = string[left : right + 1]
        resultLen = right - left + 1
      left -= 1
      right += 1
    # for even lengthed palindromes.
    left, right = i, i + 1
    while left >= 0 and right < len(string) and string[left] == string[right]:
      if(right - left + 1) > resultLen:
        result = string[left : right + 1]
        resultLen = right - left + 1
      left -= 1
      right += 1
  return result
print(longestPalindrome('abababba'))