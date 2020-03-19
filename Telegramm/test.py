# data = {'123123': '1', '1231': '2'}
# with open('Data\\user_rights', 'w') as file:
#     for i in data:
#         file.write(str(i) + ':' + str(data[i]) + ' ')
# with open('Data\\user_rights', 'r') as file:
#     data = file.readline()
# rights = {}
# data = data.split(' ')
# for i in data[0:-1]:
#     i = i.split(':')
#     rights.update({i[0]: i[1]})
# print(rights)
# print(type(rights))
data = {'123': '123'}
if '12' not in data:
    data.update({'12': '12'})
else:
    print(data)
