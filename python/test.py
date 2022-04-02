l = [{'deptStockId': 1113, 'quantity': 1}] # {'deptStockId': 1114, 'quantity': 50.0}, {'deptStockId': 1113, 'quantity': 100.0}] # [{'deptStockId': 1113, 'quantity': 1.0}]  
final_lst = []
temp_qty = 0

for i in l:
    qty = float(i.get('quantity')) - temp_qty

    if qty < 0: # -ve(consume current dept stk and iterate more)
        i['quantity'] = float(i.get('quantity'))
        i['to_consume_qty'] = 0
        final_lst.append(i)
        temp_qty -= float(i.get('quantity'))
        temp_qty = abs(temp_qty)
    elif qty == 0: # 0()
        i['to_consume_qty'] = 0.0
        final_lst.append(i)
        break
    elif qty > 0:
        # i['quantity'] += i['quantity'] - temp_qty if temp_qty == 0 else pass  # temp_qty if temp_qty == 0 else qty
        # i['to_consume_qty'] = temp_qty if temp_qty == 0 else qty
        
        if temp_qty == 0:
            i['quantity'] = qty
            i['to_consume_qty'] = 0
        else:
            i['to_consume_qty'] = temp_qty
            i['quantity'] = qty

        final_lst.append(i)
        break