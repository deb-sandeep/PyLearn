# A very simple function explain the skeletal struction of a python function
#
# def       - The keyword to let the interpreter know that we are defining a function
# say_hello - The name of the function. As per the PEP8 conventions, function 
#             names should be lowercase, with words separated by underscores as 
#             necessary to improve readability.
# name      - A parameter being passed to the function, referenced by 'name' 
#             parameter name
# :         - A colon ends the function declaration.
def say_hello( name ):
    # Lines in the method body needs to be indented by four spaces.
    """The first line in a function can be a string, called Docstring which is
    accessible via the __doc__ variable"""
    print "Hello ", name

    print "Docstring for this function : "
    print say_hello.__doc__

# -----------------------------------------------------------------------------
# Execution starts from here.
say_hello( "Sandeep" )
