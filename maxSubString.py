import operator

def findMaxSubString(s):
  # substring sem repetição -> Uma sequência de caracteres diferentes e contiguos na string

  word = ''
  size = 0


  for c in s:
    if(word and c in word):
    # ['d', 'dv', 'vd', 'vdf']
    # ['p', 'pw', 'w', 'wk', 'wke', 'w']

      word = word.replace(word[0:word.find(c)+1],'')

    word += c

    if size < len(word):
        size = len(word)

  return size






def main():
  s1 = 'abcabcabc' # -> abc
  s2 = 'dvdf'      # -> vdf
  s3 = 'pkkevk'    # -> kev or evk
  s4 = "pwwkew"    # -> wke
  print(findMaxSubString(s4))

if (__name__ == '__main__'):
  main()