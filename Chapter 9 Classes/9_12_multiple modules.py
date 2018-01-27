"""
9-12 Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, 
create an Admin instance and call show_privileges() to show that everything
is still working correctly.
"""

from admin_privilegesInfo import Admin
marc = Admin("marc", "monforte", 27, "blue")
marc.privileges.show_privileges()