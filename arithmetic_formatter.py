def arithmetic_arranger(problems, arg=False):

  line1 = []
  line2 = []
  dashes = []
  results = []
  good_operators = ["+","-"]

  for problem in problems:

    if len(problems)>5:
      return "Error: Too many problems."


    elements = (problem.split())

    a = elements[0]
    try:
      a_int = int(a)
    except:
      return "Error: Numbers must only contain digits."


    if len(a) > 4:
      return "Error: Numbers cannot be more than four digits."


    operator = elements[1]

    if operator not in good_operators:
      return "Error: Operator must be '+' or '-'."



    b = elements[2]
    try:
      b_int = int(b)
    except:
      return "Error: Numbers must only contain digits."

    if len(b) > 4:
      return "Error: Numbers cannot be more than four digits."


    if len(a) >= len(b):
      line1.extend(["  ",a,"    "])
      line2.extend([operator,(" "*(len(a)-len(b)+1)),b,"    "])
      dashes.extend([("-"*(len(a)+2)),"    "])
    else:
      line1.extend([(" "*(len(b)+2-len(a))),a,"    "])
      line2.extend([operator," ",b,"    "])
      dashes.extend([("-"*(len(b)+2)),"    "])

    if arg == True:
      if operator == "+":
        result = a_int + b_int
      else:
        result = a_int - b_int

      if len(str(result)) >= 4:
        results.extend([" ", str(result) ,"    "])
      else:
        results.extend(["  ",str(result),"    "])


  line1 = line1[:-1]
  line2 = line2[:-1]
  dashes = dashes[:-1]
  if len(results) > 0:
    results = results[:-1]

  if arg == True:
    arranged_problems = "".join(line1) + "\n" + "".join(line2) + "\n" + "".join(dashes) + "\n" + "".join(results)
  else:
    arranged_problems = "".join(line1) + "\n" + "".join(line2) + "\n" + "".join(dashes)


  return arranged_problems
