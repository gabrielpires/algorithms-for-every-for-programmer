import time

"""

The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, 
determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit 
and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a 
fixed-size knapsack and must fill it with the most valuable items.

"""


def knapsack_without_dynamic(bag_limit, items_value, items_weight, number_items):
    """
     This function calculate in recursive mode the value.

     Parameters:
         int bag_limit
         list items_value
         list items_weight
         int number_items

     Returns:
         int
     """
    if number_items == 0 or bag_limit == 0:
        return 0


    if items_weight[number_items - 1] > bag_limit:
        return knapsack_without_dynamic(bag_limit, items_value, items_weight, number_items - 1)

    else:
        return max(items_value[number_items - 1] + knapsack_without_dynamic(bag_limit - items_weight[number_items - 1],
                items_value, items_weight, number_items - 1), knapsack_without_dynamic(bag_limit, items_value, items_weight, number_items - 1))


def knapsack_with_dynamic(bag_limit, items_value, items_weight, number_items):
    """
       This function calculate and store the result into a matrix where we can retrieve the solution at the end

       Parameters:
           int bag_limit
           list items_value
           list items_weight
           int number_items

       Returns:
           int
       """
    matrix = [[0 for x in range(bag_limit + 1)] for x in range(number_items + 1)]
    # Table in bottom up manner
    for i in range(number_items + 1):
        for w in range(bag_limit + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif items_weight[i - 1] <= w:
                matrix[i][w] = max(items_value[i - 1] + matrix[i - 1][w - items_weight[i - 1]], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]
    return matrix[total_items][bag_limit]


def execution_time(started):
    print('Executed in:', round(time.time() - started, 4), ' seconds')


items_value = [50, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
items_weight = [8, 16, 32, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
total_items = len(items_value)
limit = 1150

# without dynamic programming
start = time.time()
print(knapsack_without_dynamic(limit, items_value, items_weight, total_items))
execution_time(start)

# with dynamic programing
start = time.time()
print(knapsack_with_dynamic(limit, items_value, items_weight, total_items))
execution_time(start)
