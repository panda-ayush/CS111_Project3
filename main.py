######################################################
# Project: Proejct 3 Working With Data
# UIN: 671442036
# repl.it URL: https://replit.com/@CS111-Fall2021/Project-3-AyushPanda4#main.py

######################################################
import csv
import json
import requests
import matplotlib.pyplot as plt
import numpy as np


#gets file data
def get_data_from_file(filename, format=""):

  file = open(filename)

  if format == "":
    new_file = filename.index(".")
    format = filename[new_file + 1:]
  

  if format == "csv":
    reader = csv.reader(file)
    data = []

    for row in reader:
      data.append(row)
    return data

  elif format == "json":
    text = file.read()
    data = json.loads(text)

  return data
  file.close()


#gets data from internet
def get_data_from_internet(url, format = "json"):
  if format == "json":
    r = requests.get(url)
    data = r.json()
    return data

  if format == "csv":
    r = requests.get(url)
    txt = r.textlines 
    lines = txt.split("/n")
    reader = csv.reader(lines)
    data = []
    for row in reader:
      data.append(row)
      return data

#gets the name of the state based on the state code
def get_state_name(state_names, state_code):
  return state_names[state_code]

#gets population of state
def get_state_population(state_populations, state_name):
  for dict in state_populations:
    for state in dict:
      if state == state_name:
        return dict[state]

#finds the index of an item
def get_index_for_column_label(header_row, column_label):
  return header_row.index(column_label)


#main function definitions
def main():
  #gets a dictionary of all state code with the state name
  states_dict = {}
  json_data = get_data_from_file("states_titlecase.json")
  for row in json_data:
    states_dict.setdefault(row["abbreviation"],row["name"])

 
#gets data from csv file
  csv_data = get_data_from_file("tax_return_data_2018.csv")
  #gets list for populations of each state
  temp_populations = get_data_from_internet("https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt")
  populations = []

  for dict in temp_populations:
    for values in dict:
      population = {k.replace(".", ""): v for k, v in dict.items()}
      populations.append(population)
      

#gets the index value for each of the key varaibles
  header_row = csv_data[0]
  total_returns = get_index_for_column_label(header_row , "N1")
  taxable_income_amount = get_index_for_column_label(header_row , "A04800")
  taxable_income_returns = get_index_for_column_label(header_row , "N04800")
  number_of_dependents = get_index_for_column_label(header_row , "NUMDEP")
  
  #Question 1
  average_taxable_income = 0
  total_returns_amount = 0
  taxable_income = 0
  for data in csv_data:
    if data[0] != "STATEFIPS":
      total_returns_amount += int(data[total_returns])
      taxable_income += int(data[taxable_income_amount])
    
  average_taxable_income = (taxable_income/total_returns_amount)*1000
  average_taxable_income = "{:.0f}".format(average_taxable_income)
  

  #Question 2
  Group1 = 0
  Group2 = 0
  Group3 = 0
  Group4 = 0
  Group5 = 0
  Group6 = 0
  total_returns_amount1 = 0
  taxable_income1 = 0
  total_returns_amount2 = 0
  taxable_income2 = 0
  total_returns_amount3 = 0
  taxable_income3 = 0
  total_returns_amount4 = 0
  taxable_income4 = 0
  total_returns_amount5 = 0
  taxable_income5 = 0
  total_returns_amount6 = 0
  taxable_income6 = 0
  for data in csv_data:
    if data[0] != "STATEFIPS":
      if data[3] == "1":
        total_returns_amount1 += int(data[total_returns])
        taxable_income1 += int(data[taxable_income_amount])
      if data[3] == "2":
        total_returns_amount2 += int(data[total_returns])
        taxable_income2 += int(data[taxable_income_amount])
      if data[3] == "3":
        total_returns_amount3 += int(data[total_returns])
        taxable_income3 += int(data[taxable_income_amount])
      if data[3] == "4":
        total_returns_amount4 += int(data[total_returns])
        taxable_income4 += int(data[taxable_income_amount])
      if data[3] == "5":
        total_returns_amount5 += int(data[total_returns])
        taxable_income5 += int(data[taxable_income_amount])
      if data[3] == "6":
        total_returns_amount6 += int(data[total_returns])
        taxable_income6 += int(data[taxable_income_amount])
        
     
  Group1 = (taxable_income1/total_returns_amount1)*1000
  Group1 = "{:.0f}".format(Group1)
  Group2 = (taxable_income2/total_returns_amount2)*1000
  Group2 = "{:.0f}".format(Group2)
  Group3 = (taxable_income3/total_returns_amount3)*1000
  Group3 = "{:.0f}".format(Group3)
  Group4 = (taxable_income4/total_returns_amount4)*1000
  Group4 = "{:.0f}".format(Group4)
  Group5 = (taxable_income5/total_returns_amount5)*1000
  Group5 = "{:.0f}".format(Group5)
  Group6 = (taxable_income6/total_returns_amount6)*1000
  Group6 = "{:.0f}".format(Group6)

  #Question3
  state_taxable_income = {}

  for data in range(1, len(csv_data)):

    row = csv_data[data]
    state_code = row[1]

    if state_code not in state_taxable_income:

      state_taxable_income[state_code] = {"taxable_income": 0}
    state_taxable_income[state_code]["taxable_income"] += int(row[taxable_income_amount])
    
    

  for state_code in state_taxable_income:
    state_name = get_state_name(states_dict, state_code)
    state_population = get_state_population(populations, state_name)
    
    state_taxable_income[state_code]["average"] = (state_taxable_income[state_code]["taxable_income"])/state_population
    state_taxable_income[state_code]["average"] = (state_taxable_income[state_code]["average"])*1000
    state_taxable_income[state_code]["average"] = "{:.0f}".format(state_taxable_income[state_code]["average"])

  # nat_values = state_taxable_income.values()
  # nat_values_list = list(nat_values)
  # plt.bar(state_taxable_income.keys(),nat_values_list, label="Average Taxable Income")
  # plt.legend()
  # plt.savefig("bar1.png")

  #Question4
  state_code_for_questions = input("Enter State Code")
  state_code_for_questions = state_code_for_questions.upper()

  average_taxable_income_state = 0
  total_returns_amount_state = 0
  taxable_income_state = 0
  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      total_returns_amount_state += int(row[total_returns])
      taxable_income_state += int(row[taxable_income_amount])
    
  average_taxable_income_state = (taxable_income_state/total_returns_amount_state)*1000
  average_taxable_income_state = "{:.0f}".format(average_taxable_income_state)

  #Question5
  state_average_taxable_income_agi = {}

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      agi_group = row[3]
      if agi_group not in state_average_taxable_income_agi:
        state_average_taxable_income_agi[agi_group] = 0
      state_average_taxable_income_agi[agi_group] = (int(row[taxable_income_amount])/int(row[total_returns]))
      state_average_taxable_income_agi[agi_group] = state_average_taxable_income_agi[agi_group] *1000
      state_average_taxable_income_agi[agi_group] = "{:.0f}".format(state_average_taxable_income_agi[agi_group])


  #Question6
  avg_dependents_return_agi = {}

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      agi_group = row[3]
      if agi_group not in avg_dependents_return_agi:
        avg_dependents_return_agi[agi_group] = 0
      avg_dependents_return_agi[agi_group] = (int(row[number_of_dependents])/int(row[total_returns]))
      avg_dependents_return_agi[agi_group] = "{:.2f}".format(avg_dependents_return_agi[agi_group])

  #Question7
  percent_returns_nu_tax_income_agi = {}

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      agi_group = row[3]
      if agi_group not in percent_returns_nu_tax_income_agi:
        percent_returns_nu_tax_income_agi[agi_group] = 0
      percent_returns_nu_tax_income_agi[agi_group] = (int(row[taxable_income_returns])/int(row[total_returns]))
      percent_returns_nu_tax_income_agi[agi_group] = 100 - (percent_returns_nu_tax_income_agi[agi_group] *100)
      percent_returns_nu_tax_income_agi[agi_group] = "{:.2f}".format(percent_returns_nu_tax_income_agi[agi_group])
    

  #Question8
  new_state_name = get_state_name(states_dict, state_code_for_questions)
  population_state = get_state_population(populations, new_state_name)
  taxable_income_state8 = 0
  average_taxable_income_per_resident = 0
  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      taxable_income_state8 += int(row[taxable_income_amount])
    
    average_taxable_income_per_resident = taxable_income_state8/population_state
    average_taxable_income_per_resident = average_taxable_income_per_resident *1000
    average_taxable_income_per_resident = "{:.0f}".format(average_taxable_income_per_resident)
      
  #Question9
  percent_returns_each_agi = {}
  total_returns9 = 0

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      total_returns9 += int(row[total_returns])

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      agi_group = row[3]
      if agi_group not in percent_returns_each_agi:
        percent_returns_each_agi[agi_group] = 0
      percent_returns_each_agi[agi_group] = (int(row[total_returns])/total_returns9)
      percent_returns_each_agi[agi_group] = (percent_returns_each_agi[agi_group] *100)
      percent_returns_each_agi[agi_group] = "{:.2f}".format(percent_returns_each_agi[agi_group])
  values = percent_returns_each_agi.values()
  values_list = list(values)
  y = np.array(values_list)
  mylabels = percent_returns_each_agi.keys()

  plt.pie(y, labels = mylabels)
  plt.savefig("pie1_" + state_code_for_questions + ".png") 

  #Question10
  percent_taxable_income_each_agi = {}
  total_taxable_income10 = 0

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      total_taxable_income10 += int(row[taxable_income_amount])

  for data in range(1, len(csv_data)):
    row = csv_data[data]
    state_code = row[1]
    if state_code == state_code_for_questions:
      agi_group = row[3]
      if agi_group not in percent_taxable_income_each_agi:
        percent_taxable_income_each_agi[agi_group] = 0
      percent_taxable_income_each_agi[agi_group] = (int(row[taxable_income_amount])/total_taxable_income10)
      percent_taxable_income_each_agi[agi_group] = (percent_taxable_income_each_agi[agi_group] *100)
      percent_taxable_income_each_agi[agi_group] = "{:.2f}".format(percent_taxable_income_each_agi[agi_group])
  values2 = percent_taxable_income_each_agi.values()
  values_list2 = list(values2)
  y2 = np.array(values_list2)
  mylabels2 = percent_taxable_income_each_agi.keys()

  plt.pie(y2, labels = mylabels2)
  plt.savefig("pie2_" + state_code_for_questions + ".png") 
    
#writes all questions answers to file
  file = open("answers" + state_code_for_questions + ".txt", "w")

  file.write("###################################################\n")
  file.write("Question 1\n")
  file.write("Average taxable income per return across all groups\n")
  file.write("###################################################\n")
  file.write("$   " + average_taxable_income+"\n")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 2\n")
  file.write("Average taxable income per return for each agi group\n")
  file.write("Group 1: $  " + Group1 + "\n")
  file.write("Group 2: $  " + Group2 + "\n")
  file.write("Group 3: $  " + Group3 + "\n")
  file.write("Group 4: $  " + Group4 + "\n")
  file.write("Group 5: $  " + Group5 + "\n")
  file.write("Group 6: $  " + Group6 + "\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 3\n")
  file.write("Average taxable income (per resident) per state\n")
  file.write("###################################################\n")
  for state in state_taxable_income:
    file.write(state + ": $  " + state_taxable_income[state]["average"] + "\n")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("State level informatoi for " + state_code_for_questions +  "\n")
  file.write("###################################################\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 4\n")
  file.write("Average taxable income per return across all groups\n")
  file.write("###################################################\n")
  file.write("$   " + average_taxable_income_state + "\n")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 5\n")
  file.write("average taxable income per return for each agi group \n")
  file.write("###################################################\n")
  for state in state_average_taxable_income_agi:
    file.write("Group " + state + ": $    " + state_average_taxable_income_agi[state] + "\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 6\n")
  file.write("average dependents per return for each agi group\n")
  file.write("###################################################\n")
  for group in avg_dependents_return_agi:
    file.write("Group " + group + ":    " + avg_dependents_return_agi[group] + "\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 7\n")
  file.write("percentage of returns with no taxable income per agi group\n")
  file.write("###################################################\n")
  for group in percent_returns_nu_tax_income_agi:
    file.write("Group " + group + ":    " + percent_returns_nu_tax_income_agi[group] + "%\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 8\n")
  file.write("average taxable income per resident\n")
  file.write("###################################################\n")
  file.write("$   " + average_taxable_income_per_resident + "\n")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 9\n")
  file.write("percentage of returns for each agi_group\n")
  file.write("###################################################\n")
  for group in percent_returns_each_agi:
    file.write("Group " + group + ":    " + percent_returns_each_agi[group] + "%\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")
  file.write("Question 10\n")
  file.write("percentage of taxable income for each agi_group\n")
  file.write("###################################################\n")
  for group in percent_taxable_income_each_agi:
    file.write("Group " + group + ":    " + percent_taxable_income_each_agi[group] + "%\n")
  file.write("\n ")
  file.write("\n ")
  file.write("###################################################\n")

  


  


  file.close()



main()