# This function folds a list in the middle n number of times.

# If the list has a odd length, then fold on the middle index (the
#  middle number therefore won't change)
# other wise you fold in the 'gap' between the two middle integers and so
#  all integers are folded.

# To 'fold' the numbers add them together.

# For example:

# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]
# Here we fold the 1st with the last and the second with the 4th. As it is
#  odd in length, the middle index is not folded


def fold_list(list_to_fold, fold_count):
    int_lst_len = len(list_to_fold)

    if fold_count == 1:
        if int_lst_len % 2 == 0:
            int_counter = 0 
            int_lst_len_halved = int_lst_len / 2
            lst_response = []
            while int_counter < int_lst_len_halved:
                int_outcome = list_to_fold[int_counter] + list_to_fold[(int_lst_len - 1)-int_counter]
                lst_response.append(int_outcome)
                int_counter += 1
            return lst_response
        else:
            int_middle_index = int((((int_lst_len + 1) + 1) / 2) - 1)
            int_val_at_middle_index = list_to_fold[int_middle_index]

            del list_to_fold[int_middle_index]

            int_counter = 0 
            int_lst_len_ii = len(list_to_fold)
            int_lst_len_halved = int_lst_len_ii / 2 
            lst_response = []
            while int_counter < int_lst_len_halved:
                int_outcome = list_to_fold[int_counter] + list_to_fold[(int_lst_len_ii - 1) - int_counter]
                lst_response.append(int_outcome)
                int_counter += 1
            lst_response.append(int_val_at_middle_index)
            return lst_response
    else:
        if int_lst_len % 2 == 0:
            int_counter = 0 
            int_lst_len_halved = int_lst_len / 2
            lst_response = []
            while int_counter < int_lst_len_halved:
                int_outcome = list_to_fold[int_counter] + list_to_fold[(int_lst_len - 1)-int_counter]
                lst_response.append(int_outcome)
                int_counter += 1 
            return fold_list(lst_response, fold_count - 1)
        else:
            int_middle_index = int((((int_lst_len + 1) + 1) / 2) - 1)
            int_val_at_middle_index = list_to_fold[int_middle_index]

            del list_to_fold[int_middle_index]

            int_counter = 0 
            int_lst_len_ii = len(list_to_fold)
            int_lst_len_halved = int_lst_len_ii / 2 
            lst_response = []
            while int_counter < int_lst_len_halved:
                int_outcome = list_to_fold[int_counter] + list_to_fold[(int_lst_len_ii - 1) - int_counter]
                lst_response.append(int_outcome)
                int_counter += 1
            lst_response.append(int_val_at_middle_index)
            return fold_list(lst_response, fold_count - 1)

print(fold_list([1,2,3,4,5], 1))
print(fold_list([1,2,3,4,5], 2))
print(fold_list([1,2,3,4,5], 3))