(function(){
    const btnEliminacion=document.querySelectorAll('.btnElimi')

// para recorrer el elemento
btnEliminacion.forEach(btn=>{
    // evento listener 
    btn.addEventListener('click', (e)=>{
        const confirmar=confirm('Seguro de eliminar.')
        // si el mensaje d confirmar es  false, se cancela el evento mediante preventDefault
        if(!confirmar) {
            e.preventDefault();
        }
    })
})

})();