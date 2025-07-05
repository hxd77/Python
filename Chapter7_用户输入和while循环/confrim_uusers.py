#首先，创建一个待验证的用户列表
#和一个用于存储已验证用户的空列表
unconfirm_users=['alice','brian','candace']
confirm_users=[]

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中
while unconfirm_users:
    current_number=unconfirm_users.pop()
    print("Verifying user: "+current_number.title())
    confirm_users.append(current_number)

#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirm_number in confirm_users:
    print(confirm_number.title())