def clean_word(word):
  return word.replace(",", "").replace(".", "").replace("?","")

def count_words(text):
  word_dic ={}
  text_list = text.split()
  for word in text_list:
      word = clean_word(word)
      if word in word_dic:
          word_dic[word] = word_dic[word] + 1
      else:
          word_dic[word] = 1

  return word_dic

