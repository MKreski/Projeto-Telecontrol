function test() {
    
    var uid = document.getElementById("Nome").value;
    var empresa = document.getElementById("Empresa").value;
    var Email = document.getElementById("Email").value;
    var Problema = document.getElementById("problema").value;
    var local = document.getElementById("local").value;
    var urgencia = document.getElementById("Urgência").value;
    
    
    var uid = localStorage.setItem("uid", uid);
    var empresa = localStorage.setItem("empresa", empresa);
    var Email = localStorage.setItem("Email", Email);
    var Problema = localStorage.setItem("Problema", Problema);
    var local = localStorage.setItem("Local", local);
    var urgencia = localStorage.setItem("Urgência", urgencia);

    //pegar dados e usar (cpa vai precisar ver isso Kreski)

    var uid = localStorage.getItem("uid", uid);
    var empresa = localStorage.getItem("empresa", empresa);
    var Email = localStorage.getItem("Email", Email);
    var Problema = localStorage.getItem("Problema", Problema);
    var local = localStorage.getItem("Local", local);
    var urgencia = localStorage.getItem("Urgência", urgencia);

}