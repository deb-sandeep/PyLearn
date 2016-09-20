# A function with optional arguments
def fn_with_opt_arguments( name, age=20 ):
    print "Age of ", name, " is ", age, " years."

# -----------------------------------------------------------------------------
# Calling the function without the optional arg
fn_with_opt_arguments( "Argho" )

# Calling the function with an explicit parameter which should overwrite the
# default value of the optional parameter.
fn_with_opt_arguments( "Argho", 30 )