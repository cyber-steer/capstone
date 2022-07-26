# capstone_web

프로젝트 소개와 팀 소개 그리고 관리자가 동아리방 출입관리<br>

index.html이 메인 화면<br>
index2.html이 관리자가 로그인뒤 메인화면<br>
<br>
주요 페이지 management.html이 전체적인 통계를 보여주는 페이지로<br>
차트는 canvas태그를 이용해 자바스크립트로 표현<br>
management.html 소스 제일 하단의 sciprt태그에<br>
js/demo/chart-area-demo.js<br>
js/demo/chart-pie-demo.js<br>
위 두 자바스크립트 파일이 canvas태그를 꾸며줌<br>
<br>
차트를 꾸밀때 firebase와 연동해서 데이터를 가져와 통계를 내줌<br>
<br>
<br>
<hr>
<br>
tmp 폴더가 테스트용<br>
<br>
tmp/hello_test의 index.html hello를 콘솔에 찍는 함수를 import하는 파일<br>
실행시 콘솔창에 에러 출력<br>
<br>
파이어폭스 : 교차 출처 요청 차단: 동일 출처 정책으로 인해 file:///C:/Users/admin/Desktop/web/levelTest/index.js에 있는 원격 리소스를 차단하였습니다. (원인: http가 아닌 CORS 요청).<br>
<br>
크롬 : Access to script at 'file:///C:/Users/admin/Desktop/capstone_web/tmp/hello_test/index.js' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, chrome-untrusted, https.<br>
Failed to load resource: net::ERR_FAILED<br>
<br>
tmp/hello_test를 npx http-server 해서 로컬서버로 실행시 hello 출력됨<br>
<br>
서버없이 파일로 만 실행했을시 에러가 발생하고<br>
서버로 실행하면 문제가 없다는게 의문<br>
그리고 다른 API없이 단순한 로직임이에도 불구하고 CORS가 왜 뜨는지<br>
<br>
<br>
tmp/firebase_test/index.html 파이어베이스 API를 모듈화하려고 시도<br>
tmp/firebase_test/index-module.html script태그에 type="module"추가<br>
<br>
<br>
index.html 에러 <br>
파이어폭스 : Uncaught SyntaxError: import declarations may only appear at top level of a module<br>
크롬 : Uncaught SyntaxError: Cannot use import statement outside a module<br>

index-modul.html 에러<br>
파이어폭스 : 교차 출처 요청 차단: 동일 출처 정책으로 인해 file:///C:/Users/admin/Desktop/test/firebase_test/index.js에 있는 원격 리소스를 차단하였습니다. (원인: http가 아닌 CORS 요청).<br>
크롬 : index-modul.html:1 Access to script at 'file:///C:/Users/admin/Desktop/test/firebase_test/index.js' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, chrome-untrusted, https.<br>
Failed to load resource: net::ERR_FAILED<br>