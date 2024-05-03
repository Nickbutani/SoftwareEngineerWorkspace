const items = require('./fakeDb');

class Item {
    constructor(name, price) {
        this.name = name;
        this.price = price;
        items.push(this);
    }

    static findAll() {
        return items;
    }

    static find(name) {
        return items.find(i => i.name === name);
    }

    static update(name, data) {
        let item = Item.find(name);
        if (item === undefined) {
            throw { message: "Not Found", status: 404 };
        }
        item.name = data.name;
        item.price = data.price;
        return item;
    }

    static remove(name) {
        let index = items.findIndex(i => i.name === name);
        if (index === -1) {
            throw { message: "Not Found", status: 404 };
        }
        items.splice(index, 1);
    }
}

module.exports = Item;