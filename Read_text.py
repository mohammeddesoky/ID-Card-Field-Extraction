import easyocr
from collections import defaultdict

def Read_text(variables):
  reader_ar = easyocr.Reader(['ar'])
  reader_en = easyocr.Reader(['en'])
  arabic_letters = [
    'ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز',
    'س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك',
    'ل','م','ن','ه','و','ي', 'ى', 'لا', 'ئ', 'أ', 'ة', 'ؤ', 'إ', 'ء'
  ]
  arabic_number = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩']
  special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`', ' '
  ]
  arabic_to_english = {
    '٠': '0',
    '١': '1',
    '٢': '2',
    '٣': '3',
    '٤': '4',
    '٥': '5',
    '٦': '6',
    '٧': '7',
    '٨': '8',
    '٩': '9'
  }
  results = defaultdict(list)
  for var_name, images in variables.items():
      for i, img in enumerate(images):
        if var_name in ['ExpDate', 'IssueDate', 'ID']:
          result = reader_ar.recognize(img, allowlist=arabic_number)
          text = result[0][1]
          text = ''.join(arabic_to_english.get(ch, ch) for ch in text)
          if var_name == 'ExpDate':
            text = text[:4] + "/" + text[5:7] + "/" + text[8:]
          elif var_name == 'IssueDate':
            text = text[:4] + "/" + text[5:]
        elif var_name == 'Serial_Num':
          result = reader_en.recognize(img, blocklist=special_chars)
          text = result[0][1]
          if len(text) > 9:
            text = text[1:]
        elif var_name in ['Religion', 'Status', 'Gender', 'First_Name']:
          result = reader_ar.recognize(img, allowlist=arabic_letters)
          text = result[0][1]
        elif var_name == 'Last_Name':
          result = reader_ar.recognize(img, allowlist=arabic_letters + [' '])
          text = result[0][1]
          text = text.strip()
        else:
          result = reader_ar.recognize(img)
          text = result[0][1]

      results[f"{var_name}"].append(text.strip())
  return results