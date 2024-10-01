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

        if (this.personalData) {
            data.personalData = {
                // ... (same as before)
            };
        }

        // ... (same as before)

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
