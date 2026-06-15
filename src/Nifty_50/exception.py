import sys

def get_error_message(error,error_details:sys):
    _,_,etb= error_details.exc_info()
    file_name = etb.tb_frame.f_code.co_filename
    error_message=f'An exception has occured in {file_name} line number {etb.tb_lineno} with error message {str(error).upper()}'
    return error_message

class CustomException (Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message= get_error_message(error_message,error_details)
    def __str__(self):
        
        return self.error_message

