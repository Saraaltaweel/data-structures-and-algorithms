def BinarySearch(list,val):

        indx_first=0
        indx_last=len(list)-1

        while indx_first <= indx_last:
          middle_val=len(list-1)/2
          middle_val_num=list[middle_val]
          if middle_val_num==val:
              return middle_val
          elif middle_val_num>val:
              indx_last=middle_val+1   
          elif middle_val_num<val:
              indx_firstt=middle_val-1      
        return -1      
