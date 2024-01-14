def compare(user_proof, generated_proof):
    results = []
    for line in user_proof:
        line_num = 1
        generated_proof_line = []
        for line_key, line_value in generated_proof.items():
            for element_key, element_value in line_value.items():
                generated_proof_line.append(str(element_value))
        
        assumption_dependence_result = True
        line_number_result = True
        formula_result = True
        justification_result = True

        if line.assumption_dependence != generated_proof_line[0]:
             assumption_dependence_result = False
        if line.line_number != generated_proof_line[1]:
             line_number_result = False
        if line.formula != generated_proof_line[2]:
            formula_result = False
        if line.justification != generated_proof_line[3]:
            justification_result = False
        
        line_results = [assumption_dependence_result, line_number_result, formula_result, justification_result]
        results.append(line_results)
        line_num += 1
    return results