var restart=document.querySelector("#b");
var squares=document.querySelectorAll("td");

// 칸을 클릭하면 표시가 되도록 만들어준다.

function changeMarker(){
    if(this.textContent===""){
        this.textContent="X";
    }else if (this.textContent==="X"){
        this.textContent='O';
    }else{
        this.textContent="";
    }
}

// restart버튼을 누르면 게임이 초기화되도록 해준다.


function clearBoard(){
    for (var i=0; i<squares.length; i++){
        squares[i].textContent="";
    }
}

restart.addEventListener('click', clearBoard)


for (var i=0; i<squares.length; i++){
    squares[i].addEventListener('click', changeMarker);
}