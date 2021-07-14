from auth import authenticate
from datetime import datetime
run_time = datetime.now()
get_time = run_time.strftime("%d-%m-%y  %H:%M:%S")


def resource_deco(email='example@email.com', password='example123'):
    def confirm_access(func):
        personnel = authenticate(email,password)
        def wrapper():
            if personnel:
                if personnel['role']=='admin' or personnel['role']=='superadmin':
                    func()
                    result = f"{personnel['first_name']} {personnel['last_name']}\n {func()}"
                    with open('access_granted.txt','a') as file:
                        file.write(f"\n{personnel['role'].title() } {personnel['first_name']} {personnel['last_name']} tried to view this resource at {get_time}")
                    return result

                elif personnel['role']!= 'admin' or personnel['role'] != 'superadmin':
                    result2 = (f"{personnel['first_name']} {personnel['last_name']}\nYou are not allowed to view this resource")
                    with open("access_denied.txt", 'a') as file:
                        file.write(f"\n{personnel['role'].title() }{personnel['first_name']}{personnel['last_name']} tried to view this resource at {get_time}")
                    return result2
            else:
                return "Only staff can access this resource" 
        return wrapper

    return confirm_access
