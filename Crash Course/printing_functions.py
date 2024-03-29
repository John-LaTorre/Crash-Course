def print_models(unprinted_designs, complete_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop();
        print("Printing model: " + current_design);
        complete_models.append(current_design);

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ");
    for completed_model in completed_models:
        print(completed_model);
