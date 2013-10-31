import sys

word_list = {}
points = {}
max_points = 150

def point_total(word):
  total = 0

  for letter in word:
    total += points[letter]

  return total

def setup_points():
  points['a'] = 1
  points['b'] = 4 
  points['c'] = 4 
  points['d'] = 2 
  points['e'] = 1 
  points['f'] = 4 
  points['g'] = 3 
  points['h'] = 3 
  points['i'] = 1 
  points['j'] = 10 
  points['k'] = 5 
  points['l'] = 2 
  points['m'] = 4 
  points['n'] = 2 
  points['o'] = 1 
  points['p'] = 4 
  points['q'] = 10
  points['r'] = 1
  points['s'] = 1
  points['t'] = 1
  points['u'] = 2 
  points['v'] = 5 
  points['w'] = 4 
  points['x'] = 8 
  points['y'] = 3
  points['z'] = 10

def setup_words():
  words = open('wwf_dict')
  
  for word in words:
    word = word.rstrip()
    if not point_total(word) in word_list:
      word_list[point_total(word)] = []
    word_list[point_total(word)].append(word)

def init():
  setup_points()
  setup_words()

def contained(word, characters):
  word_c = {}
  char_c = {}
  
  for letter in word:
    if letter in word_c:
      word_c[letter] += 1
    else:
      word_c[letter] = 1
  
  for letter in characters:
    if letter in char_c:
      char_c[letter] += 1
    else:
      char_c[letter] = 1
  
  for letter in word:
    try:
      if word_c[letter] > char_c[letter]:
        return False
    except KeyError:
      return False
 
  return True

def solve(characters):
  list_words = []
  for point in reversed(range(0, max_points)):
    try:
      for word in word_list[point]:
        if contained(word, characters):
          list_words.append((word, point))
    except KeyError:
      pass

  return list_words

if __name__ == '__main__':
  init()
  listw = solve(sys.argv[1])
  listw = listw[:5]

  for word, point in listw:
    print "Word:", word
    print "Point:", point
