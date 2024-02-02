# Assume you have a method isSubstring which checks 
# if one word is a substring of another.
# Given two strings, s1 and s2, write code to check 
# if s2 is a rotation of s1 using only one call to 
# isSubstring (e.g., "watterbottle" is a rotation of "erbottlewat")
# "watter"

class Solution:
  def isSubstring(self, s1, s2):
      s1 = list(s1)
      left, right = [], s1

      for i in range(len(s1)):
          left.append(s1[i])
          right = right[1:]  # Updated: remove the first element

          subs1 = ''.join(left + right)
          subs2 = ''.join(right + left)

          if subs1 == s2 or subs2 == s2:
              return True
      return False

    
