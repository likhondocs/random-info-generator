import requests
from lxml import html

class Fauxid():
    def __init__(self, country=None, number=10, personal_data=True, bank_data=True,
                    cryptocurrency_data=True, internet_data=True, education_data=True,
                        company_data=True) -> None:
        if country:
            self.url = "https://fauxid.com/fake-name-generator/"+country
        else:
            self.url = "https://fauxid.com/fake-name-generator/"
        self.country = country
        self.number = number
        self.personal_data = personal_data
        self.bank_data = bank_data
        self.cryptocurrency_data = cryptocurrency_data
        self.internet_data = internet_data
        self.education_data = education_data
        self.company_data = company_data

    def get_personal_data(self):
        name = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/span/text()")[0]
        address = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/address/text()")[0].replace('\n', '')
        phone = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[4]/span/text()")[0]
        socialSecurityNumber = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[5]/span/text()")[0]
        dateOfBirth = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[1]/div[1]/div/span[1]/text()")[0]
        height = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[1]/div[2]/div/span[2]/text()")[0]
        weight = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[1]/div[3]/div/span[2]/text()")[0]
        gender = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[1]/div/span/text()")[0]
        hairColor = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[2]/div/span/text()")[0]
        eyeColor = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[3]/div/span/text()")[0]
        ethnicity = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[4]/div/span/text()")[0]
        bloodType = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[5]/div/span/text()")[0]
        return{
            "personal_data":{
                "name":f"{name}",
                "address":f"{address}",
                "phone":f"{phone}",
                "socialSecurityNumber":f"{socialSecurityNumber}",
                "dateOfBirth":f"{dateOfBirth}",
                "height":f"{height}",
                "weight":f"{weight}",
                "gender":f"{gender}",
                "hairColor":f"{hairColor}",
                "eyeColor":f"{eyeColor}",
                "ethnicity":f"{ethnicity}",
                "bloodType":f"{bloodType}"
                }
            }

    def get_bank_data(self):
        creditCardNumber = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div[1]/span/code/text()")[0]
        expDate = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div[2]/span[1]/text()")[0]
        cvv = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div[2]/span[2]/text()")[0]
        bankName = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[2]/div[1]/span/text()")[0]
        bankAccountNumber = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[2]/div[2]/span/code/text()")[0]
        routingNumber= self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[2]/div[3]/span/code/text()")[0]
        iban = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[6]/div/div/div[2]/div[4]/span/code/text()")[0]
        return{
            "banking_data":{
                "creditCardNumber":f"{creditCardNumber}",
                "expDate":f"{expDate}",
                "cvv":f"{cvv}",
                "bankName":f"{bankName}",
                "bankAccountNumber":f"{bankAccountNumber}",
                "routingNumber":f"{routingNumber}",
                "iban":f"{iban}"
                }
            }

    def get_cryptocurrency_data(self):
        bitcoinAddress = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[7]/div/div/div[1]/div/span/code/text()")[0]
        ethereumAddress = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[7]/div/div/div[2]/div/span/code/text()")[0]
        return{
            "cryptocurrency_data":{
                "bitcoinAddress":f"{bitcoinAddress}",
                "ethereumAddress":f"{ethereumAddress}"
                }
            }

    def get_internet_data(self):
        username = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[1]/div[1]/span/text()")[0]
        password = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[1]/div[2]/span/code/text()")[0]
        uniqueUserIdentifier = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[1]/div[4]/span/code/text()")[0]
        IPAddressIPv4 = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[2]/div[1]/span/code/text()")[0]
        IPAddressLocal = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[2]/div[2]/span/code/text()")[0]
        MACAddress = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[2]/div[3]/span/code/text()")[0]
        IPAddressIPv6 = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[2]/div[4]/span/code/text()")[0]
        website = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[8]/div/div[1]/div[1]/div[5]/span/text()")[0]
        return{
            "internet_data":{
                "username":f"{username}",
                "password":f"{password}",
                "uniqueUserIdentifier":f"{uniqueUserIdentifier}",
                "IPAddressIPv4":f"{IPAddressIPv4}",
                "ipAddressLocal":f"{IPAddressLocal}",
                "MACAddress":f"{MACAddress}",
                "IPAddressIPv6":f"{IPAddressIPv6}",
                "website":f"{website}",
            }
        }

    def get_education_data(self):
        educationLevel = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[9]/div/div/div[1]/div/span/text()")[0]
        university = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[9]/div/div/div[2]/div/span/text()")[0]
        return{
            "education_data":{
                "educationLevel":f"{educationLevel}",
                "university":f"{university}"
            }
        }

    def get_company_data(self):
        shortCompanyName = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[1]/div[1]/span[1]/text()")[0]
        longCompanyName = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[1]/div[1]/span[2]/i/text()")[0]
        companyDescription = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[1]/div[2]/span/text()")[0]
        salaryInYear = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[2]/div[1]/span[1]/text()")[0].replace(' per year', '')
        salaryInHour = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[2]/div[1]/span[2]/text()")[0].replace(' per hour', '')
        employeeTitle = self.tree.xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div[2]/div[2]/span/text()")[0]
        return{
            "company_data":{
                "shortCompanyName":f"{shortCompanyName}",
                "longCompanyName":f"{longCompanyName}",
                "companyDescription":f"{companyDescription}",
                "salaryInYear":f"{salaryInYear}",
                "salaryInHour":f"{salaryInHour}",
                "employeeTitle":f"{employeeTitle}",
            }
        }

    def result(self):
        result = list()
        for i in range(self.number):
            data = list()
            page = requests.get(self.url)
            self.tree = html.fromstring(page.content)
            if self.personal_data:
                data+=list(self.get_personal_data().items())
            if self.bank_data:
                data+=list(self.get_bank_data().items())
            if self.cryptocurrency_data:
                data+=list(self.get_cryptocurrency_data().items())
            if self.internet_data:
                data+=list(self.get_internet_data().items())
            if self.education_data:
                data+=list(self.get_education_data().items())
            if self.company_data:
                data+=list(self.get_company_data().items())
            result.append(dict(data))
        return result
