function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
//쿠키로 부터 csrftoken 값을 읽어와 저장하는 코드이다!

function csrfSafeMethod(method){
    return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if(!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
)};
