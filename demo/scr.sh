export URL='https://6ehywu4ung.execute-api.us-east-2.amazonaws.com/init'
 
## WE SUBMIT THE POSTER FROM THE THRILLER/CRIME MOVIE HOSTAGE
export PIC='sun.jpg'
 
## WE SEND THE IMAGE OVER TO THE API
(echo -n '{"data": "'; base64 $PIC; echo '"}') | curl -H "Content-Type: application/json" -d @- $URL
 
