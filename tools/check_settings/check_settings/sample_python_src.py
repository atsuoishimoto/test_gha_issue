import IMP_1
import IMP_2.IMP_2_1
import IMP_3 as IMP_3_AS
from IMP_4 import IMP_4_FROM_IMPORT
from IMP_5 import IMP_5_FROM_IMPORT as IMP_5_FROM_IMPORT_AS


GLOBAL1=(1+GLOBAL_REF/2,)
(ASSGIN_EXPR:= 1999,)


if IF_REF:
    IF_GLOBAL=200

ASSIGN_ATTR1.ASSIGN_ATTR1_1.ASSIGN_ATTR1_2.ASSIGN_ATTR1_3= 1000
(1+2).ASSIGN_ATTR2_1.ASSIGN_ATTR2_2 = 300

def FUNC1():
    global GLOBAL_FUNC1_1
    ASSGIN_FUNC = REF_FUNC1
    ASSGIN_FUNC_ATTR1.ASSGIN_FUNC_ATTR1_1 = REF_FUNC_ATTR1.REF_FUNC_ATTR1_2

    def INNER_FUNC1():
        global INNER_FUNC1_GLOBAL_1
        ASSGIN_INNER_FUNC1 = REF_INNER_FUNC1

    EXTERNAL_FUNCTION(FUNC1_FUNC_ARG)

class XXX:
    ABC = 100

