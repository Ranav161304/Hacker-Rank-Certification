from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    item_dict = OrderedDict()
    
    for _ in range(N):
        data = input().split()
        item_name = ' '.join(data[:-1])
        item_price = int(data[-1])
        if item_name in item_dict:
            item_dict[item_name] += item_price
        else:
            item_dict[item_name] = item_price
    
    for item, total in item_dict.items():
        print(item, total)
