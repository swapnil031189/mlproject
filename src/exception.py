import sys
from src.logger import logging

def erorr_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  #info about exception- like which file, line number all those details will be stored in exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename # custom document handling documentation
    error_message = "Error occured in Python Script name [{0}, line number [{1}]] and error message is [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = erorr_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
    
#     except Exception as e:
#         logging.info("Divide by Zero Error")
#         raise CustomException(e,sys)
    