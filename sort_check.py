import logging
logging.basicConfig(
    filename="sorting.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d -%(levelname)s - %(message)s",
    filemode='a'    
)
def sorting(l:list) -> int:
    '''list sorted or not 
    Parameters:
        l(list):input list
    Result:
        bool:gives true or false value
    '''
    logging.info("checking a list is sorted or not")
    s=sorted(l)
    if(s==l):
        logging.info("list is sorted in ascending order")
        return True
    else:
        logging.info("list is not sorted in ascending order")
        return False
ls=[1,2,3,4,5]
result=sorting(ls)
logging.info(result)