import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print(ST.scenes)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes['Home']['Ashley2'])
