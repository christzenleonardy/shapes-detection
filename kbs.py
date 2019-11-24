import clips
import os
import image_processing

def run_kbs(img_path, desired_result):
  env = clips.Environment()
  env.load('kbs.clp')

  points, lines = image_processing.get_img_fact(img_path)

  # GANTI INI DENGAN INPUT DARI PAGE!!!
  input = desired_result

  # Memasukkan daftar fact berdasarkan input dari opencv
  initial_facts = []

  fact_string = "(n-point "+str(len(points))+")"
  initial_facts.append(fact_string)
  env.assert_string(fact_string)

  i = 0
  for point in points:
      fact_string = "(point " + str(i+1) + " " + str(point[0]) + " " + str(point[1]) + " " + str(lines[i][0]) +")"
      initial_facts.append(fact_string)
      env.assert_string(fact_string)
      i = i + 1

  i = 0
  for line in lines:
      fact_string = "(line " + str(i+1) + " " + str(line[1]) +")"
      initial_facts.append(fact_string)
      env.assert_string(fact_string)
      i = i + 1

  env.run()

  # Menyiapkan hasil inferensi dalam bentuk array-array
  matched_facts = []
  fired_rules = []
  result_list=[]

  for fact in env.facts():
      print(fact)

  for fact in env.facts():
      if ("matched-fact" in str(fact)):
          split = str(fact).split("(")
          fact_name = split[1][13:(len(split[1])-1)]
          #print(fact_name)
          matched_facts.append(fact_name)
      elif ("fired-rule" in str(fact)):
          split = str(fact).split("(")
          rule_name = split[1][11:(len(split[1])-1)]
          #print(rule_name)
          fired_rules.append(rule_name)
      elif("true" in str(fact)):
          if(not('matched-fact' in str(fact))):
              result_list.append(str(fact).split("(")[1].split()[0])

  #print(result_list)

  if (input in result_list):
      hasil = "succeed"
  else:
      hasil = "failed"

  #print(hasil)

  #print(matched_facts)
  #print(fired_rules)

  return hasil, matched_facts, fired_rules, result_list, initial_facts

# hasil, matched_facts, fired_rules, result_list, a = run_kbs('./shape/segitiga_samasisi.jpg', 'segitiga-sama-sisi')
# print(result_list)