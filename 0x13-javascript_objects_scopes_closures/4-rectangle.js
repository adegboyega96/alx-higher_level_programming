#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return Object.create(Rectangle.prototype);
    }

    this.width = w;
    this.height = h;
  }

  print () {
    let rows = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rows += 'X';
      }
      if (i < this.height - 1) rows += '\n';
    }
    console.log(rows);
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
