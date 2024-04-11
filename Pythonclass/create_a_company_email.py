full_name = input("Enter your full name: ")
company_name = input("Enter your company name: ")

splitted_full_name = full_name .split()
joined_full_name = "." .join(splitted_full_name)

splitted_company_name = company_name .split()
joined_company_name = "".join(splitted_company_name)
predicted_email = f"{joined_full_name}@{joined_company_name}.com.au "
print(predicted_email)

#  create email format with replace function

full_name = input("Enter your full name: ")
company_name = input("Enter your company name: ")
fullnamere = full_name .replace(" ", ".")
fullcompanynamere = company_name .replace(" ","")
eamil = f" {fullnamere}@{fullcompanynamere}.com.au " .upper()
print(eamil)