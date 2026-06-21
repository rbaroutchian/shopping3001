
function sendArticleComment(articleId){
    event.preventDefault();
    var comment = $('#commentText').val();
    var parentId = $('#parentId').val() || null;
    console.log("Parent ID:", parentId);
    $.post('/article/add-article-comment/',{
     articleComment : comment ,
     articleID : articleId,
     parentId : parentId,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

    }).then(res=>{
        console.log("Response:", res);
        $('#comment_list').html(res);
        $('#commentText').val('');
        $('#parentId').val('');




        if (parentId !== null && parentId !==''){
            let newcomment=document.getElementById('single_comment_box_' + parentId);
            if (newComment) {
                newComment.scrollIntoView({ behavior: 'smooth' });
            }
            // scrollIntoView({behavior:'smooth'})
        }
        else {
            let lastComment=document.querySelector("#comment_list > div:last-child");
             if (lastComment) {
                lastComment.scrollIntoView({ behavior: 'smooth' });
            }
            // scrollIntoView({behavior:'smooth'})

        }
        })
    .fail(function(err) {
        console.error("Error:", err);
    });
}


function fillParentId(parentId){
    $('#parentId').val(parentId);
    document.getElementById('commentForm').scrollIntoView({behavior:"smooth"})
}


function addProductToOrder(productId) {
    const productCount = $('#product_count').val() || 1;
    $.get('/order/add-to-order/?product_id='+productId+'&count='+productCount).then(res =>{

        Swal.fire({
          title: " اعلان! ",
          text: res.text,
          icon: res.icon,
          showCancelButton: false,
          confirmButtonColor: "#3085d6",
          confirmButtonText: res.confirm_button_text
        }).then((result) => {
          if (result.isConfirmed && res.status === 'not_logged_in') {
              window.location.href='/account/login/'
          }
        });
    });
}


function updateOrderDetailContent(url) {
    fetch(url, {
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })
        .then(response => response.json())
        .then(res => {
            const orderDetailContainer = document.getElementById('order-detail-container');
            if (res.status === 'success' && orderDetailContainer) {
                orderDetailContainer.innerHTML = res.body;
            } else {
                console.error("Basket update failed:", res);
            }
        })
        .catch(err => {
            console.error("Basket request failed:", err);
        });
}

window.removeOrderDetail = function (detailId) {
    updateOrderDetailContent('/user-panel/remove-order-detail?detail_id=' + encodeURIComponent(detailId));
}

window.changeOrderDetailCount = function (detailId, state) {
    updateOrderDetailContent(
        '/user-panel/change-order-detail?detail_id=' + encodeURIComponent(detailId) +
        '&state=' + encodeURIComponent(state)
    );
}


