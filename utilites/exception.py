import sys, os

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.sys
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_numb = exc_tb.tb_lineno
    error_message = f"Error occured python script name {file_name} line number {line_numb} erorrmessage {error}"
    return error_message

class behave_exception(Exception):
    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def _str_self(self):
        return self.error_message


