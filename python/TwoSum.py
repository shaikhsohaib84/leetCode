class TwoSum:
    '''
        **** TWO SUM ****
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    '''
    def __init__(self, int_lst, target):
        self.int_lst = int_lst
        self.target = target
    
    def twoSum(self, int_lst, target):
        try:
            if int_lst and target:
                target_dict = {}

                for pos in range(len(int_lst)):
                    diff = target - int_lst[pos]

                    if diff in int_lst:
                        if diff in target_dict:
                            return (target_dict.get(diff)[1], pos)
                        else:
                            target_dict.update({int_lst[pos]: [diff, pos]})
            raise Exception('Expected argument not found')
        except Exception as e:
            return(e)

