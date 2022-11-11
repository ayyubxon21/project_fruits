def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    row = data.split('\n')[1:-1]
    price = []
    for i in row:
        price.append(float(i.split(',')[-1]))
       
        return min(price)
    # your code here
        
data=open('fruits.csv').read()
print(get_cheapest_fruit(data))