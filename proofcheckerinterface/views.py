from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import LineItem
import random, string
from .generate_proof import generate_proof, print_proof_table, to_array

def line_exists(line_number):
    line_items = LineItem.objects.all()
    for line in line_items:
        if hasattr(line, "line_number"):
            line_num = getattr(line, "line_number")
            if line_num == line_number:
                return True
    return False

def unpack_lines(line_items):
    line_list = []
    for line in line_items:
        line = [line.line_number, line.formula, line.justification, line.assumption_dependence]
        line_list.append(line)
    return line_list

def index(request):
    # line_items = LineItem.objects.all()
    # # line_list = unpack_lines(line_items)
    # complete_proof_table = {}
    # proof = ''
    # error = ''
    # results = []
    # checked = False
    # if request.method == 'POST' and 'add_line' in request.POST:
    #     line_item = LineItem()
        
    #     if request.POST.get("line_number") != "":
    #         if line_exists(request.POST.get("line_number")) == False:
    #             line_item.line_number = request.POST.get("line_number").replace(' ','')
    #             if request.POST.get("formula") != "":
    #                 line_item.formula = request.POST.get("formula").replace(' ','')
    #                 if request.POST.get("justification") != "":
    #                     line_item.justification = request.POST.get("justification").replace(' ','')
    #                     if request.POST.get("assumption_dependence") != "":
    #                         line_item.assumption_dependence = request.POST.get("assumption_dependence").replace(' ','')
    #                         line_item.save()
    #         else:
    #             error = "Line " + request.POST.get("line_number") + " already exists!"
    #     results += [True, True, True, True]
    # if request.method == 'POST' and 'delete_line' in request.POST:
    #     current_line_number = request.POST['delete_line'][len('Delete Line ')]
    #     if line_exists(current_line_number) == True:
    #         current_line_item = LineItem.objects.get(line_number=current_line_number)
    #         current_line_item.delete()
    if request.method == 'POST' and 'check_proof' in request.POST:
        original_statement = request.POST.get("original_statement")
        try:
            complete_proof_table = generate_proof(original_statement)
            complete_proof_table_array = to_array(complete_proof_table)
        except UnboundLocalError:
            print("Error 1")
        except ValueError:
            print("Error 2")


    #     # table = request.POST.items()
    #     # print(str(original_statement) != '')
    #     # for row in table:
    #     #     name_found=False
    #     #     for item in row:
    #     #         if name_found:
    #     #             print(item)
    #     #             request.POST.set(item, '5')
    #     #             name_found = False
    #     #         if item == "assumption_dependence":
    #     #             name_found = True
    #     #         if item == "line_number":
    #     #             name_found = True
    #     #         if item == "formula":
    #     #             name_found = True
    #     #         if item == "justification":
    #     #             name_found = True
    #         # print(element.line_number)
    #         # print(element.line_number)
    #         # print(element.formula)
    #         # print(element.justification)
    #     try:
    #         if original_statement != '':
    #             proof = str(original_statement).replace(' ', '')
    #             complete_proof_table = setup(proof)
    #             user_proof = line_items
    #             results = compare(user_proof, complete_proof_table)
    #             checked = True
    #             print(results)
    #             print_proof_table(complete_proof_table)
    #     except ValueError:
    #         print(original_statement)
    #         print(ValueError)
    #         error = "'"+original_statement+"'"+' not valid!'
    #     # update_table(results, line_items)
    # if request.method == 'POST' and 'update_line' in request.POST:
    #     current_line_number = request.POST['update_line'][len('Update Line ')]
    #     if line_exists(current_line_number) == True:
    #         current_line_item = LineItem.objects.get(line_number=current_line_number)
    #         current_line_item.assumption_dependence = request.POST.get("assumption_dependence")
    #         current_line_item.line_number = request.POST.get("line_number")
    #         current_line_item.formula = request.POST.get("formula")
    #         current_line_item.justification = request.POST.get("justification")
    #         current_line_item.save()

    return render(request, 
                  'index.html',
                  {'complete_proof_table': complete_proof_table_array,
                   'proof': original_statement})