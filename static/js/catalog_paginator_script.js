window.onload = () => {
    $('.cat').on('click', 'a[name="paginator"]', () => {
        let target_href = event.target;
        if (target_href.localName === 'i'){
            target_href = target_href.parentElement
        }
        if (target_href) {
            $.ajax({
                url: target_href.href,
                success: (data) => {
                    $('.catalog').empty()
                    $('.catalog').append($(data).find('.catalog').html())
                    $('.paginator').empty()
                    $('.paginator').append($(data).find('.paginator').html())
                },
            });
        }
        event.preventDefault();
    });
};