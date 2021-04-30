import os
def parse(fp):

  if (".dsmd" in fp):
    pass 
  else:
    raise Exception("That is not a dsmd file.")

#fp = "README.dsmd"
# Using readlines()
  file1 = open(f'{fp}', 'r')
  eee = fp.replace('.dsmd', '')
  file2 = open(f'{eee}.md', 'w')
  file2.close()
  Lines = file1.readlines()
  read_line = True
  count = 0
  # Strips the newline character
  for line in Lines:
    count += 1
    def comment():
      data = line 
      # data = data.replace(")", "")
      data = data.replace("\n", "")
      return "[//]: # (" + data + ")"
    def h1_TAG():
      data = line
      spl_word = '#'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "", 1)
          ress = check.replace("**>", "", 1)
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "", 1)
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress

      return "# " + res
    def h2_TAG():
      data = line
      spl_word = '##'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "")
          ress = check.replace("**>", "")
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "")
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress
      return "## " + res
    def h3_TAG():
      data = line
      spl_word = '###'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "")
          ress = check.replace("**>", "")
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "")
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress
      return "### " + res
    def h4_TAG():
      data = line
      spl_word = '####'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "")
          ress = check.replace("**>", "")
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "")
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress
      return "#### " + res
    def h5_TAG():
      data = line
      spl_word = '#####'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "")
          ress = check.replace("**>", "")
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "")
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress
      return "##### " + res
    def reg_TAG():
      data = line
      spl_word = '>'
      try:
        res = data.partition(spl_word)[2]   
        res = data.partition("(")[2]
      except:
        raise Exception("No header text found.")
      split_string = res.split(")", -1)
      res = split_string[0]
      ress = res
      if "<**" in ress:
        if "**>" in ress:
          start = "<**"
          end = "**>"
          check = ress[ress.find(start) + len(start):ress.rfind(end)]
          ress = check.replace("<**", "")
          ress = check.replace("**>", "")
          check = "**" + ress + "**"
          res = res + check
          res = res.replace(f"<**{ress}**>", "")
      if ("|" in ress):
          resss = ress
          start = "|"
          end = "|"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          if ("https://" in ress):
            e_link = resss
            link = "(" + resss + ")"
          else:
            e_link = resss
            link = "(https://" + resss + ")" 
          resss = ress
          start = "{"
          end = "}"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("{", "", 1)
          resss = check.replace("}", "", 1)
          e_text = resss
          text = "[" + resss + "]"
          ress = ress.replace(f"|{e_link}|{{{e_text}}}", f"{text}{link}", 1)
          ress = ress.replace("\n", "")
          ress = ress.rstrip("\n")
          res = ress
      return res
    def code_TAG():
      if ("$" in line):
          resss = line
          start = "$"
          end = "$"
          check = resss[resss.find(start) + len(start):resss.rfind(end)]
          resss = check.replace("|", "", 1)
          resss = check.replace("|", "", 1)
          # data is in resss 
          if ("[" and "]" in resss):
            res = resss 
            start = "["
            end = "]"
            check = res[res.find(start) + len(start):res.rfind(end)]
            res = check.replace(f"[{check}]", "", 1)
            res = check.replace(f"[{check}]", "", 1)
            resss = resss.replace(f"[{check}]", "", 1)
            if (";" in resss):
              resss = resss.replace(";", ";\n")
            return f"``` {res}\n{resss}\n```"
          else:
            raise Exception("No lang markdown syntax highlight was found. If you want to not have a lang syntax highlight, please put an empty [].")
    if ("$" in line):
      if (read_line == True):
        eee = code_TAG()
        read_line = False
    elif ("#####" in line):
      if (read_line == True):
        eee = h5_TAG()
        read_line = False
    elif ("####" in line):
      if (read_line == True):
        eee = h4_TAG()
        read_line = False
    elif ("###" in line):
      if (read_line == True):
        eee = h3_TAG()
        read_line = False
    elif ("##" in line):
      if (read_line == True):
        eee = h2_TAG()
        read_line = False
    elif ("#" in line):
      if (read_line == True):
        eee = h1_TAG()
        read_line = False
    elif (">" in line):
      if (read_line == True):
        eee = reg_TAG()
        read_line = False
    elif (line == ""):
      eee = ""
      read_line = ""		
    else:
      eee = comment()
      read_line = False
    fp = fp.replace(".dsmd", "")
    file1.close()
    file1 = open(f"{fp}.md", 'a')
    file1.write(eee)
    if (eee == ""):
      pass
    else:
      file1.write("\n\n")
      file1.close()
    read_line = True
  print("Parsed successfully!")
#parse("README.dsmd")
