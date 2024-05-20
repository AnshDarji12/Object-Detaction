import sys

def error_message_detail(error,error_detail: sys):
    _, _, exc_tb = error_detail.exc_info
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_massege = "Error occurred python script name [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno, str(error)
        
    )
    
    return error_massege

class SignLanguage(Exception):
    def __init__(self,error_massege,error_detail):
        super().__init__(error_massege)
        self.error_massege = error_message_detail(
            error_massege,error_detail=error_detail
        )
def __str__(self):
    return self.error_massege