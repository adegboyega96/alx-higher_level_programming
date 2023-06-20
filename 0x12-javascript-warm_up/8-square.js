#!/usr/bin/node

let rows = '';
if (isNaN(process.argv[2]))
{
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < process.argv[2]; i++)
    {
        for (let j = 0; j < process.argv[2]; j++)
        {
            rows += "X";
        }
        rows += "\n";
    }
    console.log(rows);
}
