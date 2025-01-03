def alphabetize_lists(list1, list2):
  combined_list = list1+list2 # Combine the lists.
  combined_list.sort() # Sort the combined lists.

  print(combined_list)
# Assign the combined lists to the "new_list".
  return combined_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
