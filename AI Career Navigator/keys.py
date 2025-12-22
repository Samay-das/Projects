# importing os module to set the environmental variable
import os

# Setting the environmental variable using .environ class 
os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY'

# And storing the environmental variable into the variable 
api_key = os.environ.get('GOOGLE_API_KEY')

"""
If you are using Window Operating System declaring
environmental variable is quite tricky so use it.
And if you are using Linux based Operating System 
simplily write this below command to set the environmental 
variable:
>>> export api_key="YOUR_API_KEY"
"""