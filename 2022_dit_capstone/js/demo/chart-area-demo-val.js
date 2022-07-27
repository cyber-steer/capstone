import {dayCount, selectTest} from "../db/firebase-connect.js";
// selectTest()
let count = await dayCount();
console.log("count out : "+count)
