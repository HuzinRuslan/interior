window.onload = ()=> {
    $('.basket_list').on('click', 'input[type="number"]', ()=>{
        let target_href = event.target;

        if (target_href) {
            $.ajax({
                url:'/basket/edit/' + target_href.name + '/' + target_href.value+ '/',
                success: (data) => {
                    $('.basket_list').html(data.result);
                },
            });
        }
        event.preventDefault();
    });
};