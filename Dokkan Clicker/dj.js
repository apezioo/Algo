let lads = document.getElementById('ds')
score1 = 0
ajout=1
lads.addEventListener('click', function(){
    score = document.getElementById('score')    
    score1 += ajout
    score.textContent = score1
})
    
let upclick1 = document.getElementById('upclick1')
upclick1.addEventListener('click', function(){
    if (score1 >= 1000){
    ajout*=2
    upclick1.removeEventListener('click', arguments.callee);
    upclick1.style.filter = 'grayscale(100%)';
    score1 -= 1000
    score.textContent = score1
    }
})


let upclick2 = document.getElementById('upclick2')
upclick2.addEventListener('click', function(){
    if (score1 >= 10000){
    ajout*=2
    upclick2.removeEventListener('click', arguments.callee);
    upclick2.style.filter = 'grayscale(100%)';
    score1 -= 10000
    score.textContent = score1
    }
})

let upclick3 = document.getElementById('upclick3')
upclick3.addEventListener('click', function(){
    if (score1 >= 100000){
        ajout*=2
        upclick3.removeEventListener('click', arguments.callee);
        upclick3.style.filter = 'grayscale(100%)';
        score1 -= 100000
        score.textContent = score1
        }
})

let upclick4 = document.getElementById('upclick4')
upclick4.addEventListener('click', function(){
    if (score1 >= 1000000){
        ajout*=2
        upclick4.removeEventListener('click', arguments.callee);
        upclick4.style.filter = 'grayscale(100%)';
        score1 -= 1000000
        score.textContent = score1
        }
})

let upclick5 = document.getElementById('upclick5')
upclick5.addEventListener('click', function(){
    if (score1 >= 10000000){
        ajout*=2
        upclick5.removeEventListener('click', arguments.callee);
        upclick5.style.filter = 'grayscale(100%)';
        score1 -= 10000000
        score.textContent = score1
        }
})

let upclick6 = document.getElementById('upclick6')
upclick6.addEventListener('click', function(){
    if (score1 >= 100000000){
        ajout*=2
        upclick6.removeEventListener('click', arguments.callee);
        upclick6.style.filter = 'grayscale(100%)';
        score1 -= 100000000
        score.textContent = score1
        }
})

let upclick7 = document.getElementById('upclick7')
upclick7.addEventListener('click', function(){
    if (score1 >= 1000000000){
        ajout*=2
        upclick7.removeEventListener('click', arguments.callee);
        upclick7.style.filter = 'grayscale(100%)';
        score1 -= 1000000000
        score.textContent = score1
        }
})
