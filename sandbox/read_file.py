import sys

def print_words(filename:str) -> dict:
  # read file
  f = open(filename, 'rt', encoding='utf-8')
  word_counts = {}
  # loop through all lines in file and split into list
  for line in f:
    line_list = line.split()
    # loop through words in list and add to word_counts dict
    for word in line_list:
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
  # Close file      
  f.close()
  print(word_counts)
  return word_counts

# main 
def main():
  if len(sys.argv) != 2:
    print('usage: ./wordcount.py filename')
    sys.exit(1)

  filename = sys.argv[1]
  print_words(filename)

if __name__ == '__main__':
  main()
