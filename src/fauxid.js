const axios = require('axios');
const cheerio = require('cheerio');

class Fauxid {
    constructor(options = {}) {
        this.country = options.country || null;
        this.number = options.number || 10;
        this.personalData = options.personalData || true;
        this.bankData = options.bankData || true;
        this.cryptocurrencyData = options.cryptocurrencyData || true;
        this.internetData = options.internetData || true;
        this.educationData = options.educationData || true;
        this.companyData = options.companyData || true;

        this.url = this.country ? `${this.country}` : "https://fauxid.com/fake-name-generator/";
    }

    async getData() {
        const response = await axios.get(this.url);
        const $ = cheerio.load(response.data);
        const data = {};

        if (this.personal_data) {
            data.personal_data = {
                name: $('div.name span').text(),
                address: $('div.address address').text().replace(/
/g, ''),
                phone: $('div.phone span').text(),
                socialSecurityNumber: $('div.ssn span').text(),
                dateOfBirth: $('div.dob span:first-child').text(),
                height: $('div.height span:last-child').text(),
                weight: $('div.weight span:last-child').text(),
                gender: $('div.gender span').text(),
                hairColor: $('div.hair-color span').text(),
                eyeColor: $('div.eye-color span').text(),
                ethnicity: $('div.ethnicity span').text(),
                bloodType: $('div.blood-type span').text()
            };
        }

        if (this.bank_data) {
            data.banking_data = {
                creditCardNumber: $('div.credit-card span code').text(),
                expDate: $('div.credit-card-expiration span:first-child').text(),
                cvv: $('div.credit-card-expiration span:last-child').text(),
                bankName: $('div.bank-name span').text(),
                bankAccountNumber: $('div.bank-account span code').text(),
                routingNumber: $('div.routing-number span code').text(),
                iban: $('div.iban span code').text()
            };
        }

        if (this.cryptocurrency_data) {
            data.cryptocurrency_data = {
                bitcoinAddress: $('div.bitcoin span code').text(),
                ethereumAddress: $('div.ethereum span code').text()
            };
        }

        if (this.internet_data) {
            data.internet_data = {
                username: $('div.username span').text(),
                password: $('div.password span code').text(),
                uniqueUserIdentifier: $('div.uuid span code').text(),
                IPAddressIPv4: $('div.ipv4 span code').text(),
                IPAddressLocal: $('div.local-ip span code').text(),
                MACAddress: $('div.mac-address span code').text(),
                IPAddressIPv6: $('div.ipv6 span code').text(),
                website: $('div.website span').text()
            };
        }

        if (this.education_data) {
            data.education_data = {
                educationLevel: $('div.education-level span').text(),
                university: $('div.university span').text()
            };
        }

        if (this.company_data) {
            data.company_data = {
                shortCompanyName: $('div.company-name span:first-child').text(),
                longCompanyName: $('div.company-name span:last-child').text(),
                companyDescription: $('div.company-description span').text(),
                salaryInYear: $('div.salary span:first-child').text().replace(' per year', ''),
                salaryInHour: $('div.salary span:last-child').text().replace(' per hour', ''),
                employeeTitle: $('div.employee-title span').text()
            };
        }

        return data;
    }

    async result() {
        const results = [];
        for (let i = 0; i < this.number; i++) {
            const data = await this.getData();
            results.push(data);
        }
        return results;
    }
}

module.exports = Fauxid;
