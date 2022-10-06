
let week = [];

for(let i =6; i>=0; i--){
    let date = new Date()
    date.setDate(date.getDate()-i);
    date.setHours(date.getHours()+9);
    date = date.toISOString()+"";
    week.push(date.substr(0,10));
}
console.log(week)

// let month = []
// for(let i=13; i>=0; i--){
//     let date = new Date()
//     date.setMonth(date.getMonth()-i);
//     date.setHours(date.getHours()+9);
//     date = date.toISOString()+"";
//     month.push(date.substr(0,7));
// }
// console.log(month)

// arr = [1,2,3,4,5]
// arr.array.forEach(i => {
//     console.log(i);
//     if(i >3){
//         break;
//     }});

