$(document).ready(function(){

    // TODO: initial index and tell where its goes

    page_index = 0;

    function addNewMessaheColumn(dataset, index)
    {
        messageContainer = document.getElementById('noticesContainer');
        messageContainer.innerHTML = ""
        for(var i = 0; i < dataset.length; i++)
        {
            horizontal_colII = document.createElement('div');
            horizontal_colII.className = "horizontal_colII";
            order = document.createElement('div');
            order.className = "order";
            p_tag = document.createElement('p')
            p_tag.innerText = index*5+1+i;
            order.appendChild(p_tag);
            horizontal_colII.appendChild(order);
            notice_content = document.createElement('div');
            notice_content.className = "notice_content";
            p_tag_item = document.createElement('p');
            p_tag_item.innerText = dataset[i];
            notice_content.appendChild(p_tag_item);
            horizontal_colII.appendChild(notice_content);
            spaceholderIII = document.createElement('div');
            spaceholderIII.className = "spaceholderIII";

            messageContainer.appendChild(horizontal_colII);
            messageContainer.appendChild(spaceholderIII);
        }
    }

    // TODO: Ajax Get

    $('#previous').click(function(){

        page_index -= 1;
        if(page_index < 0)
        {
            swal({
               title: "Error!",   text: "You have reach the first page!",   type: "error",   confirmButtonText: "Cool"
            });
            page_index = 0
        }


        else {

            $.ajax({
                type: "POST",
                url: "/client/ajax/post/",
                dataType: "json",
                data: {"message": "previous", "index": page_index},
                success: function (data) {
                    addNewMessaheColumn(data, page_index);
                },
                failure: function (errMsg) {
                    alert(errMsg);
                }
                ,
            });
        }

        console.log(page_index);

    });

    // TODO: Ajax Post

    $('#next').click(function(){

        page_index += 1

        $.ajax({

            type: "POST",
            url: "/client/ajax/post/",
            dataType: "json",
            data: {"message": "next", "index": page_index},
            success: function(data){
                if(data['0'] == "error"){
                    page_index = data['1'] - 1;
                    swal({
                        title: "Error!",   text: "You have reach the last page!",   type: "error",   confirmButtonText: "Cool"
                    });
                }else{
                    addNewMessaheColumn(data, page_index);
                }
            },

            failure: function(errMsg){
                alert(errMsg);
            },

        });

        console.log(page_index);

    });

    // TODO: CRSF code

    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});