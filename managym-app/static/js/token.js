function getCookie(name) {
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
}

$.ajaxSetup({
    // fonction appelée avant d'envoyer une requête AJAX
    beforeSend: function(xhr, settings) {
         // on ajoute le header que si la requête est pour le site en cours
         // (URL relative) et est de type POST
         if (!/^https?:.*/.test(settings.url)  && settings.type == "POST") {
             // attachement du token dans le header
             xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
         }
     }
});