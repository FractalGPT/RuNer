from transformers import QuestionAnsweringPipeline, AutoModelForQuestionAnswering, AutoTokenizer
import pymorphy2
import re
analyzer = pymorphy2.MorphAnalyzer()

# Нормализация текста на русском
def text_normal(text):
  '''Нормализация текста на русском'''
  txt = re.sub('[^А-Яа-яёЁ0-9A-Za-z -+*/=^]', '', text)
  txt = re.sub(' +', ' ', txt)
  txt = txt.strip(' ')

  words = [analyzer.parse(word)[0].normal_form for word in txt.split(' ')]


  return ' '.join(words)


# Поиск неров на русском языке на базе QA модели (возвращает словарь 1 Ner, каждого типа на 1 текст)
class RuNerQA():

  def __init__(self, model_name):
    '''Поиск неров на русском языке (возвращает словарь 1 Ner, каждого типа на 1 текст)'''
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    self.qap = QuestionAnsweringPipeline(model, tokenizer)

  # Поиск именованной сущности
  def SearchNer(self, text, q, p = 0.35):
    '''Поиск именованной сущности'''
    ans = self.qap(context = text, question = q, top_k = 1)
    answers = []
    if ans['score'] >= p:
      return text_normal(ans['answer'])
    else:
      return None

  # Поиск неров
  def NerDetection(self, ner_list, text):
    '''Поиск неров'''
    ners = [{ner:self.SearchNer(text, f"Какой {ner}?")} for ner in ner_list]
    return ners
