// // version 1
// function conversion(){
//     let distance = Number(prompt("How many meters?: "));
//     let feet = distance * 0.3048;
//     return feet;
// }

// let x = conversion();
// alert(x);



// version 2 (comment out version 3 when testing)
// let unit_dict = {
//     'ft': 0.3048,
//     'mi': 1609.34,
//     'm': 1,
//     'km': 1000,
// }

// let unit = prompt("Which unit of measurement?: ");
// let distance = Number(prompt("How many meters?: "));
// let unit_value = unit_dict[unit]
// let total = distance * unit_value
// alert(total)


// version 3 (comment out version 2 when testing)
// let unit_dict = {
//     'ft': 0.3048,
//     'mi': 1609.34,
//     'm': 1,
//     'km': 1000,
//     'yd': 0.9144,
//     'in': 0.0254,
// }

// let unit = prompt("Which unit of measurement?: ");
// let distance = Number(prompt("How many meters?: "));
// let unit_value = unit_dict[unit]
// let total = distance * unit_value
// alert(total)



// version 4
let unitDict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

let distance = Number(prompt("What is the distance?: "));
let inputUnit = prompt("What is the starting unit of measurement?: ");
let outputUnit = prompt("Which unit of measurement would you like to convert to?: ");
let unitValue = unitDict[inputUnit];
let total = distance * unitValue;
let conversion = total * unitDict[outputUnit];


// f string javascript equivalent
x = `${distance}${inputUnit} is equal to ${conversion}${outputUnit}`
alert(x)