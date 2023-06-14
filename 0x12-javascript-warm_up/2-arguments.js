#!/usr/bin/node

if (process.argv.length > 2) {
    for (let i = 2; i < process.argv.length; i++)
    {
        isFounded = "Argument found";
    }
} 
else {
    isFounded = "No argument";
}

console.log(isFounded);
