import { initializeApp } from  '/node_modules/firebase/app/dist/index.cjs.js';
import { getDatabase} from '/node_modules/firebase/database/dist/public.d.ts';
// import { getDatabase, ref,get, set, child, update, remove } from '/node_modules/firebase/database/dist/public.d.ts';
// node_modules/firebase/database/dist/public.d.ts
// node_modules\@firebase\database\dist\public.d.ts
// node_modules\@firebase\database\dist\public.d.ts
// 




const firebaseConfig = {
    apiKey: "AIzaSyBETK45cbP1g2ZYC03ras5UYys5fXAqV_4",
    authDomain: "fir-course-edb8c.firebaseapp.com",
    databaseURL: "https://fir-course-edb8c-default-rtdb.firebaseio.com",
    projectId: "fir-course-edb8c",
    storageBucket: "fir-course-edb8c.appspot.com",
    messagingSenderId: "760960563313",
    appId: "1:760960563313:web:eb3b145202888f8a3c83d0",
    measurementId: "G-336MJ5MK72"
  };

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);


const select = function(){
    const dbref = ref(db);

    get(child(dbref,"test")).then((snapshot)=>{
        if(snapshot.exists()){
            let arr = [];
            snapshot.forEach(childSnapshot=>{
                console.log(childSnapshot.val());
                arr.push(childSnapshot.val());
            })
            console.log(arr);
        }
        else{
            console.log("not data");
        }
    })
    .catch((error)=>{
        console.log("error : "+error);
    });
}
// const select = function(){
//     console.log("select");
// }
export {select};