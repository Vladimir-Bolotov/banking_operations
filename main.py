import functions

operations = functions.reading_operations()
executed_operations = functions.executed_operations(operations)
sorted_operations = functions.sorted_operations(executed_operations)
last_operations = functions.get_last_operations(sorted_operations)
print_operations = functions.preparing_printing(last_operations)
functions.print_last_operations(print_operations)
